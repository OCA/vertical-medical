# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import api, fields, models
from openerp.exceptions import ValidationError


class MedicalPathology(models.Model):
    _name = 'medical.pathology'
    _description = 'Medical Pathology'

    @api.one
    @api.constrains('code')
    def _check_unicity_name(self):
        domain = [
            ('code', '=', self.code),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError('"code" Should be unique per Pathology')

    name = fields.Char(string='Name', required=True, translate=True)
    code = fields.Char(string='Code', required=True)
    notes = fields.Text(string='Notes')
    protein = fields.Char(string='Protein involved')
    chromosome = fields.Char(string='Affected Chromosome')
    gene = fields.Char(string='Gene')
    category_id = fields.Many2one(
        comodel_name='medical.pathology.category',
        string='Category of Pathology', select=True)
    medical_disease_group_members_ids = fields.One2many(
        comodel_name='medical.disease_group.members',
        inverse_name='disease_group_id', string='Disease Groups')
