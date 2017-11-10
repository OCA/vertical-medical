

from odoo import fields, models


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    plan_definition_id = fields.Many2one(
        comodel_name='workflow.plan.definition'
    )   # FHIR Field: definition

    activity_definition_id = fields.Many2one(
        comodel_name='workflow.activity.definition',
    )   # FHIR Field: definition

    plan_definition_action_id = fields.Many2one(
        comodel_name='workflow.plan.definition.action',
    )   # FHIR Field: definition
