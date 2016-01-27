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
