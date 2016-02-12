# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api
from openerp.exceptions import ValidationError


class MedicalHistoryType(models.Model):
    '''
    Provides History Types to be used as classification for change logging
    '''

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
        ('all', 'All'),
    ],
        help='New columns to save in the history record',
        default='none',
    )

    @api.multi
    def _compute_display_name(self, ):
        ''' Compute name for representation to user '''
        for rec_id in self:
            rec_id.display_name = '[%(code)s] %(prefix)s%(name)s%(suffix)s' % {
                'code': self.code,
                'name': self.name,
                'prefix': self.prefix,
                'suffix': self.suffix,
            }

    @api.multi
    @api.constrains('code')
    def _check_unique_code(self, ):
        ''' Constrain that code is unique '''
        for rec_id in self:
            if len(self.search([('code', '=', rec_id.code)])) > 1:
                raise ValidationError(
                    'Code (%s) must be unique.' % rec_id.code,
                )

    @api.model
    @api.returns('self')
    def get_by_code(self, code, ):
        '''
        Return a Recordset singleton for the code

        Args:
            code: `str` of History Type code to search for

        Returns:
            `Recordset` Singleton of the History Type matching code
        '''
        return self.search([
            ('code', '=', code),
        ], limit=1)

    @api.model
    @api.returns('self')
    def get_by_name(self, name, operator='=', ):
        '''
        Return a Recordset for the name

        Args:
            name: `str` of History Type name to search for
            operator: `str` domain operator to apply (`like`, `=like`, etc.)

        Returns:
            `Recordset` of History Type(s) matching name
        '''
        return self.search([
            ('name', operator, name)
        ])
