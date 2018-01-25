# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.disease_2 = self.env.ref(
            'medical_patient_disease.medical_patient_disease_disease_2'
        )
        self.patient_4 = self.env.ref(
            'medical_patient_disease.medical_patient_patient_4'
        )
        self.partner_4 = self.env.ref(
            'medical_patient_disease.res_partner_patient_4'
        )

    def test_compute_count_disease_ids(self):
        """ Test amount of diseases calculated """
        self.assertEquals(
            self.patient_4.count_disease_ids, 1,
            'Disease ids length should be 1.\rGot: %s\rExpected: %s' % (
                self.patient_4.count_disease_ids, 1,
            )
        )

    def test_action_invalidate(self):
        """ Test patient, partner, disease properly invalidated """
        self.patient_4.active = True
        self.partner_4.active = True
        self.disease_2.active = True
        self.patient_4.action_invalidate()
        res = [
            self.patient_4.active,
            self.partner_4.active,
            self.disease_2.active,
        ]
        expect = [False] * 3
        self.assertEquals(
            res, expect,
            'Not all 3 have been invalidated .\rGot: %s\rExpected: %s' % (
                res, expect
            )
        )

    def test_action_revalidate(self):
        """ Test patient, partner, disease properly revalidated """
        self.patient_4.active = False
        self.partner_4.active = False
        self.disease_2.active = False
        self.patient_4.action_revalidate()
        res = [
            self.patient_4.active,
            self.partner_4.active,
            self.disease_2.active,
        ]
        expect = [True] * 3
        self.assertEquals(
            res, expect,
            'Not all 3 have been invalidated .\rGot: %s\rExpected: %s' % (
                res, expect
            )
        )
