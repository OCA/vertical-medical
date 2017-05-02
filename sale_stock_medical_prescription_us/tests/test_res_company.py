# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestResCompany(TransactionCase):

    def setUp(self):
        super(TestResCompany, self).setUp()
        self.company_1 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'company_pharmacy_us_2'
        )

    def test_refill_threshold_greater_than_1(self):
        """ Test raise validationerror if greater than 1 """
        with self.assertRaises(ValidationError):
            self.company_1.medical_prescription_refill_threshold = 1.1

    def test_refill_threshold_less_than_0(self):
        """ Test raise validationerror if less than 0 """
        with self.assertRaises(ValidationError):
            self.company_1.medical_prescription_refill_threshold = -1.1
