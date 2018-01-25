# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

import mock
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
            'Should be a pharmacy.\rGot: %s\rExpected: %s' % (
                self.partner_pharmacy_1.is_pharmacy, True
            )
        )

    def test_is_company(self):
        """ Validate is_company is set to True on partner """
        self.assertTrue(
            self.partner_pharmacy_1.is_company,
            'Should be a company.\rGot: %s\rExpected: %s' % (
                self.partner_pharmacy_1.is_company, True
            )
        )

    def test_customer(self):
        """ Test customer is set to False on partner """
        self.assertFalse(
            self.partner_pharmacy_1.customer,
            'Should not be a customer.\rGot: %s\rExpected: %s' % (
                self.partner_pharmacy_1.customer, False
            )
        )

    def test_onchange_state(self):
        """ Test onchange_state is passed through to partner """
        with mock.patch.object(res_partner, 'onchange_state') as mk:
            expect = 'Expect'
            self.medical_pharmacy_1.onchange_state(expect)
            mk.assert_called_once_with(expect)
