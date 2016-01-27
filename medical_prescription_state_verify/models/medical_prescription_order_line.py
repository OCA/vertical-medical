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

from openerp import models, exceptions, api, _


class MedicalPrescriptionOrderLine(models.Model):
    '''
    Add State verification functionality to MedicalPrescriptionOrderLine

    This model disallows editing of a `medical.prescription.order.line` if its
    `prescription_order_id` is in a `verified` state.
    '''

    _inherit = 'medical.prescription.order.line'
    state_type = fields.Char(
        related='prescription_order_id.state_type'
    )

    @api.multi
    def write(self, vals, ):
        '''
        Overload write & perform audit validations
        
        Raises:
            ValidationError: When a write is not allowed due to being in a
                protected state
        '''
        for rec_id in self:
            if rec_id.state_type == 'verified':
                raise exceptions.ValidationError(_(
                    'You cannot edit this value after its parent Rx has'
                    ' been verified. Please either cancel it, or mark it as'
                    ' an exception if manual reversals are required. [%s]' %
                    rec_id.name
                ))

            return super(MedicalPrescriptionOrderLine, self).write(vals)
