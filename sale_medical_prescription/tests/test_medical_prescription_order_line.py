# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()
        self.rx_7 = self.env.ref(
            'sale_medical_prescription.'
            'medical_prescription_prescription_order_7'
        )
        self.rx_line_7 = self.env.ref(
            'sale_medical_prescription.'
            'medical_prescription_order_order_line_7'
        )

    def test_compute_orders(self):
        """ Test sale_order_ids properly computed """
        exp = self.rx_line_7.sale_order_line_ids.mapped('order_id').ids
        exp = sorted(set(exp))
        res = sorted(self.rx_line_7.sale_order_ids.ids)
        self.assertEqual(
            res, exp,
        )

    def test_default_name(self):
        """ Test name added to rx_line as default """
        self.assertTrue(self.rx_line_7.name)
