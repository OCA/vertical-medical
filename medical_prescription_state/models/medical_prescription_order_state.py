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


class MedicalPrescriptionOrderState(models.Model):
    '''
    Add KanBan states to MedicalPrescriptionOrder
    
    This class adds KanBan state attributes to `medical.prescription.order`
    For the most part, it should operate similar to that of the Project
    KanBan.
    '''

    _name = 'medical.prescription.order.state'
    _description = 'Prescription Order States'

    name = fields.Char(
        'State Name',
        translate=True,
        required=True,
        help='Displayed as the header for this state in KanBan views.',
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
        default=False,
        help='This stage is folded in the kanban view when'
        ' there are no records in that stage to display.',
    )
    color = fields.Integer(
        'Color Index',
        default=1,
        help='Color index to be used if the Rx does not have one defined',
    )
