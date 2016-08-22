# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()

        self.line_model = self.env['medical.prescription.order.line']
        self.line = self.env.ref(
            'medical_prescription.' +
            'medical_prescription_order_line_patient_1_order_1_line_1'
        )

    def test_name_search_patient(self):
        recs = self.line_model.name_search(
            self.line.patient_id.name
        )
        self.assertEqual(
            2,
            len(recs),
            'Length of recs (%d) not equal to 2' % (len(recs)),
        )

    def test_name_search_medicament_name(self):
        recs = self.line_model.name_search(
            self.line.medicament_id.name
        )
        self.assertEqual(
            3,
            len(recs),
            'Length of recs (%d) not equal to 3' % (len(recs)),
        )

    def test_name_search_none(self):
        recs = self.line_model.name_search()
        self.assertEqual(
            3,
            len(recs),
            'Length of recs (%d) not equal to 3' % (len(recs)),
        )
