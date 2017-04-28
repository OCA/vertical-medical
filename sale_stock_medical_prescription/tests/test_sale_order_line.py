# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestSaleOrderLine(TransactionCase):

    def setUp(self):
        super(TestSaleOrderLine, self).setUp()

        self.order_line_12 = self.env.ref(
            'sale_stock_medical_prescription.sale_order_medical_order_line_12'
        )
        self.order_line_13 = self.env.ref(
            'sale_stock_medical_prescription.sale_order_medical_order_line_13'
        )
        self.rx_line_12 = self.env.ref(
            'sale_stock_medical_prescription.'
            'medical_prescription_order_order_line_12'
        )
        self.amoxicillin = self.env.ref(
            'sale_stock_medical_prescription.medical_medicament_amoxicillin_1'
        )

    def test_compute_dispense_qty_no_rx_line(self):
        """ Test returns False if no rx_line tied to sale_order_line """
        self.order_line_12.prescription_order_line_id = None
        self.assertFalse(
            self.order_line_12._compute_dispense_qty()
        )
        self.assertEquals(
            self.order_line_12.dispense_qty,
            0.0,
        )

    def test_check_can_dispense_dispense_qty(self):
        """ Test ValidationError dispense_qty greater than can_dispense_qty """
        with self.assertRaises(ValidationError):
            self.order_line_13.dispense_qty = 18

    def test_check_product_with_context(self):
        """ Test returns true if rx_force in context """
        self.assertTrue(
            self.order_line_12.with_context(
                {'__rx_force__': True})._check_product()
        )

    def test_check_can_dispense_with_context(self):
        """ Test returns true if rx_force in context """
        self.assertTrue(
            self.order_line_12.with_context(
                {'__rx_force__': True})._check_can_dispense()
        )

    def test_compute_dispense_qty_same_uom(self):
        """ Test sets dispense_qty to product qty if same uom as rx_line """
        self.assertEquals(
            self.order_line_12.dispense_qty,
            self.order_line_12.product_uom_qty,
        )

    def test_compute_dispense_qty_different_uom(self):
        """ Test converts dispense_qty if different uom as rx_line """
        dozen = self.env.ref('product.product_uom_dozen')
        self.order_line_13.product_uom = dozen
        self.assertEquals(
            self.order_line_13.dispense_qty,
            self.order_line_13.product_uom_qty * 12,
        )

    def test_check_product(self):
        """ Test changing product to incorrect one raise ValidationError """
        product = self.env['product.product'].search([
            ('id', '!=', self.order_line_12.product_id.id)
        ], limit=1)
        with self.assertRaises(ValidationError):
            self.order_line_12.product_id = product.id

    def test_check_can_dispense_false(self):
        """ Test raise ValidationError if try to dispense but cannot """
        with self.assertRaises(ValidationError):
            self.order_line_12._check_can_dispense()

    def test_check_can_dispense_conditions_all_true(self):
        """ Test no Validation Errors if NOT all conditions True """
        self.order_line_12.product_id.is_medicament = False
        try:
            self.order_line_12._check_can_dispense()
            self.assertTrue(True)
        except ValidationError:
            self.fail()

    def test_check_can_dispense_qty_greater_than_rx_line_can_dispense(self):
        """ Test raise ValidationError if try dispense but not enough stock """
        self.order_line_13.product_uom_qty = 1000
        with self.assertRaises(ValidationError):
            self.order_line_13._check_can_dispense()

    def test_prepare_order_line_procurement_otc(self):
        """ It should not throw an error and should assign OTC route """
        self.amoxicillin.is_prescription = False
        res = self.order_line_12._prepare_order_line_procurement()
        expect = self.env.ref(
            'sale_stock_medical_prescription.route_warehouse0_otc'
        )
        res = res['route_ids'][0][2]
        self.assertEquals(
            [expect.id], res,
            'Did not correctly assign route. Expect %s, Got %s' % (
                [expect.id], res
            )
        )

    def test_prepare_order_line_procurement_prescription(self):
        """ It should not throw an error and should assign RX route """
        res = self.order_line_12._prepare_order_line_procurement()
        expect = self.env.ref(
            'sale_stock_medical_prescription.route_warehouse0_prescription'
        )
        res = res['route_ids'][0][2]
        self.assertEquals(
            [expect.id], res,
            'Did not correctly assign route. Expect %s, Got %s' % (
                [expect.id], res
            )
        )

    def test_check_can_dispense_no_order_lines(self):
        """ Test Validations skipped if no prescription lines present """
        try:
            self.order_line_12.prescription_order_line_id = None
            self.assertTrue(True)
        except ValidationError:
            self.fail(
                'Should skip validations if no rx_line.'
            )
