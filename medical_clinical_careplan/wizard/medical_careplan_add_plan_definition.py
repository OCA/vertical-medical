# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalCareplanAddPlanDefinition(models.TransientModel):
    _name = 'medical.careplan.add.plan.definition'
    _inherit = 'medical.add.plan.definition'

    def _domain_plan_definition(self):
        return [
            ('type_id', '=', self.env.ref(
                'medical_workflow.medical_workflow').id)
        ]

    patient_id = fields.Many2one(
        comodel_name='medical.patient',
        string='Patient',
        related='careplan_id.patient_id',
    )

    careplan_id = fields.Many2one(
        comodel_name='medical.careplan',
        string='Care plan',
        required=True,
    )

    plan_definition_id = fields.Many2one(
        comodel_name='workflow.plan.definition',
        domain=_domain_plan_definition,
        required=True,
    )

    def _get_values(self):
        values = super(MedicalCareplanAddPlanDefinition, self)._get_values()
        values['careplan_id'] = self.careplan_id.id
        return values
