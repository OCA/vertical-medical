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

from openerp.osv import fields, orm, orm
from openerp.tools.translate import _

from dateutil.relativedelta import relativedelta
from datetime import datetime


class MedicalPatient(orm.Model):
#    _name= 'oemedical.patient'
    _inherit= 'medical.patient'

    _columns={
        'family': fields.many2one('oemedical.family', string='Family', help='Family Code'),
        'blood_type': fields.selection([
                                        ('A', 'A'), 
                                        ('B', 'B'),
                                        ('AB', 'AB'),
                                        ('O', 'O'), ], string='Blood Type'),
        'rh': fields.selection([
                                        ('+', '+'), 
                                        ('-', '-'), ], string='Rh'),
        'primary_care_doctor': fields.many2one('medical.physician', 'Primary Care Doctor', help='Current primary care / family doctor'),
        'childbearing_age': fields.boolean('Potential for Childbearing'),
        'medications': fields.one2many('oemedical.patient.medication', 'patient_id', string='Medications',),
        'evaluations': fields.one2many('oemedical.patient.evaluation', 'patient_id', string='Evaluations',),
        'critical_info': fields.text(string='Important disease, allergy or procedures information', help='Write any important information on the patient\'s disease, surgeries, allergies, ...'),
        'diseases': fields.one2many('oemedical.patient.disease', 'patient_id', string='Diseases', help='Mark if the patient has died'),
        'ethnic_group': fields.many2one('oemedical.ethnicity', string='Ethnic group',),
#        'vaccinations': fields.one2many('oemedical.vaccination', 'patient_id', 'Vaccinations',),
        'cod': fields.many2one('oemedical.pathology', string='Cause of Death',),
    }
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
