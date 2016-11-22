# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()
        self.order_line_1 = self.env.ref(
            'medical_prescription.' +
            'medical_prescription_order_order_line_1'
        )

    def test_check_refill_qty_original(self):
        """ Test refill_qty_original cannot be less than 0 """
        with self.assertRaises(ValidationError):
            self.order_line_1.refill_qty_original = -1
