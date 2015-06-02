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

from openerp.osv import fields, orm
from openerp.tools.translate import _

from dateutil.relativedelta import relativedelta
from datetime import datetime


class medical_patient_med_center_rel(orm.Model):
    _name = 'medical.patient.med.center.rel'
    _rec_name = 'patient_id'
    _columns = {
        'patient_id': fields.many2one('medical.patient', 'Patient', required=True, select=1, ondelete='cascade'),
        'medical_center_id': fields.many2one('res.partner', 'Medical Center', required=True, select=1, ondelete='cascade', domain="[('is_institution', '=', True)]"),
        'identification_code': fields.char(size=256, string='ID', help='Patient Identifier provided by the Health Center.Is not the Social Security Number'),
    }
    _sql_constraints = [
        ('uniq_patient_center', 'unique(patient_id, medical_center_id)', "You cannot have twice a medical center for a patient"),
    ]


class MedicalPatient(orm.Model):
    _name = 'medical.patient'
    _inherits = {
        'res.users': 'user_id',
    }

    def _get_age(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        age = ''
        now = datetime.now()
        for record in self.browse(cr, uid, ids, context=context):
            if (record.dob):
                dob = datetime.strptime(str(record.dob), '%Y-%m-%d')

                if record.deceased:
                    dod = datetime.strptime(record.dod, '%Y-%m-%d %H:%M:%S')
                    delta = relativedelta(dod, dob)
                    deceased = ' (deceased)'
                else:
                    delta = relativedelta(now, dob)
                    deceased = ''
                years_months_days = str(delta.years) + 'y ' \
                        + str(delta.months) + 'm ' \
                        + str(delta.days) + 'd' + deceased
            else:
                years_months_days = 'No DoB !'

            # Return the age in format y m d when the caller is the field name
            if field_name == 'age':
                age = years_months_days

            res[record.id] = age
        return res

    _columns = {
        'id': fields.integer('ID', readonly=True),
        'user_id': fields.many2one(
            'res.users', 'Related User', required=True,
            ondelete='cascade', help='User-related data of the patient'),
        'sex': fields.selection([('m', 'Male'), ('f', 'Female'), ], string='Sex', required=True),
        'general_info': fields.text(string='General Information', help='General information about the patient'),
        'dob': fields.date(string='DoB'),
        'medical_center_ids': fields.one2many('medical.patient.med.center.rel', 'patient_id', 'Related Medical Centers', readonly=True),
        'age': fields.function(_get_age, type='char', string='Age', help="It shows the age of the patient in years(y), months(m) and days(d).\nIf the patient has died, the age shown is the age at time of death, the age corresponding to the date on the death certificate. It will show also \"deceased\" on the field", multi=False),
        'marital_status': fields.selection([('s', 'Single'), ('m', 'Married'),
                                            ('w', 'Widowed'),
                                            ('d', 'Divorced'),
                                            ('x', 'Separated'),
                                            ('z', 'law marriage'),
                                            ],
                                           string='Marital Status', sort=False),
        'deceased': fields.boolean(string='Deceased'),
        'dod': fields.datetime(string='Date of Death'),
        'identification_code': fields.char(size=256, string='ID', help='Patient Identifier provided by the Health Center.Is not the Social Security Number'),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the patient without removing it."),
    }

    def create(self, cr, uid, vals, context=None):
        sequence = unicode(self.pool.get('ir.sequence').get(cr, uid, 'medical.patient'))
        vals['identification_code'] = sequence
        vals['is_patient'] = True
        vals['customer'] = True
        return super(MedicalPatient, self).create(cr, uid, vals, context=context)

MedicalPatient()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
