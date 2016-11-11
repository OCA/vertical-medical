# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from .common import CommonTestBase


class TestMedicalPatient(CommonTestBase):

    def test_invalidate(self, ):
        self.assertTrue(
            self.disease_id.active,
            'Disease should be active before invalidation'
        )
        self.disease_id.patient_id.action_invalidate()
        self.assertFalse(
            self.disease_id.active,
            'Allergy should be inactive after invalidation'
        )
        self.assertFalse(
            self.disease_id.patient_id.active,
            'Patient should be inactive after invalidation'
        )

    def test_compute_allergy(self, ):
        self.assertEquals(
            self.disease_id.patient_id.count_allergy_ids, 1,
            'Should have one allergy'
        )
