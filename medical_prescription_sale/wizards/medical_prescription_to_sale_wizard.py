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
    _name = 'rx.sale.wizard'
    _description = 'Convert Medical Prescription Line(s) to Sale Order(s)'

    def _compute_default_session(self, ):
        return self.env['medical.prescription.order.line'].browse(
            self._context.get('active_ids')
        )

    prescription_line_ids = fields.Many2many(
        string='Prescription',
        comodel_name='medical.prescription.order.line',
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
        required=True,
        default=fields.Datetime.now,
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        help=_('Pharmacy to dispense orders from'),
        comodel_name='medical.pharmacy',
        required=True,
    )
    sale_wizard_ids = fields.One2many(
        string='Orders',
        help=_('Orders to create when wizard is completed'),
        comodel_name='medical.sale.wizard',
        inverse_name='prescription_wizard_id',
    )
    state = fields.Selection([
        ('new', _('Not Started')),
        ('start', _('Started')),
        ('partial', _('Open')),
        ('done', _('Completed')),
    ],
        readonly=True,
        default='new',
    )
    warehouse_id = fields.Many2one(
        string='Warehouse',
        comodel_name='stock.warehouse',
        required=True,
    )

    @api.multi
    def create_sale_wizards(self, ):

        self.ensure_one()
        order_map = defaultdict(list)
        order_inserts = []

        for rx_line in self.prescription_line_ids:
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
            for l in self.prescription_line_ids:
                medicament_id = l.medical_medication_id.medicament_id
                order_lines.append((0, 0, {
                    'product_id': medicament_id.product_id.id,
                    'product_uom': medicament_id.product_id.uom_id.id,
                    'product_uom_qty': l.quantity,
                    'price_unit': medicament_id.product_id.list_price,
                    'prescription_order_line_id': l.id,
                    'patient_id': l.patient_id.id,
                }))

            if order.patient_id.property_product_pricelist:
                pricelist_id = order.patient_id.property_product_pricelist.id
            else:
                pricelist_id = False

            order_inserts.append((0, 0, {
                'partner_id': order.patient_id.partner_id.id,
                'pricelist_id': pricelist_id,
                'partner_invoice_id': order.patient_id.id,
                'partner_shipping_id': order.patient_id.id,
                'prescription_order_id': order.prescription_order_id.id,
                'pharmacy_id': self.pharmacy_id.id,
                'client_order_ref': order.prescription_order_id.name,
                'order_line': order_lines,
                'date_order': self.date_order,
                'origin': order.prescription_order_id.name,
                'warehouse_id': self.warehouse_id.id,
                'user_id': self.env.user.id,
                'company_id': self.env.user.company_id.id,
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
        action = self._get_next_sale_wizard(['new', 'start'])
        _logger.debug('Got action: %s', action)
        if action:
            return action
        else:
            self.state = 'done'
            return self.do_rx_sale_conversions()

    @api.multi
    def do_rx_sale_conversions(self, ):
        self.ensure_one()
        sale_obj = self.env['sale.order']
        sale_ids = None
        for sale_wizard_id in self.sale_wizard_ids:
            sale_vals = sale_wizard_id._to_vals()
            _logger.debug(sale_vals)
            sale_id = sale_obj.create(sale_vals)
            try:
                sale_ids += sale_id
            except TypeError:
                sale_ids = sale_id
        model_obj = self.env['ir.model.data']
        form_id = model_obj.xmlid_to_object('sale.view_order_form')
        tree_id = model_obj.xmlid_to_object('sale.view_quotation_tree')
        action_id = model_obj.xmlid_to_object('sale.action_quotations')
        context = self._context.copy()
        _logger.info('Created %s', sale_ids)
        _logger.debug('%s %s %s', form_id, tree_id, action_id)
        sale_ids = [s.id for s in sale_ids]
        return {
            'name': action_id.name,
            'help': action_id.help,
            'type': action_id.type,
            'view_mode': 'tree',
            'view_id': tree_id.id,
            'views': [
                (tree_id.id, 'tree'), (form_id.id, 'form'),
            ],
            'target': 'current',
            'context': context,
            'res_model': action_id.res_model,
            'res_ids': sale_ids,
            'domain': [('id', 'in', sale_ids)],
        }
