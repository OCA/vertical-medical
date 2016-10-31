# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPrescriptionOrder(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrder, self).setUp()

        self.line_model = self.env['medical.prescription.order.line']
        self.line = self.env.ref(
            'medical_prescription.'
            'medical_prescription_order_line_patient_1_order_1_line_1'
        )

    def test_active_true(self):
        """ It should set active to true when rx line is active """
        self.assertTrue(
            self.line.prescription_order_id.active
        )

    def test_active_false(self):
        """ It should set active to true when rx line is active """
        order = self.line.prescription_order_id
        for line in order.prescription_order_line_ids:
            line.active = False
        self.assertFalse(
            self.line.prescription_order_id.active
        )
