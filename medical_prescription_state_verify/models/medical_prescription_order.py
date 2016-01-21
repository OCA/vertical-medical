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

from openerp import fields, models, exceptions, _


class MedicalPrescriptionOrder(models.Model):
    '''
    Add State verification functionality to MedicalPrescriptionOrder

    This model will allow you to plug in verification methods to Rx Orders,
    allowing for custom business logic in regards to workflows and auditing.

    Attributes:
        _ALLOWED_CHANGE_KEYS: `list` of keys that are allowed to be changed
            on an RX after it has been verified (without moving to a stage
            that has been defined in `_ALLOWED_CHANGE_STATES`)
        _ALLOWED_CHANGE_STATES: `list` of keys defining status types in which
            an RX can be moved to after being verified
    '''

    _inherit = 'medical.prescription.order'
    _ALLOWED_CHANGE_KEYS = ['state_id', ]
    _ALLOWED_CHANGE_STATES = ['verified', 'cancel', 'exception', ]

    state_type = fields.Char(
        related='state_id.type'
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
                
                # Only allow changes for keys in self._ALLOWED_CHANGE_KEYS
                keys = vals.keys()
                for allowed_key in self._ALLOWED_CHANGE_KEYS:
                    try:
                        del keys[keys.index(allowed_key)]
                    except ValueError:
                        pass
                if len(keys) > 1:
                    raise exceptions.ValidationError(_(
                        'You cannot edit this value after an Rx has been'
                        ' verified. Please either cancel it, or mark it as an'
                        ' exception if manual reversals are required. [%s]' %
                        rec_id.name
                    ))

                # Only allow state changes from self._ALLOWED_CHANGE_STATES
                if vals.get('state_id'):
                    state_id = self.env['%s.state' % self._name].browse(
                        vals['state_id']
                    )
                    if state_id.type not in self._ALLOWED_CHANGE_STATES:
                        raise exceptions.ValidationError(_(
                            'You cannot move an Rx into this state after it'
                            ' has been verified. [%s]' % rec_id.name
                        ))

            return super(MedicalPrescriptionOrder, self).write(vals)
