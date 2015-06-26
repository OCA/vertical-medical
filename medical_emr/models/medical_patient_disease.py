# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Ported to 8.0 by Dave Lasley - LasLabs (https://laslabs.com)
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

from openerp.osv import fields, orm
from openerp.tools.translate import _


class MedicalPatientDisease(orm.Model):
    _name = 'medical.patient.disease'

    _columns = {
        'treatment_description': fields.char(size=256,
                                             string='Treatment Description'),
        'healed_date': fields.date(string='Healed'),
        'pathology': fields.many2one('medical.pathology',
                                     string='Disease',help='Disease'),
        'disease_severity': fields.selection([
            ('1_mi', 'Mild'),
            ('2_mo', 'Moderate'),
            ('3_sv', 'Severe'),
        ], string='Severity',select=True, sort=False),
        'is_allergy': fields.boolean(string='Allergic Disease'),
        'doctor': fields.many2one('medical.physician', string='Physician', 
                        help='Physician who treated or diagnosed the patient'),
        'pregnancy_warning': fields.boolean(string='Pregnancy warning'),
        'weeks_of_pregnancy': fields.integer(
            string='Contracted in pregnancy week #'),
        'is_on_treatment': fields.boolean(string='Currently on Treatment'),
        'diagnosed_date': fields.date(string='Date of Diagnosis'),
        'extra_info': fields.text(string='Extra Info'),
        'status': fields.selection([
            ('a', 'acute'),
            ('c', 'chronic'),
            ('u', 'unchanged'),
            ('h', 'healed'),
            ('i', 'improving'),
            ('w', 'worsening'),
        ], string='Status of the disease',select=True, sort=False),
        'is_active': fields.boolean(string='Active disease'),
        'date_stop_treatment': fields.date(string='End', 
                                           help='End of treatment date'),
        'pcs_code': fields.many2one('medical.procedure', string='Code', 
        help='Procedure code, for example, ICD-10-PCS Code 7-character string'),
        'is_infectious': fields.boolean(string='Infectious Disease',
                                help='Check if the patient has an infectious' \
                                'transmissible disease'),
        'allergy_type': fields.selection([
            ('da', 'Drug Allergy'),
            ('fa', 'Food Allergy'),
            ('ma', 'Misc Allergy'),
            ('mc', 'Misc Contraindication'),
        ], string='Allergy type',select=True, sort=False),
        'patient_id': fields.many2one('medical.patient', string='Patient', ),
        'age': fields.integer(string='Age when diagnosed',  
          help='Patient age at the moment of the diagnosis. Can be estimative'),
        'date_start_treatment': fields.date(string='Start', 
                                            help='Start of treatment date'),
        'short_comment': fields.char(size=256, string='Remarks',
        help='Brief, one-line remark of the disease. Longer description will'\
        ' go on the Extra info field'),
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
