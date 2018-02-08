# -*- coding: utf-8 -*-
# #############################################################################
#
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

from openerp import fields, models


class MedicalMedicationDosage(models.Model):
    _name = 'medical.medication.dosage'
    _description = 'Medical Medication Dosage'

    name = fields.Char(required=True, translate=True)
    abbreviation = fields.Char(
        help='Dosage abbreviation, such as tid in the US or tds in the UK')
    code = fields.Char(
        help='Dosage Code,for example: SNOMED 229798009 = 3 times per day')

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
