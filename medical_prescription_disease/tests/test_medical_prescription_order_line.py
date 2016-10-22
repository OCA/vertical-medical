# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()
        self.patient_vals = {
            'name': 'Test Patient',
        }
        self.physician_vals = {
            'name': 'Test Physician',
        }
        self.pathology_vals = {
            'name': 'Pathology',
            'code': 'PAT',
        }
        self.specialty_vals = {
            'name': 'Specialty',
            'code': 'SPEC',
        }
        self.medicament_vals = {
            'name': 'simvastatin',
            'drug_form_id': self.env.ref('medical_medicament.AEM').id,
        }
        self.order_vals = {}
        self.vals = {}

    def _new_record(self, ):
        self.patient_id = self.env['medical.patient'].create(
            self.patient_vals,
        )
        self.pathology_id = self.env['medical.pathology'].create({
            'name': 'Another Pathology',
            'code': 'PAT2',
        })
        self.specialty_id = self.env['medical.specialty'].create(
            self.specialty_vals,
        )
        self.medicament_id = self.env['medical.medicament'].create(
            self.medicament_vals
        )
        self.physician_vals.update({
            'specialty_id': self.specialty_id.id,
        })
        self.physician_id = self.env['medical.physician'].create(
            self.physician_vals,
        )
        self.disease_id = self.env['medical.patient.disease'].create({
            'patient_id': self.patient_id.id,
            'physician_id': self.physician_id.id,
            'pathology_id': self.pathology_id.id,
        })
        self.order_vals.update({
            'patient_id': self.patient_id.id,
            'physician_id': self.physician_id.id,
        })
        self.rx_id = self.env['medical.prescription.order'].create(
            self.order_vals,
        )
        self.vals.update({
            'disease_id': self.disease_id.id,
            'medicament_id': self.medicament_id.id,
            'prescription_order_id': self.rx_id.id,
            'patient_id': self.patient_id.id,
            'physician_id': self.physician_id.id,
        })
        return self.env['medical.prescription.order.line'].create(
            self.vals
        )

    def test_onchange_disease_id(self, ):
        rec_id = self._new_record()
        disease_id = self.env['medical.patient.disease'].create({
            'patient_id': self.patient_id.id,
            'physician_id': self.physician_id.id,
            'pathology_id': self.pathology_id.id,
        })
        rec_id.disease_id = disease_id.id
        self.assertEqual(
            self.patient_id, rec_id.patient_id,
            'Patient did not change w/ disease. Expect %s got %s' % (
                self.patient_id, rec_id.patient_id
            )
        )
