# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()
        self.rx_line_us_1 = self.env.ref(
            'medical_prescription_us.' +
            'medical_prescription_order_order_line_us_1'
        )
        self.rx_line_us_2 = self.env.ref(
            'medical_prescription_us.' +
            'medical_prescription_order_order_line_us_2'
        )

    def test_check_refill_qty_original(self):
        """ Test refill_qty_original cannot be less than 0 """
        with self.assertRaises(ValidationError):
            self.rx_line_us_1.refill_qty_original = -1

    def test_create_date_stop_treatment(self):
        """ Test date_stop_treatment properly calculated """
        self.assertEquals(
            self.rx_line_us_1.date_stop_treatment,
            '1983-07-20 00:00:00',
        )
