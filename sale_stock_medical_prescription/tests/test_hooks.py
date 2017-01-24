# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestHooks(TransactionCase):

    def setUp(self):
        super(TestHooks, self).setUp()
        self.rx_line_13 = self.env.ref(
            'sale_stock_medical_prescription.'
            'medical_prescription_order_order_line_13'
        )
        self.medicament_amox_1 = self.env.ref(
            'sale_stock_medical_prescription.'
            'product_product_amoxicillin_1'
        )

    def test_post_init_medicament(self):
        """ It should convert pre-existing medicaments to new type """
        self.assertEqual(
            self.medicament_amox_1.type,
            'product',
        )
