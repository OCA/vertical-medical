# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields, _
from collections import defaultdict
import logging


_logger = logging.getLogger(__name__)


class MedicalLeadWizard(models.TransientModel):
    _name = 'medical.lead.wizard'
    _description = 'Medical Lead Wizard'

    def _compute_default_session(self, ):
        return self.env['medical.prescription.order.line'].browse(
            self._context.get('active_ids')
        )

    prescription_line_ids = fields.Many2many(
        string='Prescription',
        comodel_name='medical.prescription.order.line',
        default=lambda s: s._compute_default_session(),
        required=True,
        readonly=True,
    )
    pharmacy_id = fields.Many2one(
        string='Pharmacy',
        help=_('Pharmacy to dispense orders from'),
        comodel_name='medical.pharmacy',
        required=True,
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

    @api.multi
    def action_create_leads(self, ):

        order_map = defaultdict(list)
        for rx_line in self.prescription_line_ids:
            if self.split_orders == 'partner':
                raise NotImplementedError(_(
                    'Patient and Customers are currently identical concepts.'
                ))
            elif self.split_orders == 'patient':
                order_map[rx_line.patient_id].append(rx_line)
            else:
                order_map[None].append(rx_line)

        lead_obj = self.env['crm.lead']
        lead_ids = lead_obj
        for patient_id, order in order_map.items():

            partner_id = patient_id.partner_id
            order_lines = [(4, l.id, 0) for l in order]
            lead_ids += lead_obj.create({
                'partner_id': partner_id.id,
                'email_from': partner_id.email,
                'phone': partner_id.phone,
                'pharmacy_id': self.pharmacy_id.id,
                'prescription_order_line_ids': order_lines,
                'is_prescription': True,
                'name': ', '.join(l.name for l in order)
            })

        _logger.debug('Created %s', lead_ids)

        model_obj = self.env['ir.model.data']
        form_id = model_obj.xmlid_to_object('crm.crm_case_form_view_oppor')
        tree_id = model_obj.xmlid_to_object('crm.crm_case_tree_view_oppor')
        action_id = model_obj.xmlid_to_object('crm.crm_lead_action_activities')
        context = self._context.copy()
        _logger.debug('%s %s %s', form_id, tree_id, action_id)
        lead_ids = [l.id for l in lead_ids]

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
