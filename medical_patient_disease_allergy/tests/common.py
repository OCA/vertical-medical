# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class CommonTestBase(TransactionCase):
    def setUp(self, ):
        super(CommonTestBase, self).setUp()
        vals = {
            'name': 'Patient 1',
            'gender': 'm',
        }
        patient_id = self.env['medical.patient'].create(vals)
        allergy_code = self.env.ref(
            'medical_patient_disease_allergy.pathology_code_allergy',
        )
        vals = {
            'name': 'path_1',
            'code': 'path_1',
            'code_type_id': allergy_code.id,
        }
        pathology_id = self.env['medical.pathology'].create(vals)
        vals = {
            'patient_id': patient_id.id,
            'pathology_id': pathology_id.id,
            'is_allergy': True,
        }
        self.disease_id = self.env['medical.patient.disease'].create(vals)
