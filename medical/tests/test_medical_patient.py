# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta

from openerp import fields
from openerp.tests.common import TransactionCase
from datetime import date


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.model_obj = self.env['medical.patient']
        self.vals = {
            'name': 'Patient 1',
            'gender': 'm',
        }

    def test_sequence(self):
        patient_id = self.model_obj.create(self.vals)
        self.assertTrue(
            patient_id.identification_code, 'Should have a sequence'
        )

    def test_is_patient(self, ):
        ''' Validate that is_patient is set on the partner '''
        patient_id = self.model_obj.create(self.vals)
        self.assertTrue(
            patient_id.is_patient, '`is_patient` not set on partner'
        )

    def test_age_computation(self):
        ''' Check value of age depending of the birth_date '''
        age = 10
        complete_age = '10y 0m 0d'
        birth_date = fields.Date.to_string(
            date.today() - relativedelta(years=age)
        )
        self.vals['dob'] = birth_date
        patient_id = self.model_obj.create(self.vals)
        self.assertEquals(
            complete_age, patient_id.age,
            'Should be the same age.\rGot: %s\rExpected: %s' % (
                patient_id.age, complete_age
            )
        )

    def test_age_computation_deceased(self, ):
        """ Check proper handling of deceased patient """
        age = 5
        birth_date = fields.Date.to_string(
            date.today() - relativedelta(years=age*2)
        )
        self.vals.update({
            'dob': birth_date,
            'deceased': True,
            'dod': fields.Date.to_string(
                date.today() - relativedelta(years=age)
            )
        })
        patient_id = self.model_obj.create(self.vals)
        dod_age = '5y 0m 0d'
        expect = '%s (deceased)' % dod_age
        self.assertEquals(
            expect, patient_id.age,
            'Did not properly handle deceased.\rGot: %s\rExpected: %s' % (
                patient_id.age, expect
            )
        )

    def test_invalidate(self):
        """
        Invalidate a patient should invalidate itself and partner
        """
        patient_id = self.model_obj.create(self.vals)
        self.assertTrue(patient_id.active, 'Should be active')
        self.assertTrue(patient_id.partner_id.active, 'Should be inactive')
        self.assertFalse(patient_id.dod, 'Should be empty')
        patient_id.action_invalidate()
        self.assertFalse(patient_id.active, 'Patient should be inactive')
        self.assertFalse(patient_id.partner_id.active,
                         'Partner should be inactive')
