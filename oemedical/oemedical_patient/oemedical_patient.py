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


class OeMedicalPatient(osv.osv):
    _name = 'oemedical.patient'
    _inherits = {
        'res.partner': 'partner_id',
    }
    _columns = {
        'partner_id': fields.many2one('res.partner', required=True,
                                      string='Related Partner', 
                                      ondelete='cascade',
                                  help='Partner-related data of the patient'),
        'family': fields.many2one('oemedical.family', string='Family', ),
        'photo': fields.binary(string='Picture'),
        'sex': fields.selection([('m', 'Male'), ('f', 'Female'), ],
            string='Sex'),
        'blood_type': fields.selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'),
                                        ('O', 'O'), ], string='Blood Type'),
        'general_info': fields.text(string='General Information'),
        'primary_care_doctor': fields.many2one('oemedical.physician',
            string='Primary Care Doctor', ),
        'childbearing_age': fields.boolean(
            string='Potential for Childbearing'),
        'medications': fields.one2many('oemedical.patient.medication',
            'patient', string='Medications', ),
        'critical_info': fields.text(
            string='Important disease, allergy or procedures information'),
        'rh': fields.selection([('+', '+'), ('-', '-'), ], string='Rh'),
        'current_address': fields.many2one('res.partner', string='Address', ),
        'diseases': fields.one2many('oemedical.patient.disease',
            'patient_id', string='Diseases', ),
        'lastname': fields.char(size=256, string='Lastname', required=True),
        'ethnic_group': fields.many2one('oemedical.ethnicity',
            string='Ethnic group', ),
        'ssn': fields.char(size=256, string='SSN', required=True),
        'vaccinations': fields.one2many('oemedical.vaccination',
            'patient_id',
            string='Vaccinations', ),
        'patient': fields.many2one('res.partner', string='Patient', ),
        'dob': fields.date(string='DoB'),
        'age': fields.char(size=256, string='Age', required=True),
        'marital_status': fields.selection([('s', 'Single'), ('m', 'Married'),
                                            ('w', 'Widowed'),
                                            ('d', 'Divorced'),
                                            ('x', 'Separated'), ],
            string='Marital Status'),
        'dod': fields.datetime(string='Date of Death'),
        'current_insurance': fields.many2one('oemedical.insurance',
            string='Insurance', ),
        'cod': fields.many2one('oemedical.pathology',
            string='Cause of Death', ),
        'identification_code': fields.char(size=256, string='ID',
            required=True),
        'deceased': fields.boolean(string='Deceased'),
    }

OeMedicalPatient()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
