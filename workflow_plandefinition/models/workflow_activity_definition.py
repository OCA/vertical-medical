# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _


class ActivityDefinition(models.Model):
    """
    FHIR entity: Activity Definition
    Link: https://www.hl7.org/fhir/activitydefinition.html
    """
    _name = 'workflow.activity.definition'
    _description = 'Activity Definition'
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
        string='Workflow Type',
        comodel_name='workflow.type',
        help="Type of worklow this activity definition can be used in",
    )
    model_id = fields.Many2one(
        string='Model',
        comodel_name='ir.model',
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('retired', 'Retired'),
         ('unknown', 'Unknown')],
        required=True,
        default='draft',
    )   # FHIR field: status
    resource_product_id = fields.Many2one(
        string='Resource Product',
        comodel_name='product.product',
        help='Product that represents this resource',
        required=False,
    )   # FHIR field: product
    quantity = fields.Float(
        string='Quantity',
        help='How much to administer/supply/consume',
    )   # FHIR field: quantity
    action_ids = fields.One2many(
        string='Subsequent actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='activity_definition_id',
        readonly=True,
    )

    @api.constrains('type_id')
    def _check_type_id(self):
        for rec in self:
            if rec.action_ids:
                raise exceptions.UserError(
                    _('Type cannot be modified if the record has relations'))

    @api.onchange('type_id')
    def _onchange_type_id(self):
        self.model_id = False
        return {
            'domain': {
                'model_id': [('id', 'in', self.type_id.model_ids.ids)],
            },
        }
