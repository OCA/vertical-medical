# -*- coding: utf-8 -*-
#
#    Copyright (C) 2008-2010  Luis Falcon
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
from openerp.osv import fields, orm


class surgery (orm.Model):
    _name = "oemedical.surgery"
    _description = "Surgery"
    _columns = {
        'name': fields.many2one(
            'oemedical.procedure',
            'Code',
            help="Procedure Code, for example ICD-10-PCS Code 7-character"
                 " string"),
        'pathology': fields.many2one(
            'oemedical.pathology', 'Base condition',
            help="Base Condition / Reason"),
        'classification': fields.selection([
            ('o', 'Optional'),
            ('r', 'Required'),
            ('u', 'Urgent'),
        ], 'Surgery Classification', select=True),
        'surgeon': fields.many2one(
            'oemedical.physician',
            'Surgeon',
            help="Surgeon who did the procedure"),
        'date': fields.datetime('Date of the surgery'),
        'age': fields.char(
            'Patient age',
            size=3,
            help='Patient age at the moment of the surgery. Can be estimative'
            ),
        'description': fields.char('Description', size=128),
        'extra_info': fields.text('Extra Info'),
    }


# Add to the Medical patient_data class (oemedical.patient) the surgery field.

class oemedical_patient (orm.Model):
    _name = "oemedical.patient"
    _inherit = "oemedical.patient"
    _columns = {
        'surgery': fields.many2many(
            'oemedical.surgery',
            'patient_surgery_rel', 'patient_id', 'surgery_id', 'Surgeries'),

    }
