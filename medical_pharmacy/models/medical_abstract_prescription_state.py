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


class MedicalAbstractPrescriptionState(models.AbstractModel):
    _name = 'medical.abstract.prescription.state'
    _description = 'Prescription Order Abstract States'
    _order = 'sequence'
    name = fields.Char(
        'State Name',
        required=True,
    )
    description = fields.Text(
        'Description',
    )
    sequence = fields.Integer(
        'Sequence',
        default=1,
    )
    legend_priority = fields.Char(
        'Priority Management Explanation',
        help='Explanation text to help users using the star and priority'
        ' mechanism on stages or RXs that are in this stage.',
    )
    legend_blocked = fields.Char(
        'Kanban Blocked Explanation',
        help='Override the default value displayed for the blocked state for'
        ' kanban selection, when the RX is in that stage.',
    )
    legend_done = fields.Char(
        'Kanban Valid Explanation',
        help='Override the default value displayed for the done state for'
        ' kanban selection, when the RX is in that stage.',
    )
    legend_normal = fields.Char(
        'Kanban Ongoing Explanation',
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
        help='Color index to be used if the Rx does not have one defined'
    )
