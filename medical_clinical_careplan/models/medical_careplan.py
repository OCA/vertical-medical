# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalCarePlan(models.Model):
    # FHIR Entity: Care Plan
    # (https://www.hl7.org/fhir/careplan.html)
    _name = 'medical.careplan'
    _description = 'Medical Care Plan'
    _inherit = 'medical.request'

    start_date = fields.Datetime(
        string='start date',
    )   # FHIR Field: Period
    end_date = fields.Datetime(
        string='End date',
    )   # FHIR Field: Period
    careplan_ids = fields.One2many(
        inverse_name='careplan_id',
    )

    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code('medical.careplan') or '/'

    def draft2active(self):
        for record in self:
            record.start_date = fields.Datetime.now()
        return super(MedicalCarePlan, self).draft2active()

    def active2completed(self):
        for record in self:
            record.end_date = fields.Datetime.now()
        return super(MedicalCarePlan, self).active2completed()

    def _get_parent_field_name(self):
        return 'careplan_id'

    def action_view_request_parameters(self):
        return {
            'view': 'medical_clinical_careplan.medical_careplan_action',
            'view_form': 'medical.careplan.view.form', }
