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


class OeMedicalPatientDisease(osv.osv):
    _name = 'oemedical.patient.disease'

    _columns = {
        'treatment_description': fields.char(size=256, string='Treatment Description', required=True),
        'healed_date': fields.date(string='Healed'),
        'pathology': fields.many2one('oemedical.pathology', string='Disease', ),
        #'disease_severity': fields.selection([], string='Severity'),
        'is_allergy': fields.boolean(string='Allergic Disease'),
        'doctor': fields.many2one('oemedical.physician', string='Physician', ),
        'pregnancy_warning': fields.boolean(string='Pregnancy warning'),
        'weeks_of_pregnancy': fields.integer(string='Contracted in pregnancy week #'),
        'is_on_treatment': fields.boolean(string='Currently on Treatment'),
        'diagnosed_date': fields.date(string='Date of Diagnosis'),
        'extra_info': fields.text(string='Extra Info'),
        #'status': fields.selection([], string='Status of the disease'),
        'is_active': fields.boolean(string='Active disease'),
        'date_stop_treatment': fields.date(string='End'),
        'pcs_code': fields.many2one('oemedical.procedure', string='Code', ),
        'is_infectious': fields.boolean(string='Infectious Disease'),
        #'allergy_type': fields.selection([], string='Allergy type'),
        'rec_name': fields.char(size=256, string='Name', required=True),
        'name': fields.many2one('oemedical.patient', string='Patient', ),
        'age': fields.integer(string='Age when diagnosed'),
        'date_start_treatment': fields.date(string='Start'),
        'short_comment': fields.char(size=256, string='Remarks', required=True),
    }

OeMedicalPatientDisease()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
