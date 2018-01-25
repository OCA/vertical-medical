# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import api, fields, models
from collections import defaultdict
import logging


_logger = logging.getLogger(__name__)


class MedicalSaleWizard(models.TransientModel):
    _name = 'medical.sale.wizard'
    _description = 'Medical Sale Wizard'

    prescription_line_ids = fields.Many2many(
        string='Prescription',
        comodel_name='medical.prescription.order.line',
        default=lambda s: s._compute_default_session(),
        required=True,
        readonly=True,
    )
    split_orders = fields.Selection(
        string='Split Orders',
        selection=[
            ('patient', 'By Patient'),
        ],
        default='patient',
        required=True,
        help='How to split the new orders',
    )
    date_order = fields.Datetime(
        help='Date For The New Orders',
        required=True,
        default=lambda s: fields.Datetime.now(),
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        help='Pharmacy to dispense orders from',
        comodel_name='medical.pharmacy',
        required=True,
        default=lambda s: s._compute_default_pharmacy(),
    )
    sale_wizard_ids = fields.One2many(
        string='Orders',
        help='Orders to create when wizard is completed',
        comodel_name='medical.sale.temp',
        inverse_name='prescription_wizard_id',
    )
    state = fields.Selection(
        selection=[
            ('new', 'Not Started'),
            ('start', 'Started'),
            ('partial', 'Open'),
            ('done', 'Completed'),
        ],
        readonly=True,
        default='new',
    )

    def _compute_default_session(self):
        return self.env['medical.prescription.order.line'].browse(
            self._context.get('active_ids')
        )

    def _compute_default_pharmacy(self):
        default_order_lines = self._compute_default_session()
        if len(default_order_lines):
            return default_order_lines[0].prescription_order_id.partner_id

    @api.multi
    def action_create_sale_wizards(self):

        self.ensure_one()
        order_map = defaultdict(list)
        order_inserts = []

        for rx_line in self.prescription_line_ids:
            order_map[rx_line.patient_id].append(rx_line)

        for patient, order in order_map.items():
            order_lines = []
            rx_orders = self.env['medical.prescription.order'].browse()

            for rx_line in self.prescription_line_ids:
                medicament = rx_line.medical_medication_id.medicament_id
                order_lines.append((0, 0, {
                    'product_id': medicament.product_id.id,
                    'product_uom': medicament.product_id.uom_id.id,
                    'product_uom_qty': rx_line.qty,
                    'price_unit': medicament.product_id.list_price,
                    'prescription_order_line_id': rx_line.id,
                }))
                rx_orders += rx_line.prescription_order_id
            rx_orders = set(rx_orders)

            if patient.property_product_pricelist:
                pricelist_id = patient.property_product_pricelist.id
            else:
                pricelist_id = False

            rx_order_ids = [(4, p.id, 0) for p in rx_orders]
            client_order_ref = ', '.join(
                p.name for p in rx_orders
            )

            partner = patient.partner_id
            order_inserts.append((0, 0, {
                'partner_id': partner.id,
                'patient_id': patient.id,
                'pricelist_id': pricelist_id,
                'partner_invoice_id': partner.id,
                'partner_shipping_id': partner.id,
                'prescription_order_ids': rx_order_ids,
                'pharmacy_id': self.pharmacy_id.id,
                'client_order_ref': client_order_ref,
                'order_line': order_lines,
                'date_order': self.date_order,
                'origin': client_order_ref,
                'user_id': self.env.user.id,
                'company_id': self.env.user.company_id.id,
            }))

        _logger.debug(order_inserts)

        self.write({
            'sale_wizard_ids': order_inserts,
            'state': 'start',
        })
        return self.action_next_wizard()

    @api.model
    def _get_next_sale_wizard(self, only_states=None):
        model_obj = self.env['ir.model.data']
        wizard = model_obj.xmlid_to_object(
            'sale_medical_prescription.medical_sale_temp_view_form'
        )
        action = model_obj.xmlid_to_object(
            'sale_medical_prescription.medical_sale_temp_action'
        )
        context = self._context.copy()
        for sale_wizard in self.sale_wizard_ids:

            _logger.debug(sale_wizard)

            if only_states and sale_wizard.state not in only_states:
                continue
            context['active_id'] = sale_wizard.id

            return {
                'name': action.name,
                'help': action.help,
                'type': action.type,
                'views': [
                    (wizard.id, 'form'),
                ],
                'target': 'new',
                'context': context,
                'res_model': action.res_model,
                'res_id': sale_wizard.id,
            }
        return False

    @api.model
    def action_next_wizard(self):
        action = self._get_next_sale_wizard(['new', 'start'])

        _logger.debug('Got action: %s', action)

        if action:
            return action
        else:
            self.state = 'done'
            return self.action_rx_sale_conversions()

    @api.multi
    def action_rx_sale_conversions(self):
        self.ensure_one()
        sale_obj = self.env['sale.order']
        sale_orders = None

        for sale_wizard in self.sale_wizard_ids:
            sale_vals = sale_wizard._to_vals()

            _logger.debug(sale_vals)

            sale_order = sale_obj.create(sale_vals)
            try:
                sale_orders += sale_order
            except TypeError:
                sale_orders = [sale_order]

        model_obj = self.env['ir.model.data']
        form = model_obj.xmlid_to_object('sale.view_order_form')
        tree = model_obj.xmlid_to_object('sale.view_quotation_tree')
        action = model_obj.xmlid_to_object('sale.action_quotations')
        context = self._context.copy()

        _logger.info('Created %s', sale_orders)
        _logger.debug('%s %s %s', form, tree, action)

        sale_order_ids = [s.id for s in sale_orders]
        return {
            'name': action.name,
            'help': action.help,
            'type': action.type,
            'view_mode': 'tree',
            'view_id': tree.id,
            'views': [
                (tree.id, 'tree'), (form.id, 'form'),
            ],
            'target': 'current',
            'context': context,
            'res_model': action.res_model,
            'res_ids': sale_order_ids,
            'domain': [('id', 'in', sale_order_ids)],
        }
