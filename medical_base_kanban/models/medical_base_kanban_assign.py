# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalBaseKanbanAssign(models.Model):
    """ It provides KanBan assignment history for Medical """

    _name = 'medical.base.kanban.assign'
    _description = 'Medical Base State Assignments'
    _order = 'date_assign desc'

    stage_id = fields.Many2one(
        string='State',
        comodel_name='medical.base.stage',
        required=True,
    )
    user_id = fields.Many2one(
        string='Assigned User',
        comodel_name='res.users',
        required=True,
    )
    date_assign = fields.Datetime(
        string='Assigned Date',
        required=True,
    )
    kanban_id = fields.Many2one(
        string='Related Record',
        comodel_name='medical.base.kanban',
        required=True,
        index=True,
    )
