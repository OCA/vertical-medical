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
    sale_wizard_ids = fields.Many2many(
        string='Orders',
        help=_('Orders to create when wizard is completed'),
        comodel_name='medical.sale.wizard',
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
                    'Patient and Customers are currently identical concepts'
                ))
            elif self.split_orders == 'patient':
                order_map[rx_line.patient_id].append(rx_line)
            else:
                order_map[None].append(rx_line)

        for order in order_map.values():
            
            order_lines = list((0, 0, {
                'product_id': l.medical_medication_id.product_id.id,
                'product_uom_id': l.medical_medication_id.product_id.uom_id.id,
                'product_uom_qty': l.qty,
                'price_unit': l.list_price,
                'patient_id': l.patient_id.id,
                
            }) for l in self.prescription_id.prescription_order_line_ids)
            
            order_inserts.append((0, 0, {
                'prescription_wizard_id': self.id,
                'partner_id': self.patient_id.id,
                'partner_invoice_id': self.patient_id.id,
                'partner_shipping_id': self.patient_id.id,
                'prescription_order_id': self.prescription_id.id,
                'order_line': order_lines,
            }))
        
        self.write({
            'sale_wizard_ids': order_inserts,
            'state': 'start',
        })
        return self._next_wizard()
    
    @api.multi
    def _wizard_action_iter(self, only_states=None, ):
        self.ensure_one()
        model_obj = self.env['ir.model.data']
        wizard_id = model_obj.xmlid_to_object(
            'medical_pharmacy.medical_sale_wizard_view_form'
        )
        action_id = model_obj.xmlid_to_object(
            'medical_sale_wizard_action'
        )
        context = self._context.copy()
        for wizard in self.sale_wizard_ids:
            if only_states and wizard.state in only_states:
                continue
            yield {
                'name': action_id.name,
                'help': action_id.help,
                'type': action_id.type,
                'views': [
                    (wizard_id.id, 'form'),
                ],
                'target': action_id.target,
                'context': context,
                'res_model': action_id.res_model,
            }
            
    @api.model
    def next_wizard(self, ):
        try:
            return next(self._wizard_action_iter(['draft']))
        except StopIteration:
            self.state = 'partial'
            wizard_id = model_obj.xmlid_to_object(
                'medical_pharmacy.medical_rx_sale_wizard_view_form'
            )
            action_id = model_obj.xmlid_to_object(
                'medical_rx_sale_wizard_action'
            )
            return {
                'name': action_id.name,
                'help': action_id.help,
                'type': action_id.type,
                'views': [
                    (wizard_id.id, 'form'),
                ],
                'target': action_id.target,
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
