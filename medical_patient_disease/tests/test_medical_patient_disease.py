# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp import fields


class TestMedicalPatientDisease(TransactionCase):

    def setUp(self):
        super(TestMedicalPatientDisease, self).setUp()
        self.disease_1 = self.env.ref(
            'medical_patient_disease.medical_patient_disease_disease_1'
        )
        self.disease_2 = self.env.ref(
            'medical_patient_disease.medical_patient_disease_disease_2'
        )

    def test_name_without_short_comment(self):
        """ Test name without short_comment present """
        self.assertEquals(
            self.disease_1.name, 'Malaria - Cause of death',
            'Name should include short_comment.\rGot: %s\rExpected: %s' % (
                self.disease_1.name, 'Malaria - Cause of death'
            )
        )

    def test_name_with_short_comment(self):
        """ Test name if short_comment present """
        self.assertEquals(
            self.disease_2.name, 'HIV/AIDS',
            'Name should include short_comment.\rGot: %s\rExpected: %s' % (
                self.disease_2.name, 'HIV/AIDS'
            )
        )

    def test_compute_expire_date_active_disease(self):
        """ Test expire_date is False if disease is active """
        self.disease_2.active = True
        self.assertFalse(
            self.disease_2.expire_date,
            'expire_date should be False.\rGot: %s\rExpected: %s' % (
                self.disease_2.expire_date, False
            )
        )

    def test_compute_expire_date_not_active_disease(self):
        """ Test expire_date is Datetime.now() if disease not active """
        self.disease_2.active = False
        self.assertEquals(
            self.disease_2.expire_date, fields.Datetime.now(),
            'expire_date should be Datetime.now().\rGot: %s\rExpected: %s' % (
                self.disease_2.expire_date, fields.Datetime.now()
            )
        )

    def test_action_invalidate(self):
        """ Test disease active field is False on invalidation """
        self.disease_2.active = True
        self.disease_2.action_invalidate()
        self.assertFalse(
            self.disease_2.active,
            'Partner should be reactivated.\rGot: %s\rExpected: %s' % (
                self.disease_2.active, False
            )
        )

    def test_action_revalidate(self):
        """ Test disease active field is True on revalidation """
        self.disease_2.active = False
        self.disease_2.action_revalidate()
        self.assertTrue(
            self.disease_2.active,
            'Disease should be reactivated.\rGot: %s\rExpected: %s' % (
                self.disease_2.active, True
            )
        )
