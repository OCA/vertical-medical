# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import ValidationError


class PlanDefinitionAction(models.Model):
    # FHIR entity: Action
    _name = 'workflow.plan.definition.action'
    _description = 'Medical Plan Definition Action'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _parent_name = 'parent_id'
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'
    _rec_name = 'complete_name'

    name = fields.Char(
        string='Action name',
        required=True,
    )   # FHIR field: title
    complete_name = fields.Char(
        "Full Action Name",
        compute='_compute_complete_name',
        store=True,
    )
    parent_id = fields.Many2one(
        string='Parent Action',
        comodel_name='workflow.plan.definition.action',
        ondelete='cascade',
        domain="[('plan_definition_id', '=', plan_definition_id)]",
    )
    child_ids = fields.One2many(
        string='Child Actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='parent_id',
        required=True,
    )   # FHIR field: Action (sub-action)
    direct_plan_definition_id = fields.Many2one(
        string='Root plan definition',
        comodel_name='workflow.plan.definition',
        ondelete='cascade',
    )
    type_id = fields.Many2one(
        'workflow.type',
        related='plan_definition_id.type_id',
    )
    plan_definition_id = fields.Many2one(
        string='Plan definition',
        comodel_name='workflow.plan.definition',
        compute='_compute_plan_definition_id',
        ondelete='cascade',
        store=True
    )
    execute_plan_definition_id = fields.Many2one(
        string='Plan definition',
        comodel_name='workflow.plan.definition',
        help='This plan will be executed instead of an activity',
    )
    activity_definition_id = fields.Many2one(
        string='Activity definition',
        comodel_name='workflow.activity.definition',
    )   # FHIR field: definition (Activity Definition)
    parent_left = fields.Integer(
        'Left Parent',
        index=True,
    )
    parent_right = fields.Integer(
        'Right Parent',
        index=True,
    )

    @api.depends('name', 'parent_id')
    def _compute_complete_name(self):
        """ Forms complete name of action from parent to child action. """
        for rec in self:
            name = rec.name
            current = rec
            while current.parent_id:
                current = current.parent_id
                name = '%s/%s' % (current.name, name)
            rec.complete_name = name

    @api.multi
    @api.depends('parent_id', 'direct_plan_definition_id')
    def _compute_plan_definition_id(self):
        for rec in self:
            rec.plan_definition_id = rec.direct_plan_definition_id
            if rec.parent_id:
                rec.plan_definition_id = rec.parent_id.plan_definition_id

    @api.onchange('plan_definition_id')
    def _onchange_activity_definition_id(self):
        return {
            'domain': {
                'activity_definition_id':
                    [('type_id', 'in', [self.plan_definition_id.type_id.id,
                                        False])],
            },
        }

    @api.onchange('activity_definition_id')
    def _onchange_activity_definition_id(self):
        self.name = self.activity_definition_id.name
        self.execute_plan_definition_id = False

    @api.onchange('execute_plan_definition_id')
    def _onchange_execute_plan_definition_id(self):
        self.name = self.execute_plan_definition_id.name
        self.activity_definition_id = False

    @api.multi
    @api.constrains('parent_id')
    def _check_recursion_parent_id(self):
        if not self._check_recursion():
            raise exceptions.ValidationError(
                _('Error! You are attempting to create a recursive category.'))

    @api.multi
    @api.constrains('execute_plan_definition_id', 'child_ids')
    def _check_execute_plan_definition_id(self):
        for record in self:
            if record.execute_plan_definition_id:
                plan_ids = [record.plan_definition_id.id]
                self.execute_plan_definition_id._check_plan_recursion(plan_ids)
                if record.child_ids:
                    raise ValidationError(_(
                        'Actions with Plans cannot have child actions'))

    @api.multi
    @api.constrains('execute_plan_definition_id', 'activity_definition_id')
    def _check_execute_plan_activity_definition(self):
        for record in self:
            if (
                not record.execute_plan_definition_id and
                not record.activity_definition_id
            ):
                raise ValidationError(_(
                    'Activity definition or plan definition must be defined '
                    'on each action'))

    @api.multi
    def execute_action(self, vals, parent=False):
        self.ensure_one()
        if self.execute_plan_definition_id:
            return self.execute_plan_definition_id.execute_plan_definition(
                vals, parent)
        res = self.activity_definition_id.execute_activity(
            vals, parent, self.plan_definition_id, self
        )
        for action in self.child_ids:
            action.execute_action(vals, parent=res)
        return True
