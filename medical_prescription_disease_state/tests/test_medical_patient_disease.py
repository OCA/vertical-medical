# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPatientDisease(TransactionCase):

    def setUp(self):
        super(TestMedicalPatientDisease, self).setUp()
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

    def test_count_prescription_order_lines(self, ):
        self._new_record()
        self.assertEqual(
            self.disease_id.count_prescription_order_lines, 1
        )

    def test_last_prescription_order_line(self, ):
        line_1 = self._new_record()
        line_2 = self.env['medical.prescription.order.line'].create({
            'disease_id': self.disease_id.id,
            'medicament_id': self.medicament_id.id,
            'prescription_order_id': self.rx_id.id,
            'patient_id': self.patient_id.id,
            'physician_id': self.physician_id.id,
        })
        line_1.date_start_treatment = '2016-01-01 00:00:00'
        line_2.date_start_treatment = '2016-02-01 00:00:00'
        self.assertEqual(
            self.disease_id.last_prescription_order_line_id.id, line_2.id
        )

    def test_last_prescription_order_line_active(self, ):
        line_id = self._new_record()
        line_id.date_stop_treatment = '1970-01-01 00:00:00'
        self.assertEqual(
            self.disease_id.last_prescription_order_line_active, False
        )
