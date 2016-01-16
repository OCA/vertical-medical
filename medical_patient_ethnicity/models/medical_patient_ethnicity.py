# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
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

from openerp import models, fields


class MedicalPatientEthnicity(models.Model):
    _name = 'medical.patient.ethnicity'
    _description = 'Medical Patient Ethnicity'
    notes = fields.Char()
    code = fields.Char(
        required=True,
    )
    name = fields.Char(
        required=True,
        translate=True,
    )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Ethnicity name must be unique.'),
        ('code_uniq', 'UNIQUE(code)', 'Ethnicity code must be unique.'),
    ]
