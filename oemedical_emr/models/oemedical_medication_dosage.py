# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################
from openerp.osv import fields, orm


class OeMedicalMedicationDosage(orm.Model):
    _name = 'oemedical.medication.dosage'

    _columns = {
        'abbreviation': fields.char(
            string='Abbreviation', size=256,
            help='Dosage abbreviation, such as tid in the US or tds in the UK'
            ),
        'code': fields.char(
            string='Code', size=8,
            help='Dosage Code,for example: SNOMED 229798009 = 3 times per day'
            ),
        'name': fields.char(
            string='Frequency', size=256,
            required=True, translate=True),
    }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
