# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalBaseKanban(models.AbstractModel):
    """ It provides abstract KanBan state mechanism for poly inherits.

    All public properties are preceded with kanban_ in order to isolate
    from child models.

    There is one exception to the kanban_ prefix rule - ``stage_id``.
    This is a required field in the KanBan widget and must be defined as such.
    """

    _name = 'medical.base.kanban'
    _desciption = 'Medical Base KanBan'
    _order = 'kanban_priority desc, kanban_sequence, kanban_date_assign'

    kanban_sequence = fields.Integer(
        default=10,
        index=True,
        help="Sequence order when displaying a list of Rxs",
    )
    kanban_priority = fields.Selection([
        ('0', 'Normal'),
        ('5', 'Medium'),
        ('10', 'High'),
    ],
        index=True,
        default='0',
        help="Priority of the order",
    )
    stage_id = fields.Many2one(
        string='State',
        comodel_name='medical.base.stage',
        track_visibility='onchange',
        index=True,
        copy=False,
        help="The state in Kanban view",
        # default="_default_stage_id",
        domain=lambda s: [('res_model', '=', s._name)],
    )
    kanban_user_id = fields.Many2one(
        string='Assigned To',
        comodel_name='res.users',
        index=True,
        track_visibility='onchange',
        help="The record is assigned to",
    )
    kanban_assign_history_ids = fields.One2many(
        string='Assign History',
        comodel_name='medical.base.kanban.assign',
        inverse_name='kanban_id',
        ondelete='cascade',
    )
    kanban_date_assign = fields.Datetime(
        string='Assigned Date',
        compute='_compute_kanban_date_assign',
        store=True,
        help="Date and time when record is assigned",
    )
    kanban_color = fields.Integer(
        'Color Index',
        help="Color of the Kanban card",
    )
    kanban_legend_blocked = fields.Char(
        string='Kanban Blocked Explanation',
        related='stage_id.legend_blocked',
        help="Kanban blocked explanation",
    )
    kanban_legend_done = fields.Char(
        string='Kanban Done Explanation',
        related='stage_id.legend_done',
        help="Kanban done explanation",
    )
    kanban_legend_normal = fields.Char(
        string='Kanban Ongoing Explanation',
        related='stage_id.legend_normal',
        help="Kanban ongoing explanation",
    )
    kanban_state = fields.Selection([
        ('normal', 'Normal Handling'),
        ('done', 'Ready'),
        ('blocked', 'Special Handling'),
    ],
        'Kanban State',
        default='normal',
        track_visibility='onchange',
        required=True,
        copy=False,
        help="A Record's Kanban state indicates special situations affecting"
        " it:\n"
        "* `Normal Handling` is the default situation, and indicates no"
        " special handling."
        "* `Special Handling` indicates that this Record must be processed"
        " in a special way, or by a particular agent. \n"
        "* `Ready` indicates the Record is ready to be pulled to the next"
        " stage.",
    )
    kanban_canonical_state = fields.Selection(
        related='stage_id.state',
    )

    _group_by_full = {
        'stage_id': lambda s, *a, **k: s._read_group_stage_ids(*a, **k),
    }

    @api.model
    def _default_stage_id(self, model_name):
        return

    @api.multi
    def _read_group_stage_ids(
        self, domain, read_group_order=None, access_rights_uid=None,
    ):
        stage_obj = self.env['medical.base.stage'].sudo(access_rights_uid)
        domain = [('res_model', '=', self._name)]
        stages = stage_obj.search(domain)
        result = [(r.id, r.display_name) for r in stages]
        fold = {r.id: r.fold for r in stages}
        return result, fold

    @api.multi
    @api.depends('kanban_user_id', 'stage_id')
    def _compute_kanban_date_assign(self):
        """ It sets new assign date and adds into assignment history """
        for rec_id in self:
            if not rec_id.kanban_user_id or not rec_id.stage_id:
                return
            history_ids = rec_id.kanban_assign_history_ids
            if (
                not history_ids or
                rec_id.kanban_user_id != history_ids[0].user_id
            ):
                date = fields.Datetime.now()
                rec_id.kanban_date_assign = date
                rec_id.kanban_assign_history_ids = [
                    (0, 0, {
                        'user_id': rec_id.kanban_user_id.id,
                        'stage_id': rec_id.stage_id.id,
                        'date_assign': date,
                    }),
                ]
