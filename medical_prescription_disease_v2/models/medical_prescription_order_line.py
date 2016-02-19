# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'
    state = fields.Selection(
        [
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        ],
        default='active',
        compute='_compute_state',
    )
    is_treatment_stopped = fields.Boolean(
        compute='_compute_is_treatment_stopped'
    )

    @api.multi
    def _compute_state(self, ):
        for rec_id in self:
            if rec_id.is_course_complete or rec_id.is_treatment_stopped:
                rec_id.state = 'inactive'
            else:
                rec_id.state = 'active'

    @api.multi
    def _compute_is_treatment_stopped(self, ):
        for rec_id in self:
            if not rec_id.date_stop_treatment:
                rec_id.is_treatment_stopped = False
            else:
                stop_date = fields.Datetime.from_string(
                    rec_id.date_stop_treatment
                )
                today = fields.Datetime.from_string(fields.Datetime.now())
                days = (today - stop_date).days
                rec_id.is_treatment_stopped = (days > 0)
