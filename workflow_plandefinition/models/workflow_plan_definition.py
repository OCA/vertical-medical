# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class PlanDefinition(models.Model):
    """
    FHIR entity: Plan Definition
    link: https://www.hl7.org/fhir/plandefinition.html
    """
    _name = 'workflow.plan.definition'
    _description = 'Plan Definition'
    _inherit = 'mail.thread'

    name = fields.Char(
        string='Name',
        help='Human-friendly name for the Plan Definition',
        required=True,
    )   # FHIR field: name
    description = fields.Text(
        string='Description',
        help='Summary of nature of plan',
    )   # FHIR field: description
    type_id = fields.Many2one(
        string='Workflow type',
        comodel_name='workflow.type',
        required=True,
    )   # FHIR field: type
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('retired', 'Retired'),
         ('unknown', 'Unknown')],
        required=True,
        default='draft',
    )   # FHIR field: status
    direct_action_ids = fields.One2many(
        string='Parent actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='direct_plan_definition_id',
    )   # FHIR field: action
    activity_definition_id = fields.Many2one(
        string='Activity definition',
        comodel_name='workflow.activity.definition',
        description='Main action'
    )   # FHIR field: action (if a parent action is created)
    action_ids = fields.One2many(
        string='All actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='plan_definition_id',
        readonly=True,
    )

    @api.multi
    def execute_plan_definition(self, vals):
        self.ensure_one()
        parent = False
        if (
            self.env.user._has_group('workflow_plandefinition.'
                                     'group_main_activity_plan_definition') and
            self.activity_definition_id
        ):
            parent = self.activity_definition_id.execute_activity(
                vals, plan=self)
        for action in self.direct_action_ids:
            action.execute_action(vals, parent)
        return parent
