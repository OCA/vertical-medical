# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from dateutil.relativedelta import relativedelta
from openerp.exceptions import ValidationError
from openerp import fields
from openerp.tests.common import TransactionCase
from datetime import datetime


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.patient_1 = self.env.ref('medical.medical_patient_patient_1')
        self.partner_patient_1 = self.env.ref('medical.res_partner_patient_1')
        self.patient_3 = self.env.ref('medical.medical_patient_patient_3')

    def test_sequence_for_identification_code(self):
        """ Test identification_code created if there is none """
        self.assertTrue(
            self.patient_1.identification_code,
            'Should make id code if none.\rGot: %s\rExpected: %s' % (
                self.patient_1.identification_code, 'A truthey value'
            )
        )

    def test_partner_is_patient(self):
        """ Test is_patient set to True on partner """
        self.assertTrue(
            self.partner_patient_1.is_patient,
            'is_patient should be True.\rGot: %s\rExpected: %s' % (
                self.partner_patient_1.is_patient, True
            )
        )

    def test_pregnant_male_raises_error(self):
        """ Test raises ValidationError if male pregnant """
        with self.assertRaises(ValidationError):
            self.patient_3.is_pregnant = True

    def test_pregnant_female_no_error(self):
        """ Test no ValidationError if female is pregnant """
        try:
            self.patient_1.is_patient = True
            self.assertTrue(True)
        except ValidationError:
            self.fail(
                'Should not raise ValidationError if female pregnant'
            )

    def test_compute_age(self):
        """ Test compute_age with no special cases """
        now = datetime.now()
        dob = fields.Datetime.from_string(self.patient_1.dob)
        delta = relativedelta(now, dob)
        age = '%s%s %s%s %s%s' % (
            delta.years, 'y',
            delta.months, 'm',
            delta.days, 'd',
        )
        self.assertEqual(
            self.patient_1.age, age,
            'Should be the same age.\rGot: %s\rExpected: %s' % (
                self.patient_1.age, age
            )
        )

    def test_compute_age_patient_deceased(self):
        """ Test age properly set if patient deceased """
        self.assertEquals(
            self.patient_3.age, '36y 1m 20d (deceased)',
            'Should be the same age.\rGot: %s\rExpected: %s' % (
                self.patient_3.age, '36y 1m 20d (deceased)'
            )
        )

    def test_compute_age_no_dob_set(self):
        """ Test age equals 'No DoB !' if no dob present """
        self.patient_1.dob = None
        self.assertEquals(
            self.patient_1.age, 'No DoB!',
            'Age is incorrect.\rGot: %s\rExpected: %s' % (
                self.patient_1.age, 'No DoB!'
            )
        )

    def test_action_invalidate(self):
        """ Test invalidate patient also invalidates partner """
        self.patient_1.action_invalidate()
        self.assertEquals(
            [self.partner_patient_1.active, self.patient_1.active],
            [False, False],
            'Should be inactive.\rGot: %s\rExpected: %s' % (
                [self.partner_patient_1.active, self.patient_1.active],
                [False, False]
            )
        )

    def test_patient_deceased_if_dod_exists(self):
        """ Test deceased is True if value set on dod """
        self.assertTrue(
            self.patient_3.deceased,
            'Should be deceased if dod exists.\rGot: %s\rExpected: %s' % (
                self.patient_3.deceased, True
            )
        )

    def test_patient_not_deceased_if_no_dod(self):
        """ Test deceased is False if no value set on dod """
        self.assertFalse(
            self.patient_1.deceased,
            'Should not be deceased if no dod.\rGot: %s\rExpected: %s' % (
                self.patient_1.deceased, False
            )
        )
