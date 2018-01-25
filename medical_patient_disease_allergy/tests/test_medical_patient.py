# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.disease_3 = self.env.ref(
            'medical_patient_disease_allergy.medical_patient_disease_disease_3'
        )
        self.patient_5 = self.env.ref(
            'medical_patient_disease_allergy.medical_patient_patient_5'
        )
        self.partner_5 = self.env.ref(
            'medical_patient_disease_allergy.res_partner_patient_5'
        )

    def test_action_invalidate(self):
        """ Test patient, partner, disease properly invalidated """
        self.patient_5.active = True
        self.partner_5.active = True
        self.disease_3.active = True
        self.patient_5.action_invalidate()
        res = [
            self.patient_5.active,
            self.partner_5.active,
            self.disease_3.active,
        ]
        expect = [False] * 3
        self.assertEquals(
            res, expect,
            'Not all 3 have been invalidated .\rGot: %s\rExpected: %s' % (
                res, expect
            )
        )

    def test_compute_count_allergy_ids(self):
        """ Test amount of allergy diseases calculated """
        self.assertEquals(
            self.patient_5.count_allergy_ids, 1,
            'Disease ids length should be 1.\rGot: %s\rExpected: %s' % (
                self.patient_5.count_allergy_ids, 1
            )
        )
