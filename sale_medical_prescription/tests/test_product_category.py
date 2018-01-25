# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestProductCategory(TransactionCase):

    def setUp(self):
        super(TestProductCategory, self).setUp()
        self.rx_categ = self.env.ref(
            'sale_medical_prescription.product_category_rx'
        )
        self.otc_categ = self.env.ref(
            'sale_medical_prescription.product_category_otc'
        )
        self.medicament_categ = self.env.ref(
            'sale_medical_prescription.product_category_medicament'
        )
        self.rx_descendant = self.env.ref(
            'sale_medical_prescription.product_category_test_rx_descendant'
        )
        self.rx_descendant_2 = self.env.ref(
            'sale_medical_prescription.product_category_test_rx_descendant_2'
        )

    def test_is_descendant_of_direct(self):
        """ Test category is direct child of rx category """
        self.assertTrue(
            self.rx_descendant._is_descendant_of(self.rx_categ),
        )

    def test_is_descendant_of_recurse(self):
        """ Test category is grandchild of rx category """
        self.assertTrue(
            self.rx_descendant_2._is_descendant_of(self.rx_categ),
        )

    def test_not_descendant_of_direct(self):
        """ Test category not child of rx category """
        self.assertFalse(
            self.medicament_categ._is_descendant_of(self.rx_categ),
        )

    def test_not_descendant_of_recurse(self):
        """ Test category not grandchild of rx category """
        self.assertFalse(
            self.otc_categ._is_descendant_of(self.rx_categ),
        )
