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


class OeMedicalPathology(osv.osv):
    _name = 'oemedical.pathology'

    _columns = {
        'category': fields.many2one('oemedical.pathology.category',
                                    string='Main Category', ),
        'info': fields.text(string='Extra Info'),
        'code': fields.char(size=256, string='Code', required=True),
        'name': fields.char(size=256, string='Name', required=True),
        'groups': fields.one2many('oemedical.disease_group.members',
                                   'disease_group_id', string='Groups', ),
        'protein': fields.char(size=256, string='Protein involved',
                               required=True),
        'gene': fields.char(size=256, string='Gene', required=True),
        'chromosome': fields.char(size=256, string='Affected Chromosome',
                                  required=True),
    }

OeMedicalPathology()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
