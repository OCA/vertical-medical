# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalCenter(TransactionCase):

    def setUp(self):
        super(TestMedicalCenter, self).setUp()
        self.partner_center_1 = self.env.ref(
            'medical_center.partner_center_1'
        )
        self.medical_center_1 = self.env.ref(
            'medical_center.medical_center_1'
        )

    def test_is_center(self):
        """ It should set type to center on create """
        self.assertEqual(
            self.partner_center_1.type,
            'medical.center',
        )

    def test_is_company(self):
        """ Validate is_company is set to True on partner """
        self.assertTrue(
            self.partner_center_1.is_company,
        )

    def test_customer(self):
        """ Test customer is set to False on partner """
        self.assertFalse(
            self.partner_center_1.customer,
        )
