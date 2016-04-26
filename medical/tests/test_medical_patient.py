# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical, an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical is free software:
#     you can redistribute it and/or
#     modify it under the terms of the GNU Affero General Public License
#     as published by the Free Software Foundation, either version 3 of
#     the License, or (at your option) any later version.
#
#     medical is distributed in the hope that it will
#     be useful but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the
#     GNU Affero General Public License
#     along with medical.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from dateutil.relativedelta import relativedelta

from openerp import fields
from openerp.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.vals = {
            'name': 'Patient 1',
            'gender': 'm',
        }
        self.context_date = fields.Date.from_string('2016-01-01')

    def model_obj(self):
        return self.env['medical.patient'].with_context({
            'date': fields.Date.to_string(self.context_date),
        })

    def test_sequence(self):
        patient_id = self.env['medical.patient'].create(self.vals)
        self.assertTrue(
            patient_id.identification_code, 'Should have a sequence')

    def test_age_computation_dob(self):
        """ Check value of age depending of the birth_date """
        age = 10
        complete_age = '10y 0m 0d'
        birth_date = fields.Date.to_string(
            self.context_date - relativedelta(years=age)
        )
        self.vals['dob'] = birth_date
        patient_id = self.model_obj().create(self.vals)
        self.assertEquals(
            complete_age, patient_id.age,
            'Should be the same age'
        )

    def test_age_computation_dob_leap_year(self):
        """ Check age computation when patient born on Feb 29 """
        complete_age = '3y 0m 0d'
        self.context_date = fields.Date.from_string('2015-02-28')
        birth_date = '2012-02-29'
        self.vals['dob'] = birth_date
        patient_id = self.model_obj().create(self.vals)
        self.assertEquals(
            complete_age, patient_id.age,
            'Should be the same age'
        )

    def test_age_computation_dod(self):
        """ Check value of age depending on the death date """
        age = 5
        birth_date = fields.Date.to_string(
            self.context_date - relativedelta(years=age)
        )
        vals = {
            'deceased': True,
            'dod': fields.Date.to_string(self.context_date),
            'dob': birth_date,
        }
        self.vals.update(vals)
        patient_id = self.model_obj().create(self.vals)
        dod_age = '5y 0m 0d'
        self.assertEquals(
            '%s (deceased)' % dod_age, patient_id.age,
            'Should be the same age',
        )

    def test_age_computation_no_dob(self):
        """ Check age computation w/ no DOB """
        res = self.model_obj().create(self.vals)
        self.assertEqual(
            'No DoB !', res.age,
        )

    def test_invalidate(self):
        """
        Invalidate a patient should invalidate its diseases
        """
        patient_id = self.env['medical.patient'].create(self.vals)
        self.assertTrue(patient_id.active, 'Should be active')
        self.assertTrue(patient_id.partner_id.active, 'Should be inactive')
        self.assertFalse(patient_id.dod, 'Should be empty')
        patient_id.action_invalidate()
        self.assertFalse(patient_id.active, 'Should be inactive')
        self.assertFalse(patient_id.partner_id.active, 'Should be inactive')
