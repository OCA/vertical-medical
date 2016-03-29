# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MedicalInsurancePlanWizard(models.TransientModel):
    _name = 'medical.insurance.plan.wizard'
    _description = 'Medical Insurance Plan Wizard'
    insurance_template_id = fields.Many2one(
        string='Plan Template',
        help='Insurance Plan Template',
        comodel_name='medical.insurance.template',
        required=True,
    )
    number = fields.Char(
        required=True,
        help='Identification number for insurance account',
    )
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='medical.patient',
        default=lambda s: s._compute_default_session(),
        required=True,
        readonly=True,
    )
    member_since = fields.Date(
        string='Member Since',
    )
    member_exp = fields.Date(
        string='Expiration Date',
    )

    @api.model
    def _compute_default_session(self):
        return self.env['medical.patient'].browse(
            self._context.get('active_id')
        )

    @api.multi
    def action_create_plan(self):
        self.ensure_one()
        plan_obj = self.env['medical.insurance.plan']
        plan_obj.create({
            'insurance_template_id': self.insurance_template_id.id,
            'number': self.number,
            'patient_id': self.patient_id.id,
            'member_since': self.member_since,
            'member_exp': self.member_exp,
        })
        return True
