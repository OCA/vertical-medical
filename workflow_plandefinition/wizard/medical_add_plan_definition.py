# Copyright 2017 Creu Blanca
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalAddPlanDefinition(models.TransientModel):
    _name = 'medical.add.plan.definition'

    def _domain_plan_definition(self):
        return [
            ('type_id', '=', self.env.ref(
                'workflow_plandefinition.medical_workflow').id)
        ]
    #

    patient_id = fields.Many2one(
        comodel_name='medical.patient',
        string='Patient',
        required=True
    )

    plan_definition_id = fields.Many2one(
        comodel_name='workflow.plan.definition',
        domain=_domain_plan_definition,
        required=True
    )

    def _get_values(self):
        return {
            'patient_id': self.patient_id.id,
            'name': self.plan_definition_id.name,
        }

    @api.multi
    def run(self):
        self.ensure_one()
        vals = self._get_values()
        self.plan_definition_id.execute_plan_definition(vals)
