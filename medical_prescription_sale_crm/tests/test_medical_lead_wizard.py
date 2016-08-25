# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from psycopg2 import IntegrityError
from openerp.tests.common import TransactionCase


class TestMedicalLeadWizard(TransactionCase):

    def _create_first_order_line(self):
        self.pharmacy_1 = self.env['medical.pharmacy'].create({
            'name': 'Test Pharmacy',
        })
        self.patient = self.env['medical.patient'].create({
            'name': 'Test Patient',
        })
        self.physician = self.env['medical.physician'].create({
            'name': 'Test Physician',
        })
        drug_form = self.env['medical.drug.form'].create({
            'name': 'Test'
        })
        self.medicament = self.env['medical.medicament'].create({
            'name': 'Test Medicament',
            'drug_form_id': drug_form.id,
        })
        order_1 = self.env['medical.prescription.order'].create({
            'name': 'Test Order 1',
            'partner_id': self.pharmacy_1.id,
            'patient_id': self.patient.id,
            'physician_id': self.physician.id,
        })
        self.line_1 = self.env['medical.prescription.order.line'].create({
            'name': 'Test Order Line 1',
            'prescription_order_id': order_1.id,
            'medicament_id': self.medicament.id,
            'patient_id': order_1.patient_id.id,
        })

    def _create_second_order_line(self):
        self.pharmacy_2 = self.env['medical.pharmacy'].create({
            'name': 'Test Pharmacy',
        })
        order_2 = self.env['medical.prescription.order'].create({
            'name': 'Test Order 2',
            'partner_id': self.pharmacy_2.id,
            'patient_id': self.patient.id,
            'physician_id': self.physician.id,
        })
        self.line_2 = self.env['medical.prescription.order.line'].create({
            'name': 'Test Order Line 2',
            'prescription_order_id': order_2.id,
            'medicament_id': self.medicament.id,
            'patient_id': order_2.patient_id.id,
        })

    def test_default_pharmacy_no_order_lines(self):
        with self.assertRaises(IntegrityError):
            self.env['medical.lead.wizard'].create({})

    def test_default_pharmacy_single_order_line(self):
        self._create_first_order_line()
        wizard = self.env['medical.lead.wizard'].with_context(
            active_ids=[self.line_1.id],
        ).create({})

        self.assertEqual(wizard.pharmacy_id, self.pharmacy_1)

    def test_default_pharmacy_multiple_order_lines(self):
        self._create_first_order_line()
        self._create_second_order_line()
        wizard = self.env['medical.lead.wizard'].with_context(
            active_ids=[self.line_1.id, self.line_2.id],
        ).create({})

        self.assertIn(wizard.pharmacy_id, [self.pharmacy_1, self.pharmacy_2])

    def test_default_session_single_order_line(self):
        self._create_first_order_line()
        wizard = self.env['medical.lead.wizard'].with_context(
            active_ids=[self.line_1.id],
        ).create({})

        self.assertEqual(wizard.prescription_line_ids, self.line_1)

    def test_default_session_multiple_order_lines(self):
        self._create_first_order_line()
        self._create_second_order_line()
        wizard = self.env['medical.lead.wizard'].with_context(
            active_ids=[self.line_1.id, self.line_2.id],
        ).create({})

        self.assertEqual(
            wizard.prescription_line_ids,
            self.line_1 + self.line_2,
        )
