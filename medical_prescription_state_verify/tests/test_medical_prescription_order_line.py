# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()
        patient_id = self.env['medical.patient'].create({
            'name': 'Test Patient',
        })
        specialty_id = self.env['medical.specialty'].create({
            'name': 'Test Specialty',
        })
        physician_id = self.env['medical.physician'].create({
            'name': 'Test Physician',
            'specialty_id': specialty_id.id,
        })
        self.order_id = self.env['medical.prescription.order'].create({
            'patient_id': patient_id.id,
            'physician_id': physician_id.id,
        })
        product_id = self.env['product.product'].create({
            'name': 'Test Product',
        })
        drug_form_id = self.env['medical.drug.form'].create({
            'name': 'Test Drug Form',
        })
        medicament_id = self.env['medical.medicament'].create({
            'name': 'Test Medicament',
            'product_id': product_id.id,
            'drug_form_id': drug_form_id.id,
        })
        self.model_obj = self.env['medical.prescription.order.line']
        self.vals = {
            'prescription_order_id': self.order_id.id,
            'medicament_id': medicament_id.id,
            'patient_id': patient_id.id,
        }

    def _new_record(self):
        return self.model_obj.create(self.vals)

    def test_write_not_allowed_when_verified(self):
        record_id = self._new_record()
        self.order_id.state_type = 'verified'
        with self.assertRaises(ValidationError):
            record_id.write({'qty': 1, })

    def test_write_allowed_when_not_verified(self):
        record_id = self._new_record()
        self.order_id.state_type = 'cancel'
        record_id.write({'qty': 1, })
        record_id.refresh()
        self.assertEquals(1, record_id.qty)
