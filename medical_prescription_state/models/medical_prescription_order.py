# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPrescriptionOrder(models.Model):
    '''
    Add Kanban functionality to MedicalPrescriptionOrder
    '''

    _inherit = 'medical.prescription.order'
    _order = 'priority desc, sequence, date_prescription, name'

    sequence = fields.Integer(
        default=10,
        help="Sequence order when displaying a list of Rxs",
    )
    priority = fields.Selection([
        (0, 'Normal'),
        (5, 'Medium'),
        (10, 'High'),
    ],
        select=True,
        default=0,
        help="Priority of the order",
    )
    stage_id = fields.Many2one(
        'medical.prescription.order.state',
        'State',
        track_visibility='onchange',
        select=True,
        copy=False,
        help="The state in Kanban view",
    )
    user_id = fields.Many2one(
        'res.users',
        'Assigned To',
        select=True,
        track_visibility='onchange',
        help="The order is assigned to",
    )
    date_assign = fields.Datetime(
        'Assigned Date',
        help="Date and time when order is assigned",
    )
    color = fields.Integer(
        'Color Index',
        help="Color of the Kanban card",
    )
    legend_blocked = fields.Char(
        string='Kanban Blocked Explanation',
        related='stage_id.legend_blocked',
        help="Kanban blocked explanation",
    )
    legend_done = fields.Char(
        string='Kanban Done Explanation',
        related='stage_id.legend_done',
        help="Kanban done explanation",
    )
    legend_normal = fields.Char(
        string='Kanban Ongoing Explanation',
        related='stage_id.legend_normal',
        help="Kanban ongoing explanation",
    )
    kanban_state = fields.Selection([
        ('normal', 'Normal Handling'),
        ('done', 'Ready'),
        ('blocked', 'Pharmacist Handling'),
    ],
        'Kanban State',
        default='normal',
        track_visibility='onchange',
        required=True,
        copy=False,
        help="An Rx's Kanban state indicates special situations affecting"
        " it:\n"
        "* `Normal Handling` is the default situation, and indicates no "
        " special handling."
        "* `Pharmacist Handling` indicates that this Rx must be processed"
        " by a pharmacist. \n"
        "* `Ready` indicates the Rx is ready to be pulled to the next stage.",
    )
