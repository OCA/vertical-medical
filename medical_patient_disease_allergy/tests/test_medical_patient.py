# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):
    def setUp(self, ):
        super(TestMedicalPatient, self).setUp()
        vals = {
            'name': 'Patient 1',
            'gender': 'm',
        }
        patient_id = self.env['medical.patient'].create(vals)
        vals = {
            'name': 'path_1',
            'code': 'path_1',
        }
        pathology_id = self.env['medical.pathology'].create(vals)
        vals = {
            'patient_id': patient_id.id,
            'pathology_id': pathology_id.id,
            'is_allergy': True,
        }
        self.disease_id = self.env['medical.patient.disease'].create(vals)

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
