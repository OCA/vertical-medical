# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Ported to 8.0 & 9.0 by Dave Lasley - LasLabs (https://laslabs.com)
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
###############################################################################

from openerp import api, fields, models
from openerp.exceptions import ValidationError


class MedicalPathology(models.Model):
    _name = 'medical.pathology'
    _description = 'Medical Pathology'
    _sql_constraints = [
        ('code', 'UNIQUE(code)', 'Pathology codes must be unique.'),
    ]

    name = fields.Char(required=True, translate=True)
    code = fields.Char(required=True)
    notes = fields.Text(translate=True)
    category_id = fields.Many2one(
        string='Category of Pathology',
        comodel_name='medical.pathology.category',
        index=True,
    )
    medical_pathology_group_ids = fields.Many2many(
        string='Medical Pathology Groups',
        comodel_name='medical.pathology.group',
        column1='pathology_id',
        colmun2='pathology_group_id',
        relation="pathology_id_pathology_group_id_rel"
    )
    # @TODO: This should be in medical_genetics
    protein = fields.Char(string='Protein Involved')
    chromosome = fields.Char(string='Affected Chromosome')
    gene = fields.Char(string='Affected Gene')
