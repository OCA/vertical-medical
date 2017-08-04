# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, api, exceptions


class PlanDefinitionAction(models.Model):
    _name = 'workflow.plan.definition.action'
    _description = 'Medical Plan Definition Action'
    _inherit = 'mail.thread'
    _parent_name = 'parent_id'
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'
    _rec_name = 'complete_name'
    _order = 'id asc'

    @api.one
    @api.depends('name', 'parent_id')
    def _compute_complete_name(self):
        """ Forms complete name of action from parent to child action. """
        name = self.name
        current = self
        while current.parent_id:
            current = current.parent_id
            name = '%s/%s' % (current.name, name)
        self.complete_name = name

    @api.multi
    @api.depends('parent_id', 'direct_plan_definition_id')
    def _compute_plan_definition_id(self):
        for rec in self:
            rec.plan_definition_id = rec.direct_plan_definition_id
            if rec.parent_id:
                rec.plan_definition_id = rec.parent_id.plan_definition_id

    name = fields.Char(
        string='Action name',
        required=True,
    )
    complete_name = fields.Char(
        "Full Action Name",
        compute='_compute_complete_name',
        store=True,
    )
    parent_id = fields.Many2one(
        string='Parent Action',
        comodel_name='workflow.plan.definition.action',
        ondelete='cascade',
    )
    child_ids = fields.One2many(
        string='Child Actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='parent_id',
        required=True,
    )
    direct_plan_definition_id = fields.Many2one(
        string='Root plan definition',
        comodel_name='workflow.plan.definition',
        ondelete='cascade',
    )
    plan_definition_id = fields.Many2one(
        string='Plan definition',
        comodel_name='workflow.plan.definition',
        compute='_compute_plan_definition_id',
        ondelete='cascade',
    )
    activity_definition_id = fields.Many2one(
        string='Activity definition',
        comodel_name='workflow.activity.definition',
    )
    parent_left = fields.Integer(
        'Left Parent',
        index=True,
    )
    parent_right = fields.Integer(
        'Right Parent',
        index=True,
    )

    @api.onchange('plan_definition_id')
    def _domain_activity_definition_id(self):
        return {
            'domain': {
                'activity_definition_id':
                    [('type_id', 'in', [self.plan_definition_id.type_id.id, False])]}}

    @api.onchange('activity_definition_id')
    def _onchange_activity_definition_id(self):
        self.name = self.activity_definition_id.name
