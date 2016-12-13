# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.patient_5 = self.env.ref(
            'medical_patient_disease_allergy.medical_patient_patient_5'
        )

    def test_compute_count_allergy_ids(self):
        """ Test amount of allergy diseases calculated """
        self.assertEquals(
            self.patient_5.count_allergy_ids, 1,
        )
