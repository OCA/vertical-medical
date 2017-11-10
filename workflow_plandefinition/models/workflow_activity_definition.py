# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools import pycompat


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
        required=True
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

    def _get_medical_values(self, vals, parent=False, plan=False, action=False
                            ):
        if not vals.get('patient_id', False):
            raise ValidationError(_('Patient is not defined'))
        values = {
            'service_id': self.service_id.id,
            'plan_definition_id': plan.id or action.plan_definition_id.id,
            'plan_definition_action_id': action and action.id,
            'activity_definition_id': self.id,
        }
        if parent and parent._name == 'medical.request.group':
            values['request_group_id'] = parent.id
        return values

    def _get_activity_values(self, vals, parent=False, plan=False, action=False
                             ):
        values = vals.copy()
        model_obj = self.env[self.model_id.model]
        parents = model_obj._inherit
        parents = [parents] if isinstance(
            parents, pycompat.string_types) else (parents or [])
        if 'medical.request' in parents:
            values.update(self._get_medical_values(vals, parent, plan, action))
            values['internal_identifier'] = model_obj._get_internal_identifier(
                values)
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
