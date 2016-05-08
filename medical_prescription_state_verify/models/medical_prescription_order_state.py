# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPrescriptionOrderState(models.Model):
    '''
    Add generic types to `medical.prescription.order` for validations

    This class provides generic types to `medical.prescription.order` so that
    validations and auditing can be applied based on status definitions.
    '''

    _inherit = 'medical.prescription.order.state'

    type = fields.Selection([
        ('normal', 'Normal'),
        ('verified', 'Verified'),
        ('exception', 'Exception'),
        ('cancel', 'Cancelled'),
    ],
        default='normal',
        translate=True,
        required=True,
        help='Type of state:\n'
        '* `Verified` will trigger `verified` hooks & lock record.\n'
        '* `Cancelled` indicates an Rx is cancelled and no manual action'
        ' is required.'
        '* `Exception` indicates an exception w/ the Rx, and is also'
        ' the only state that a `Verified` Rx can be moved to aside from'
        ' other `Verified` states.',
    )
