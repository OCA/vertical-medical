# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models
from collections import defaultdict


class MedicalLeadWizard(models.TransientModel):
    _name = 'medical.lead.wizard'
    _description = 'Medical Lead Wizard'

    prescription_line_ids = fields.Many2many(
        string='Prescription',
        comodel_name='medical.prescription.order.line',
        default=lambda s: s._compute_default_session(),
        required=True,
        readonly=True,
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        help='Pharmacy to dispense orders from',
        comodel_name='medical.pharmacy',
        required=True,
        default=lambda s: s._compute_default_pharmacy(),
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

    def _compute_default_session(self):
        return self.env['medical.prescription.order.line'].browse(
            self._context.get('active_ids')
        )

    def _compute_default_pharmacy(self):
        default_order_lines = self._compute_default_session()
        if len(default_order_lines):
            return default_order_lines[0].prescription_order_id.partner_id

    @api.multi
    def action_create_leads(self):
        order_map = defaultdict(list)

        for rx_line in self.prescription_line_ids:
            order_map[rx_line.patient_id].append(rx_line)

        lead_obj = self.env['crm.lead'].browse()
        lead_ids = lead_obj

        for patient_id, rx_orders in order_map.items():
            partner_id = patient_id.partner_id
            rx_order_lines = [(4, rx_order.id, 0) for rx_order in rx_orders]

            lead_ids += lead_obj.create({
                'partner_id': partner_id.id,
                'email_from': partner_id.email,
                'phone': partner_id.phone,
                'pharmacy_id': self.pharmacy_id.id,
                'prescription_order_line_ids': rx_order_lines,
                'is_prescription': True,
                'name': ', '.join(rx_order.name for rx_order in rx_orders),
            })

        model_obj = self.env['ir.model.data']
        form_id = model_obj.xmlid_to_object('crm.crm_case_form_view_oppor')
        tree_id = model_obj.xmlid_to_object('crm.crm_case_tree_view_oppor')
        action_id = model_obj.xmlid_to_object('crm.crm_lead_action_activities')
        context = self._context.copy()

        lead_ids = [lead.id for lead in lead_ids]
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
            'res_ids': lead_ids,
            'domain': [('id', 'in', lead_ids)],
        }
