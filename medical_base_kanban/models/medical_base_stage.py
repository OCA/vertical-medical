# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalBaseStage(models.Model):
    """ It provides base stages for Medical KanBan resources.

    This class provides Kanban stage attributes for use in Medical modules.
    For the most part, it should operate similar to that of the Project
    Kanban.
    """

    _name = 'medical.base.stage'
    _description = 'Medical Base Stages'
    _order = 'res_model, sequence'

    name = fields.Char(
        'State name',
        translate=True,
        required=True,
        help='Displayed as the header for this state in Kanban views.',
    )
    description = fields.Text(
        'Description',
        translate=True,
        help='Short description of state\'s meaning/purpose.',
    )
    sequence = fields.Integer(
        'Sequence',
        default=1,
        required=True,
        index=True,
        help='Order of state in relation to others.',
    )
    legend_priority = fields.Char(
        'Priority Management Explanation',
        translate=True,
        default='Star an item when it needs to be escalated ahead of other'
        '  items due to special circumstances.',
        help='Explanation text to help users using the star and priority'
        ' mechanism on stages or RXs that are in this stage.',
    )
    legend_blocked = fields.Char(
        'Kanban Blocked Explanation',
        translate=True,
        default='Block an item if it requires handling by a specialist, such'
        ' as a pharmacist.',
        help='Override the default value displayed for the blocked state for'
        ' kanban selection, when the RX is in that stage.',
    )
    legend_done = fields.Char(
        'Kanban Valid Explanation',
        translate=True,
        default='Item has been fully processed in this stage.',
        help='Override the default value displayed for the done state for'
        ' kanban selection, when the RX is in that stage.',
    )
    legend_normal = fields.Char(
        'Kanban Ongoing Explanation',
        translate=True,
        default='This is the default situation, and indicates that a record'
        ' can be processed by any user working this queue.',
        help='Override the default value displayed for the normal state for'
        ' kanban selection, when the RX is in that stage.',
    )
    fold = fields.Boolean(
        'Folded in RX Pipeline',
        help='This stage is folded in the kanban view when'
        ' there are no records in that stage to display.',
    )
    color = fields.Integer(
        'Color Index',
        default=1,
        help='Color index to be used if the Rx does not have one defined',
    )
    res_model = fields.Char(
        required=True,
        index=True,
        default=lambda s: s._default_res_model(),
    )
    state = fields.Selection(
        lambda s: s._get_state_select(),
    )

    @api.model
    def _default_res_model(self):
        return self.env.context['params'].get('model', '')

    @api.model
    def _get_state_select(self):
        return [
            ('draft', 'New'),
            ('open', 'In Progress'),
            ('pending', 'Pending'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ]
