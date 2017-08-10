# -*- coding: utf-8 -*-
# Copyright 2016-2018 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPharmacy(TransactionCase):
    def setUp(self):
        super(TestMedicalPharmacy, self).setUp()

        self.partner_pharmacy_1 = self.env.ref(
            'medical_pharmacy.res_partner_pharmacy_1_demo'
        )

    def test_is_pharmacy(self):
        """It should set type to pharmacy on create"""
        self.assertEqual(
            self.partner_pharmacy_1.type,
            'medical.pharmacy',
        )

    def test_is_company(self):
        """Validate is_company is set to True on partner"""
        self.assertTrue(self.partner_pharmacy_1.is_company)

    def test_customer(self):
        """Test customer is set to False on partner"""
        self.assertFalse(self.partner_pharmacy_1.customer)
