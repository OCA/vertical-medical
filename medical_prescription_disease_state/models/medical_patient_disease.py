# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class MedicalPatientDisease(models.Model):
    _inherit = 'medical.patient.disease'
    count_prescription_order_lines = fields.Integer(
        compute='_compute_prescription_order_lines',
        string='Prescription Order Lines',
    )
    last_prescription_order_line_id = fields.Many2one(
        comodel_name='medical.prescription.order.line',
        compute='_compute_prescription_order_lines',
        string='Last Prescription Order Line',
    )
    last_prescription_order_line_active = fields.Boolean(
        related='last_prescription_order_line_id.active',
    )

    @api.multi
    def _compute_prescription_order_lines(self, ):
        for rec_id in self:
            line_ids = rec_id.prescription_order_line_ids

            if line_ids:
                rec_id.count_prescription_order_lines = len(line_ids)

                sorted_line_ids = line_ids.sorted(
                    key=lambda r: r.date_start_treatment,
                    reverse=True,
                )
                last_line_id = sorted_line_ids[0]
                rec_id.last_prescription_order_line_id = last_line_id
