# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestSaleOrder(TransactionCase):

    def setUp(self):
        super(TestSaleOrder, self).setUp()
        self.sale_7 = self.env.ref(
            'sale_medical_prescription.sale_order_medical_order_7'
        )

    def test_compute_patient_ids(self):
        """ Test patient_ids properly computed """
        exp = self.sale_7.order_line.mapped('patient_id').ids
        exp = sorted(set(exp))
        res = sorted(self.sale_7.patient_ids.ids)
        self.assertEqual(
            res, exp,
        )

    def test_compute_prescription_order_ids(self):
        """ Test rx orders properly computed """
        exp = self.sale_7.order_line.mapped(
            'prescription_order_line_id.prescription_order_id'
        ).ids
        exp = sorted(set(exp))
        res = sorted(self.sale_7.prescription_order_ids.ids)
        self.assertEqual(
            res, exp,
        )

    def test_compute_prescription_order_line_ids(self):
        """ Test rx_lines properly computed """
        exp = self.sale_7.order_line.mapped('prescription_order_line_id').ids
        exp = sorted(set(exp))
        res = sorted(self.sale_7.prescription_order_line_ids.ids)
        self.assertEqual(
            res, exp,
        )
