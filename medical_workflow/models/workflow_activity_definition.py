# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import ValidationError


class ActivityDefinition(models.Model):
    # FHIR entity: Activity Definition
    # (https://www.hl7.org/fhir/activitydefinition.html)
    _name = 'workflow.activity.definition'
    _description = 'Activity Definition'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'medical.abstract']

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
        required=True,
    )   # FHIR field: kind
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('retired', 'Retired'),
         ('unknown', 'Unknown')],
        required=True,
        default='draft',
    )   # FHIR field: status
    service_id = fields.Many2one(
        string='Resource Product',
        comodel_name='product.product',
        help='Product that represents this resource',
        required=False,
    )   # FHIR field: code
    quantity = fields.Integer(
        string='Quantity',
        help='How much to realize',
        default=1,
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

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'workflow.activity.definition') or '/'

    def _get_medical_values(self, vals, parent=False, plan=False, action=False
                            ):
        if not vals.get('patient_id', False):
            raise ValidationError(_('Patient is not defined'))
        values = {
            'service_id': self.service_id.id,
            'plan_definition_id': plan and plan.id or
            action and action.plan_definition_id.id or False,
            'plan_definition_action_id': action and action.id or False,
            'activity_definition_id': self.id,
        }
        return values

    def _get_activity_values(self, vals, parent=False, plan=False, action=False
                             ):
        values = vals.copy()
        if self.type_id == self.env.ref('medical_workflow.medical_workflow'):
            values.update(self._get_medical_values(vals, parent, plan, action))
        return values

    @api.multi
    def execute_activity(self, vals, parent=False, plan=False, action=False):
        self.ensure_one()
        values = self._get_activity_values(vals, parent, plan, action)
        model_obj = self.env[self.model_id.model]
        ids = []
        for i in range(0, self.quantity):
            ids.append(model_obj.create(values).id)
        return model_obj.browse(ids)
