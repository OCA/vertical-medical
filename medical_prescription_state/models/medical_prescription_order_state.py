# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPrescriptionOrderState(models.Model):
    '''
    Add KanBan states to MedicalPrescriptionOrder

    This class adds KanBan state attributes to `medical.prescription.order`
    For the most part, it should operate similar to that of the Project
    KanBan.
    '''

    _name = 'medical.prescription.order.state'
    _description = 'Medical Prescription Order State'

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
        help='This stage is folded in the kanban view when'
        ' there are no records in that stage to display.',
    )
    color = fields.Integer(
        'Color Index',
        default=1,
        help='Color index to be used if the Rx does not have one defined',
    )
