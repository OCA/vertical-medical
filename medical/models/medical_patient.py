# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp.osv import fields, orm

from dateutil.relativedelta import relativedelta
from datetime import datetime
from openerp.tools.translate import _


class MedicalPatientMedCenterRel(orm.Model):
    _name = 'medical.patient.med.center.rel'
    _rec_name = 'patient_id'
    _columns = {
        'patient_id': fields.many2one('medical.patient', 'Patient',
                                      required=True,
                                      select=1, ondelete='cascade'),
        'medical_center_id': fields.many2one('res.partner', 'Medical Center',
                                             required=True, select=1,
                                             ondelete='cascade',
                                             domain="[('is_institution',"
                                                    "  '=', True)]"),
        'identification_code': fields.char(size=256, string='ID',
                                           help='Patient Identifier '
                                                'provided by the '
                                                'Health Center.Is not the '
                                                'Social Security Number'),
    }
    _sql_constraints = [('uniq_patient_center',
                         'unique(patient_id, medical_center_id)',
                         "You cannot have twice a medical "
                         "center for a patient"), ]


class MedicalPatient(orm.Model):
    '''
    The concept of Patient included in medical.

    A patient is an User with extra elements due to the fact that we will
    re-use all the ACL related to users to manage the security of a patient
    form around medical.
    '''
    _name = 'medical.patient'
    _inherits = {'res.partner': 'partner_id', }

    def _get_default_patient_id(self, cr, uid, context=None):
        """ Gives default patient_id """
        patient_ids = self.search(cr, uid, [('name', '=', 'Libre')],
                                  context=context)
        if not patient_ids:
            raise orm.except_orm(_('Error!'), _('No default patient defined'))

        return patient_ids[0]

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
                years_months_days = str(delta.years) + 'y ' + str(
                    delta.months) + 'm ' + str(delta.days) + 'd' + deceased
            else:
                years_months_days = 'No DoB !'
            # Return the age in format y m d when the caller is the field name
            if field_name == 'age':
                age = years_months_days

            res[record.id] = age
        return res

    _columns = {
        'id': fields.integer('ID', readonly=True),
        'partner_id': fields.many2one('res.partner', 'Related Partner',
                                      required=True,
                                      ondelete='cascade',
                                      help='Partner-related data of '
                                           'the patient'),
        'sex': fields.selection([('m', 'Male'), ('f', 'Female')],
                                string='Sex', required=True),
        'general_info': fields.text(string='General Information',
                                    help="General information about "
                                         "the"
                                         "patient"),

        'dob': fields.date(string='DoB'),
        'medical_center_ids': fields.one2many('medical.patient.med.center.rel',
                                              'patient_id',
                                              "Related Medical Centers",
                                              readonly=True),
        'age': fields.function(_get_age, type='char', string='Age',
                               help="It shows the age of the patient "
                                    "in years(y), months(m) and days(d).\n"
                                    "If the patient has died, the age shown is"
                                    "the age at time of death, the age "
                                    "corresponding to the date on the death "
                                    "certificate. It will show "
                                    "also \"deceased\" on the field",
                               multi=False),
        'marital_status': fields.selection([('s', 'Single'),
                                            ('m', 'Married'),
                                            ('w', 'Widowed'),
                                            ('d', 'Divorced'),
                                            ('x', 'Separated'),
                                            ('z', 'law marriage'), ],
                                           string='Marital Status',
                                           sort=False),
        'deceased': fields.boolean(string='Deceased'),
        'dod': fields.datetime(string='Date of Death'),
        'identification_code': fields.char(size=256,
                                           string='Internal '
                                                  'Identification',
                                           help='Patient Identifier '
                                                'provided '
                                                'by the Health '
                                                'Center.Is not the '
                                                'Social Security '
                                                'Number'),
        'active': fields.boolean('Active',
                                 help="If unchecked, it will allow "
                                      "you to hide the patient without "
                                      "removing it."),
    }
    _defaults = {'is_patient': True, 'customer': True, 'active': True, }

    def create(self, cr, uid, vals, context=None):
        if not vals.get('identification_code', False):
            sequence = unicode(
                self.pool.get('ir.sequence').get(cr, uid, 'medical.patient'))
            vals['identification_code'] = sequence

        # When we create a patient we need ensure it belong to the group with
        # ACL's patients.
        groups_proxy = self.pool['res.groups']
        group_ids = groups_proxy.search(cr, uid,
                                        [('name', '=', 'OEMedical User')],
                                        context=context)
        vals['groups_id'] = [(6, 0, group_ids)]

        return super(MedicalPatient, self).create(cr, uid, vals,
                                                  context=context)