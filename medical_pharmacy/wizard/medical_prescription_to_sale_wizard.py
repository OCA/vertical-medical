# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api, fields, _
from collections import defaultdict
import logging


_logger = logging.getLogger(__name__)


class MedicalRxSaleWizard(models.TransientModel):
    _name = 'medical.rx.sale.wizard'
    _description = 'Convert Medical Prescription(s) to Sale Order(s)'

    def _compute_default_session(self, ):
        return self.env['medical.prescription.order'].browse(
            self._context.get('active_id')
        )
    
    def _compute_default_patient(self, ):
        if self.prescription_id:
            return self.prescription_id.patient_id
        else:
            return self._compute_default_session().patient_id
    
    prescription_id = fields.Many2one(
        string='Prescription',
        comodel_name='medical.prescription.order',
        default=_compute_default_session,
        required=True,
        readonly=True,
    )
    split_orders = fields.Selection([
        ('partner', 'By Customer'),
        ('patient', 'By Patient'),
        ('all', 'By Rx Line'),
    ],
        default='patient',
        required=True,
        help=_('How to split the new orders'),
    )
    date_order = fields.Datetime(
        help=_('Date for the new orders'),
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        help=_('Pharmacy to dispense orders from'),
        comodel_name='medical.pharmacy',
    )
    sale_wizard_ids = fields.One2many(
        string='Orders',
        help=_('Orders to create when wizard is completed'),
        comodel_name='medical.sale.wizard',
        inverse_name='prescription_wizard_id',
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        default=_compute_default_patient,
        readonly=True,
    )
    state = fields.Selection([
        ('new', _('Not Started')),
        ('start', _('Started')),
        ('partial', _('Wizards Complete')),
        ('done', _('Completed')),
    ],
        readonly=True,
        default='new',
    )
    
    @api.multi
    def create_sale_wizards(self, ):
        
        self.ensure_one()
        order_map = defaultdict(list)
        order_inserts = []
        
        for rx_line in self.prescription_id.prescription_order_line_ids:
            if self.split_orders == 'partner':
                raise NotImplementedError(_(
                    'Patient and Customers are currently identical concepts.'
                ))
            elif self.split_orders == 'patient':
                order_map[rx_line.patient_id].append(rx_line)
            else:
                order_map[None].append(rx_line)

        for order in order_map.values():
            
            order_lines = []
            for l in self.prescription_id.prescription_order_line_ids:
                medicament_id = l.medical_medication_id.medicament_id
                order_lines.append((0, 0, {
                    'product_id': medicament_id.product_id.id,
                    'product_uom_id': medicament_id.product_id.uom_id.id,
                    'product_uom_qty': l.qty,
                    'price_unit': medicament_id.product_id.list_price,
                    'patient_id': l.patient_id.id,
                }))
            
            order_inserts.append((0, 0, {
                #'prescription_wizard_id': [(4, self.id, 0)],
                'partner_id': self.patient_id.id,
                'partner_invoice_id': self.patient_id.id,
                'partner_shipping_id': self.patient_id.id,
                'prescription_order_id': self.prescription_id.id,
                'state': 'draft',
                'order_line': order_lines,
            }))
        
        _logger.debug(order_inserts)
        
        self.write({
            'sale_wizard_ids': order_inserts,
            'state': 'start',
        })
        
        return self.next_wizard()
    
    @api.model
    def _get_next_sale_wizard(self, only_states=None, ):
        model_obj = self.env['ir.model.data']
        wizard_id = model_obj.xmlid_to_object(
            'medical_pharmacy.medical_sale_wizard_view_form'
        )
        action_id = model_obj.xmlid_to_object(
            'medical_pharmacy.medical_sale_wizard_action'
        )
        context = self._context.copy()
        for wizard in self.sale_wizard_ids:
            _logger.debug(wizard)
            if only_states and wizard.state not in only_states:
                continue
            context['active_id'] = wizard.id
            return {
                'name': action_id.name,
                'help': action_id.help,
                'type': action_id.type,
                'views': [
                    (wizard_id.id, 'form'),
                ],
                'target': 'new',
                'context': context,
                'res_model': action_id.res_model,
                'res_id': wizard.id,
            }
        return False
            
    @api.model
    def next_wizard(self, ):
        action = self._get_next_sale_wizard(['draft'])
        _logger.debug('Got action: %s', action)
        if action:
            return action
        else:
            self.state = 'partial'
            model_obj = self.env['ir.model.data']
            wizard_id = model_obj.xmlid_to_object(
                'medical_pharmacy.medical_rx_sale_wizard_view_form'
            )
            action_id = model_obj.xmlid_to_object(
                'medical_pharmacy.medical_rx_sale_wizard_action'
            )
            context = self._context.copy()
            return {
                'name': action_id.name,
                'help': action_id.help,
                'type': action_id.type,
                'views': [
                    (wizard_id.id, 'form'),
                ],
                'target': 'new',
                'context': context,
                'res_model': action_id.res_model,
            }

    @api.one
    def do_rx_sale_conversions(self, ):
        sale_obj = self.env['sale.order']
        sale_ids = None
        for sale_wizard_id in self.sale_wizard_ids:
            sale_id = sale_obj.create(sale_wizard_id._to_vals())
            try:
                sale_ids += sale_id
            except TypeError:
                sale_ids = sale_id
        return sale_ids
