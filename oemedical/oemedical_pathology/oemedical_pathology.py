# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
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
#/#############################################################################
from osv import osv
from osv import fields


class OeMedicalPathology(osv.Model):
    _name = 'oemedical.pathology'

    _columns = {
        'category': fields.many2one('oemedical.pathology.category',
                                    string='Main Category', 
              help='Select the main category for this disease This is usually'\
        'associated to the standard. For instance, the chapter on the ICD-10'\
        'will be the main category for de disease' ),
        'info': fields.text(string='Extra Info'),
        'code': fields.char(size=256, string='Code', required=True, 
                            help='Specific Code for the Disease (eg, ICD-10)'),
        'name': fields.char(size=256, string='Name', required=True,
                            translate=True, help='Disease name'),
        'groups': fields.one2many('oemedical.disease_group.members',
                                  'disease_group_id', string='Groups',
                     help='Specify the groups this pathology belongs. Some' \
                     ' automated processes act upon the code of the group' ),
        'protein': fields.char(size=256, string='Protein involved', 
                               help='Name of the protein(s) affected'),
        'gene': fields.char(size=256, string='Gene'),
        'chromosome': fields.char(size=256, string='Affected Chromosome', 
                                  help='chromosome number'),
    }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
OeMedicalPathology()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
