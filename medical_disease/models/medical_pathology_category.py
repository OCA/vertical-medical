# -*- coding: utf-8 -*-
# #############################################################################
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
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
# #############################################################################

from openerp import api, fields, models
from openerp.exceptions import ValidationError


class MedicalPathologyCategory(models.Model):
    _name = 'medical.pathology.category'
    _description = 'Medical Pathology Category'

    @api.one
    @api.constrains('parent_id')
    def _check_recursion_parent_id(self):
        if not self._check_recursion():
            raise ValidationError('Error! You can not create recursive zone.')

    name = fields.Char(required=True, translate=True)
    child_ids = fields.One2many(
        comodel_name='medical.pathology.category', inverse_name='parent_id',
        string='Children Categories')
    parent_id = fields.Many2one(
        comodel_name='medical.pathology.category', string='Parent Category',
        index=True)
