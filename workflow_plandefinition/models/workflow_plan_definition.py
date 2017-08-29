# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, api, exceptions


class PlanDefinition(models.Model):
    _name = 'workflow.plan.definition'
    _description = 'Plan Definition'
    _inherit = 'mail.thread'

    name = fields.Char(
        string='Name',
        help='Human-friendly name for the Plan Definition',
        required=True,
    )
    description = fields.Text(
        string='Description',
        help='Summary of nature of plan',
    )
    type_id = fields.Many2one(
        string='Workflow type',
        comodel_name='workflow.type',
        required=True,
    )
    model_id = fields.Many2one(
        string='Plan definition model',
        comodel_name='ir.model',
        related='type_id.model_id',
        readonly=True,
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('active', 'Active'),
         ('retired', 'Retired'),
         ('unknown', 'Unknown')],
        required=True,
        default='draft',
    )
    direct_action_ids = fields.One2many(
        string='Parent actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='direct_plan_definition_id',
    )
    action_ids = fields.One2many(
        string='All actions',
        comodel_name='workflow.plan.definition.action',
        inverse_name='plan_definition_id',
        readonly=True,
    )

