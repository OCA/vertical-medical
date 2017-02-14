# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from psycopg2 import IntegrityError
from openerp.tests.common import TransactionCase


class TestMedicalLeadWizard(TransactionCase):

    def setUp(self):
        super(TestMedicalLeadWizard, self).setUp()

        self.rx_order_9 = self.env.ref(
            'sale_crm_medical_prescription.'
            'medical_prescription_prescription_order_9'
        )
        self.rx_order_10 = self.env.ref(
            'sale_crm_medical_prescription.'
            'medical_prescription_prescription_order_10'
        )
        self.rx_line_10 = self.env.ref(
            'sale_crm_medical_prescription.'
            'medical_prescription_order_order_line_10'
        )
        self.rx_line_11 = self.env.ref(
            'sale_crm_medical_prescription.'
            'medical_prescription_order_order_line_11'
        )

        self.lead_1 = self.env.ref(
            'sale_crm_medical_prescription.'
            'crm_lead_medical_lead_1'
        )

        self.wizard_1 = self.env['medical.lead.wizard'].with_context(
            active_ids=[self.rx_line_10.id]
        ).create({})

        self.wizard_2 = self.env['medical.lead.wizard'].with_context(
            active_ids=[self.rx_line_10.id, self.rx_line_11.id]
        ).create({})

    def test_compute_default_session_no_rx_lines(self):
        """ Test no rx_lines in wizard raises integrity error """
        with self.assertRaises(IntegrityError):
            self.env['medical.lead.wizard'].create({})

    def test_compute_default_session_single_rx_line(self):
        """ Test single rx line properly extracted from context """
        exp = [self.rx_line_10.id]
        res = self.wizard_1.prescription_line_ids.ids
        self.assertEquals(
            res, exp,
        )

    def test_compute_default_session_multiple_rx_lines(self):
        """ Test mutliple rx lines properly extracted from context """
        exp = [self.rx_line_10.id, self.rx_line_11.id]
        res = sorted(self.wizard_2.prescription_line_ids.ids)
        self.assertEquals(
            res, exp,
        )

    def test_compute_default_pharmacy_single_rx_line(self):
        """ Test default pharmacy extracted from single rx_line context """
        exp = self.rx_line_10.prescription_order_id.partner_id
        res = self.wizard_1.pharmacy_id
        self.assertEquals(
            res, exp,
        )

    def test_compute_default_pharmacy_multiple_rx_lines(self):
        """ Test default pharmacy extracted from multiple rx_lines context """
        exp = self.rx_order_9.partner_id
        res = self.wizard_2.pharmacy_id
        self.assertEquals(
            res, exp,
        )

    def test_action_create_leads_crm_lead_attrs_name(self):
        """ Test crm lead name attr is correct """
        vals = self.wizard_2.action_create_leads()
        crm_lead_id = self.env['crm.lead'].browse(vals['res_ids'])

        exp = '%s, %s' % (
            self.rx_line_10.name, self.rx_line_11.name,
        )
        res = crm_lead_id.name
        self.assertEquals(
            res, exp
        )

    def test_action_create_leads_crm_lead_attrs(self):
        """ Test crm lead attrs are correct """
        vals = self.wizard_2.action_create_leads()
        crm_lead_id = self.env['crm.lead'].browse(vals['res_ids'])

        exp_keys = [
            'partner_id',
            'email_from',
            'phone',
            'pharmacy_id',
            'prescription_order_line_ids',
            'is_prescription',
        ]

        for key in exp_keys:
            res = getattr(crm_lead_id, key)
            exp = getattr(self.lead_1, key)
            self.assertEquals(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )

    def test_action_create_leads_return_values(self):
        """ Test values returned from action_create_leads are correct """
        vals = self.wizard_2.action_create_leads()
        crm_lead_ids = self.env['crm.lead'].browse(vals['res_ids'])

        form_id = self.env.ref('crm.crm_case_form_view_oppor')
        tree_id = self.env.ref('crm.crm_case_tree_view_oppor')
        action_id = self.env.ref('crm.crm_lead_action_activities')
        context = self.wizard_2._context.copy()

        exp_keys = {
            'name': action_id.name,
            'help': action_id.help,
            'type': action_id.type,
            'view_mode': 'tree',
            'views': [
                (tree_id.id, 'tree'), (form_id.id, 'form'),
            ],
            'target': 'current',
            'context': context,
            'res_model': action_id.res_model,
            'res_ids': crm_lead_ids.ids,
        }

        for key in exp_keys:
            res = vals[key]
            exp = exp_keys[key]
            self.assertEquals(
                res, exp,
                '\rKey: %s \rGot: %s \rExpected: %s' % (
                    key, res, exp
                )
            )
