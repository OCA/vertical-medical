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
from openerp.exceptions import ValidationError


class MedicalHistoryType(models.Model):
    _name = 'medical.history.type'
    _description = 'Medical History Types'

    name = fields.Char(
        help='Humanized name of entry type',
        required=True,
    )
    code = fields.Char(
        help='Entry type code designation',
    )
    display_name = fields.Char(
        compute='_compute_display_name',
        help='Compiled name to display in reports',
    )
    prefix = fields.Char(
        default='----  ',
        help='Prefix to add to the entry name in notations',
    )
    suffix = fields.Char(
        default='  ----',
        help='Suffix to add to the entry name in notations',
    )
    old_cols_to_save = fields.Selection([
        ('none', 'None'),
        ('changed', 'Changed'),
        ('all', 'All'),
    ],
        help='Old columns to save in the history record',
        default='changed',
    )
    new_cols_to_save = fields.Selection([
        ('none', 'None'),
        ('changed', 'Changed'),
    ],
        help='New columns to save in the history record',
        default='none',
    )

    @api.multi
    def _compute_display_name(self, ):
        ''' Compute name for representation to user '''
        for rec_id in self:
            rec_id.display_name = '[%{code}s] %{prefix}s%{name}s%{suffix}s' % {
                'code': self.code,
                'name': self.name,
                'prefix': self.prefix,
                'suffix': self.suffix,
            }

    @api.multi
    @api.contrains('code')
    def _check_unique_code(self, ):
        ''' Constrain that code is unique '''
        for rec_id in self:
            if len(self.search(['code', '=', rec_id.code])) > 1:
                raise ValidationError(
                    'Code (%s) must be unique.' % rec_id.code,
                )

    @api.model
    def create(self, vals, ):
        ''' Overload create & capitalize vals['code'] before save '''
        vals['code'] = vals.get('code', '').capitalize()
        return super(MedicalHistoryType, self).create(vals)

    @api.multi
    def write(self, vals, ):
        ''' Overload write & capitalize vals['code'] before save '''
        if vals.get('code'):
            vals['code'] = vals['code'].capitalize()
        return super(MedicalHistoryType, self).write(vals)


    @api.model
    @api.returns('self')
    def get_by_code(self, code, ):
        '''
        Return a Recordset singleton for the code
        :param code: History type code to search for
        :type code: str
        :rtype: Recordset Singleton
        '''
        return self.search([
            ('code', '=', code),
        ], limit=1)

    @api.model
    @api.returns('self')
    def get_by_name(self, name, ):
        '''
        Return a Recordset for the name
        :param name: History type name to search for
        :type name: str
        :rtype: Recordset
        '''
        return self.search([
            ('name', '=', name)
        ])
