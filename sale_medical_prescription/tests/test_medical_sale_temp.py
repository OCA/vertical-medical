# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from . import wizard_test_setup


class TestMedicalSaleTemp(wizard_test_setup.WizardTestSetup):

    def test_compute_line_cnt(self):
        """ Test line_cnt properly calculated """
        self.wizard_1.action_create_sale_wizards()
        self.assertEquals(
            self.wizard_1.sale_wizard_ids[0].line_cnt,
            1,
        )

    def test_compute_all_amounts(self):
        """ Test amount_untaxed is correctly calculated """
        self.wizard_2.action_create_sale_wizards()
        self.assertAlmostEqual(
            self.wizard_2.sale_wizard_ids[0].amount_untaxed,
            27.30,
        )

    def test_action_next_wizard(self):
        """ Test temp order state set to done when move to next wizard """
        self.wizard_1.action_create_sale_wizards()
        order = self.wizard_1.sale_wizard_ids[0]
        order.action_next_wizard()
        self.assertEquals(
            order.state,
            'done',
        )

    def test_to_vals(self):
        """ Test attributes of real order is similar to temp order """
        self.wizard_1.action_create_sale_wizards()
        self.wizard_1.action_next_wizard()
        res_conversions = self.wizard_1.action_rx_sale_conversions()

        order_1 = self.env['sale.order'].browse(res_conversions['res_ids'][0])
        temp_order_1 = self.wizard_1.sale_wizard_ids[0]
        temp_order_vals = temp_order_1._to_vals()

        comparison_keys = [
            'state',
            'origin',
            'note',
            'client_order_ref',
            'user_id',
            'company_id',
            'partner_id',
            'partner_invoice_id',
            'partner_shipping_id',
            'pricelist_id',
            'pharmacy_id',
            'team_id',
        ]
        self.assertEqual(
            sorted(order_1.prescription_order_ids.ids),
            [temp_order_vals['prescription_order_ids'][0][1]],
        )
        for index, key in enumerate(comparison_keys):
            res = getattr(order_1, key)
            if index >= 4:
                res = res.id
            exp = temp_order_vals[key]
            self.assertEqual(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )
