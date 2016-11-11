# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPatientDisease(TransactionCase):

    def setUp(self):
        super(TestMedicalPatientDisease, self).setUp()
        self.disease_2 = self.env.ref(
            'medical_patient_disease.medical_patient_disease_disease_2'
        )
        self.disease_3 = self.env.ref(
            'medical_patient_disease_allergy.medical_patient_disease_disease_3'
        )

    def test_compute_is_allergy(self):
        """ Test is_allergy True if pathology code_type is allergy """
        self.assertTrue(
            self.disease_3.is_allergy,
            'is_allergy should be True.\rGot: %s\rExpected: %s' % (
                self.disease_3.is_allergy, True
            )
        )

    def test_compute_is_allergy_not_allergy(self):
        """ Test is_allergy not incorrectly set to True """
        self.assertFalse(
            self.disease_2.is_allergy,
            'is_allergy should be True.\rGot: %s\rExpected: %s' % (
                self.disease_2.is_allergy, False
            )
        )
