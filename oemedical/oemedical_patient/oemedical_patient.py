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
        'partner_id': fields.many2one(
            'res.partner','Related Partner', required=True,
            ondelete='cascade', help='Partner-related data of the patient'),
        'family': fields.many2one('oemedical.family', string='Family', 
                                  help='Family Code'),
        'photo': fields.binary(string='Picture'),
        'sex': fields.selection([('m', 'Male'), ('f', 'Female'), ],
                                string='Sex',required=True),
        'blood_type': fields.selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'),
                                        ('O', 'O'), ], string='Blood Type'),
        'general_info': fields.text(string='General Information', 
                                help='General information about the patient'),
        'primary_care_doctor': fields.many2one('oemedical.physician',
                                               'Primary Care Doctor',
                                help='Current primary care / family doctor'),
        'childbearing_age': fields.boolean('Potential for Childbearing'),
        'medications': fields.one2many('oemedical.patient.medication',
                                       'patient', string='Medications', ),
        'critical_info': fields.text(
            string='Important disease, allergy or procedures information',
            help='Write any important information on the patient\'s disease,'\
            ' surgeries, allergies, ...'),
        'rh': fields.selection([('+', '+'), ('-', '-'), ], string='Rh'),
        'current_address': fields.many2one('res.partner', string='Address', 
        help='Contact information. You may choose from the different contacts'\
        ' and addresses this patient has.'),
        'diseases': fields.one2many('oemedical.patient.disease',
                                    'patient_id', string='Diseases', 
                                    help='Mark if the patient has died'),
        'lastname': fields.char(size=256, string='Lastname',),
        'ethnic_group': fields.many2one('oemedical.ethnicity',
                                        string='Ethnic group', ),
        'ssn': fields.char(size=256, string='SSN',),
        'vaccinations': fields.one2many('oemedical.vaccination', 'patient_id',
                                        'Vaccinations', ),
        'patient': fields.many2one('res.partner', string='Patient', 
                                   help='Patient Name'),
        'dob': fields.date(string='DoB'),
        'age': fields.char(size=256, string='Age',),
        'marital_status': fields.selection([('s', 'Single'), ('m', 'Married'),
                                            ('w', 'Widowed'),
                                            ('d', 'Divorced'),
                                            ('x', 'Separated'), ],
                                           string='Marital Status',sort=False),
        'dod': fields.datetime(string='Date of Death'),
        'current_insurance': fields.many2one('oemedical.insurance',
                                             string='Insurance', 
                help='Insurance information. You may choose from the different'\
        ' insurances belonging to the patient'),
        'cod': fields.many2one('oemedical.pathology',
                               string='Cause of Death', ),
        'identification_code': fields.char(size=256, string='ID',
                                           readonly=True, 
            help='Patient Identifier provided by the Health Center.Is not the'\
            ' Social Security Number'),
        'deceased': fields.boolean(string='Deceased'),
    }
    
    _defaults = {
         'ref': lambda obj, cr, uid, context: 
                obj.pool.get('ir.sequence').get(cr, uid, 'oemedical.patient'),
                 }

OeMedicalPatient()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
