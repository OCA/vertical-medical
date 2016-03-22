# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MedicalInsurancePlan(models.Model):
    _inherit = 'medical.insurance.plan'
    active = fields.Boolean(
        default=True
    )

    @api.model
    def create(self, vals):
        res = super(MedicalInsurancePlan, self).create(vals)
        res._save_pricelist_and_invalidate_plans()
        return res

    @api.multi
    def write(self, vals):
        res = super(MedicalInsurancePlan, self).write(vals)
        if 'active' not in vals:
            for rec_id in self:
                rec_id._save_pricelist_and_invalidate_plans()
        return res

    @api.multi
    def _save_pricelist_and_invalidate_plans(self):
        if self.patient_id:
            self.patient_id.write({'pricelist_id': self.pricelist_id.id})
            plan_ids = self.patient_id.insurance_plan_ids
            plan_ids.search([('id', '!=', self.id)]).action_invalidate()

    @api.multi
    def action_invalidate(self):
        for rec_id in self:
            rec_id.active = False
