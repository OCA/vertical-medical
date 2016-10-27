# -*- coding: utf-8 -*-
# Copyright 2015 ACSONE SA/NV
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import mock
from openerp.addons.product.product import product_product
from openerp.tests.common import TransactionCase


class TestMedicalMedicament(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicament, self).setUp()
        self.medical_medicament_1 = self.env.ref(
            'medical_medicament.medical_medicament_advil_1'
        )
        self.product_product_1 = self.env.ref(
            'medical_medicament.product_product_advil_1'
        )

    def test_name_get_with_form_name(self):
        """ Test name_get with form name present """
        self.assertEquals(
            self.medical_medicament_1.display_name, 'Advil 0.2 g - CAP',
            'Should be the same age.\rGot: %s\rExpected: %s' % (
                self.medical_medicament_1.display_name, 'Advil 0.2 g - CAP'
            )
        )

    def test_name_get_no_form_name(self):
        """ Test name_get with no form present """
        self.medical_medicament_1.drug_form_id.name = ''
        self.assertEquals(
            self.medical_medicament_1.display_name, 'Advil 0.2 g',
            'Should be the same age.\rGot: %s\rExpected: %s' % (
                self.medical_medicament_1.display_name, 'Advil 0.2 g'
            )
        )

    def test_onchange_type(self):
        """ Test onchange_type is passed through to partner """
        with mock.patch.object(product_product, 'onchange_type') as mk:
            expect = 'Expect'
            self.medical_medicament_1.onchange_type(expect)
            mk.assert_called_once_with(expect)

    def test_onchange_uom(self):
        """ Test onchange_uom is passed through to partner """
        with mock.patch.object(product_product, 'onchange_uom') as mk:
            expect = 'Expect'
            self.medical_medicament_1.onchange_uom(expect, expect)
            mk.assert_called_once_with(expect, expect)

    def test_is_medicament(self):
        """ Test is_medicament is set to True """
        self.assertTrue(
            self.product_product_1.is_medicament,
            'Should be a medicament.\rGot: %s\rExpected: %s' % (
                self.product_product_1.is_medicament, True
            )
        )

    def test_get_by_product(self):
        """ Test returns correct medicament based on product_id given """
        res = self.medical_medicament_1.get_by_product(
            self.medical_medicament_1.product_id
        )
        self.assertEqual(
            self.medical_medicament_1.id, res.id,
            'Should be the same medicament id.\rGot: %s\rExpected: %s' % (
                self.medical_medicament_1.id, res.id
            )
        )
