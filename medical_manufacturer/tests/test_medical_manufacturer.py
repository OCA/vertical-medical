# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalManufacturer(TransactionCase):

    def setUp(self):
        super(TestMedicalManufacturer, self).setUp()

        self.manufacturer_1 = self.env.ref(
            'medical_manufacturer.medical_manufacturer_1'
        )
        self.manufacturer_partner_1 = self.env.ref(
            'medical_manufacturer.partner_manufacturer_1'
        )

    def test_is_manufacturer(self):
        """ Validate is_manufacturer is set on partner """
        self.assertTrue(
            self.manufacturer_partner_1.is_manufacturer,
        )

    def test_is_customer(self):
        """ Validate is_customer is set on partner """
        self.assertFalse(
            self.manufacturer_partner_1.customer,
        )

    def test_is_company(self):
        """ Validate is_company is set on partner """
        self.assertTrue(
            self.manufacturer_partner_1.is_company,
        )
