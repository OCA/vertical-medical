# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class WorkflowType(models.Model):
    """
    FHIR entity: Workflow (Workflow definition)
    link: https://www.hl7.org/fhir/workflow.html
    """
    _name = 'workflow.type'
    _description = 'Plan Definition Type'

    name = fields.Char(
        string='Name',
        help='Human-friendly name for the Plan Definition',
        required=True,
    )
    description = fields.Text(
        string='Description',
        help='Summary of nature of plan',
    )
    model_id = fields.Many2one(
        string='Model to be created',
        comodel_name='ir.model',
    )
    model_ids = fields.Many2many(
        string='Models',
        comodel_name='ir.model',
    )
