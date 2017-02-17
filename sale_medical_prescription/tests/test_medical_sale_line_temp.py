# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from . import wizard_test_setup


class TestMedicalSaleLineTemp(wizard_test_setup.WizardTestSetup):

    def test_compute_all_amounts(self):
        """ Test subtotal calculated correctly """
        self.wizard_1.action_create_sale_wizards()
        order_line = self.wizard_1.sale_wizard_ids[0].order_line[0]
        res = order_line.price_subtotal
        exp = order_line.product_uom_qty * order_line.price_unit
        self.assertEqual(
            res, exp,
        )

    def test_to_vals_order_line_name(self):
        """ Test order_line name is correct """
        self.wizard_1.action_create_sale_wizards()
        self.wizard_1.action_next_wizard()
        res_conversions = self.wizard_1.action_rx_sale_conversions()

        order_1 = self.env['sale.order'].browse(res_conversions['res_ids'][0])
        order_line_1 = order_1.order_line[0]

        exp_name = '%s - %s' % (
            self.rx_order_7.name,
            self.line_7.product_id.display_name,
        )
        self.assertEquals(
            order_line_1.name,
            exp_name,
        )

    def test_to_vals(self):
        """ Test real order_line similar to temp order_line """
        self.wizard_1.action_create_sale_wizards()
        self.wizard_1.action_next_wizard()
        res_conversions = self.wizard_1.action_rx_sale_conversions()

        order_1 = self.env['sale.order'].browse(res_conversions['res_ids'][0])
        line_1 = order_1.order_line[0]

        temp_order_1 = self.wizard_1.sale_wizard_ids[0]
        temp_order_line_1 = temp_order_1.order_line[0]
        temp_order_line_vals = temp_order_line_1._to_vals()

        comparison_keys = [
            'sequence',
            'product_uom_qty',
            'state',
            'price_unit',
            'product_id',
            'product_uom',
            'prescription_order_line_id'
        ]
        for index, key in enumerate(comparison_keys):
            res = getattr(line_1, key)
            if index >= 4:
                res = res.id
            exp = temp_order_line_vals[key]
            self.assertEqual(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )
