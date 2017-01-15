# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.addons.base.res.res_partner import res_partner


class TestMedicalPharmacy(TransactionCase):

    def setUp(self):
        super(TestMedicalPharmacy, self).setUp()
        self.partner_pharmacy_1 = self.env.ref(
            'medical_pharmacy.partner_pharmacy_1'
        )
        self.medical_pharmacy_1 = self.env.ref(
            'medical_pharmacy.medical_pharmacy_1'
        )

    def test_is_pharmacy(self):
        """ Validate is_pharmacy is set to True on partner """
        self.assertTrue(
            self.partner_pharmacy_1.is_pharmacy,
        )

    def test_is_company(self):
        """ Validate is_company is set to True on partner """
        self.assertTrue(
            self.partner_pharmacy_1.is_company,
        )

    def test_customer(self):
        """ Test customer is set to False on partner """
        self.assertFalse(
            self.partner_pharmacy_1.customer,
        )
