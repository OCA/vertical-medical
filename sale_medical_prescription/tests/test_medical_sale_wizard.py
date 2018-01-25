# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

import mock
from . import wizard_test_setup

NEXT_SALE = 'openerp.addons.sale_medical_prescription.wizards.' \
            'medical_sale_wizard.MedicalSaleWizard._get_next_sale_wizard'


class TestMedicalSaleWizard(wizard_test_setup.WizardTestSetup):

    def test_compute_default_session(self):
        """ Test rx lines properly extracted from context """
        exp = [self.rx_line_7.id, self.rx_line_8.id]
        res = sorted(self.wizard_2.prescription_line_ids.ids)
        self.assertEquals(
            res, exp,
        )

    def test_compute_default_pharmacy_single_rx_line(self):
        """ Test default pharmacy extracted from single rx_line context """
        exp = self.rx_line_7.prescription_order_id.partner_id
        res = self.wizard_1.pharmacy_id
        self.assertEquals(
            res, exp,
        )

    def test_compute_default_pharmacy_multiple_rx_lines(self):
        """ Test default pharmacy extracted from multiple rx_lines context """
        exp = self.rx_order_8.partner_id
        res = self.wizard_3.pharmacy_id
        self.assertEquals(
            res, exp,
        )

    def test_action_create_sale_wizards_orders(self):
        """ Test sale order fields properly populated from wizard """
        patient = self.rx_order_7.patient_id
        partner = patient.partner_id
        rx_order_names = self.rx_order_7.name

        exp_keys = {
            'partner_id': partner,
            'patient_id': patient,
            'pricelist_id': self.env.ref('product.list0'),
            'partner_invoice_id': partner,
            'partner_shipping_id': partner,
            'prescription_order_ids': self.rx_order_7,
            'pharmacy_id': self.rx_order_7.partner_id,
            'client_order_ref': rx_order_names,
            'date_order': self.order_date,
            'origin': rx_order_names,
            'user_id': self.env.user,
            'company_id': self.env.user.company_id,
        }
        self.wizard_2.action_create_sale_wizards()
        for key in exp_keys:
            exp = exp_keys[key]
            res = getattr(self.wizard_2.sale_wizard_ids[0], key)
            self.assertEquals(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )

    def test_action_create_sale_wizards_order_line(self):
        """ Test order line fields properly populated from wizard """
        simv_1 = self.env.ref(
            'sale_medical_prescription.product_product_simv_1'
        )
        exp_keys = {
            'product_id': simv_1,
            'product_uom': simv_1.uom_id,
            'product_uom_qty': self.rx_line_7.qty,
            'price_unit': simv_1.list_price,
            'prescription_order_line_id': self.rx_line_7,
        }
        self.wizard_1.action_create_sale_wizards()
        for key in exp_keys:
            exp = exp_keys[key]
            res = getattr(self.wizard_1.sale_wizard_ids[0].order_line[0], key)
            self.assertEquals(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )

    def test_action_create_sale_wizards_wizard_start(self):
        """ Test wizard state properly set to start after calling action """
        self.wizard_1.action_create_sale_wizards()
        self.assertEquals(
            'start', self.wizard_1.state,
        )

    def test_get_next_sale_wizard_not_in_states(self):
        """ Test returns False if none of sale_wizard_ids in only_states """
        self.wizard_1.action_create_sale_wizards()
        self.wizard_1.sale_wizard_ids[0].state = 'done'
        self.assertFalse(
            self.wizard_1._get_next_sale_wizard(['new'])
        )

    def test_get_next_sale_wizard(self):
        """ Test next wizard attrs correctly returned """
        self.wizard_1.action_create_sale_wizards()
        res_next_sale = self.wizard_1._get_next_sale_wizard()
        wizard = self.env.ref(
            'sale_medical_prescription.medical_sale_temp_view_form'
        )
        action = self.env.ref(
            'sale_medical_prescription.medical_sale_temp_action'
        )
        order_line = self.wizard_1.sale_wizard_ids[0]
        context = self.wizard_1._context.copy()
        context['active_id'] = order_line.id

        exp_keys = {
            'name': action.name,
            'help': action.help,
            'type': action.type,
            'target': 'new',
            'context': context,
            'res_model': action.res_model,
            'res_id': order_line.id,
        }
        self.assertEquals(
            res_next_sale['views'][0][0],
            wizard.id,
        )
        for key in exp_keys:
            res = res_next_sale[key]
            exp = exp_keys[key]
            self.assertEquals(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )

    @mock.patch(NEXT_SALE)
    def test_action_next_wizard_no_action(self, next_sale):
        """ Test wizard state properly set to done after calling action """
        next_sale.return_value = False
        self.wizard_1.action_create_sale_wizards()
        self.wizard_1.action_next_wizard()
        self.assertEquals(
            'done', self.wizard_1.state,
        )

    def test_action_rx_sale_conversions_sale_orders(self):
        """ Test real sale orders created properly """
        self.wizard_2.action_create_sale_wizards()
        self.wizard_2.action_next_wizard()
        res_action = self.wizard_2.action_rx_sale_conversions()
        sale_orders = self.env['sale.order'].browse(res_action['res_ids'])
        self.assertEquals(
            1, len(sale_orders),
        )

    def test_action_rx_sale_conversions_sale_order_line(self):
        """ Test real sale order lines created properly """
        self.wizard_2.action_create_sale_wizards()
        self.wizard_2.action_next_wizard()
        res_action = self.wizard_2.action_rx_sale_conversions()
        sale_orders = self.env['sale.order'].browse(res_action['res_ids'])
        self.assertEquals(
            2, len(sale_orders[0].order_line),
        )

    def test_action_rx_sale_conversions_return_attrs(self):
        """ Test dictionary returned is correct """
        self.wizard_1.action_create_sale_wizards()
        self.wizard_1.action_next_wizard()
        res_action = self.wizard_1.action_rx_sale_conversions()

        form = self.env.ref('sale.view_order_form')
        tree = self.env.ref('sale.view_quotation_tree')
        action = self.env.ref('sale.action_quotations')
        context = self.wizard_1._context.copy()
        exp_keys = {
            'name': action.name,
            'help': action.help,
            'type': action.type,
            'view_mode': 'tree',
            'view_id': tree.id,
            'target': 'current',
            'context': context,
            'res_model': action.res_model,
        }
        self.assertEquals(
            [tree.id, form.id],
            [
                res_action['views'][0][0],
                res_action['views'][1][0],
            ],
        )
        for key in exp_keys:
            res = res_action[key]
            exp = exp_keys[key]
            self.assertEquals(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )
