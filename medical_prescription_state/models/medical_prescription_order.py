# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models


class MedicalPrescriptionOrder(models.Model):
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
    )
    state_id = fields.Many2one(
        'medical.prescription.order.state',
        'State',
        track_visibility='onchange',
        select=True,
        copy=False,
    )
    user_id = fields.Many2one(
        'res.users',
        'Assigned To',
        select=True,
        track_visibility='onchange',
    )
    date_assign = fields.Datetime(
        'Assigned Date'
    )
    legend_blocked = fields.Char(
        string='Kanban Blocked Explanation',
        related='state_id.legend_blocked'
    )
    legend_done = fields.Char(
        string='Kanban Valid Explanation',
        related='state_id.legend_done'
    )
    legend_normal = fields.Char(
        string='Kanban Ongoing Explanation',
        related='state_id.legend_normal'
    )
    color = fields.Integer(
        'Color Index',
    )
    kanban_state = fields.Selection([
        ('normal', 'In Progress'),
        ('done', 'Ready for next stage'),
        ('blocked', 'Blocked')
    ],
        'Kanban State',
        default='normal',
        track_visibility='onchange',
        required=True,
        copy=False,
        help="An Rx's kanban state indicates special situations affecting it:"
        "\n * Normal is the default situation"
        "\n * Blocked indicates something is preventing the progress of this"
        " Rx"
        "\n * Ready for next stage indicates the Rx is ready to be pulled to"
        " the next stage",
    )
