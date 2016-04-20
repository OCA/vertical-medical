# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
import mock


mod_path = 'openerp.addons.website_sale.models.sale_order'


class TestWebsite(TransactionCase):

    def setUp(self):
        super(TestWebsite, self).setUp()
        self.patient_id = self.env['medical.patient'].create({
            'name': 'Test Patient',
            'partner_id': self.env.user.partner_id.id,
        })
        self.product_id = self.env['product.product'].create({
            'name': 'Insurance Product',
        })
        self.pricelist_id = self.env['product.pricelist'].create({
            'currency_id': self.env.ref('base.USD').id,
            'name': 'pricelist',
        })
        self.ins_co_id = self.env['medical.insurance.company'].create({
            'name': 'Test Insurance',
        })
        self.ins_temp_id = self.env['medical.insurance.template'].create({
            'name': 'Medical Insurance Plan',
            'plan_number': 'Plan #',
            'insurance_company_id': self.ins_co_id.id,
            'pricelist_id': self.pricelist_id.id,
            'product_id': self.product_id.id,
        })
        self.ins_plan_id = self.env['medical.insurance.plan'].create({
            'insurance_template_id': self.ins_temp_id.id,
            'patient_id': self.patient_id.id,
            'number': 'num',
            'plan_number': 'plan numb',
            'insurance_company_id': self.ins_co_id.id,
        })
        self.weblist_id = self.env['website_pricelist'].create({
            'website_id': self.env.ref('website.default_website').id,
            'pricelist_id': self.pricelist_id.id,
        })
        patient2_id = self.env['medical.patient'].create({
            'name': 'Test Patient',
        })
        self.pricelist2_id = self.env['product.pricelist'].create({
            'currency_id': self.env.ref('base.USD').id,
            'name': 'pricelist 2',
        })
        self.weblist2_id = self.env['website_pricelist'].create({
            'website_id': self.env.ref('website.default_website').id,
            'pricelist_id': self.pricelist2_id.id,
        })
        self.ins2_temp_id = self.env['medical.insurance.template'].create({
            'name': 'Medical Insurance Plan',
            'plan_number': 'Plan #',
            'insurance_company_id': self.ins_co_id.id,
            'pricelist_id': self.pricelist2_id.id,
            'product_id': self.product_id.id,
        })
        self.env['medical.insurance.plan'].create({
            'insurance_template_id': self.ins2_temp_id.id,
            'patient_id': patient2_id.id,
            'number': 'num',
            'plan_number': 'plan numb',
            'insurance_company_id': self.ins_co_id.id,
        })

    @mock.patch('%s.request' % mod_path)
    def test_website_sql_fetchall(self, req_mk):
        model_obj = self.env['website']
        with mock.patch.object(model_obj.env.cr, 'fetchall') as cr_mk:
            model_obj.get_pricelist_available()
            cr_mk.assert_called_once_with()

    @mock.patch('%s.request' % mod_path)
    def test_website_pricelist_template_computation_show(self, mk):
        self.assertIn(
            self.ins_temp_id,
            self.weblist_id.medical_insurance_template_ids,
            'Insurance template was not in medical_insurance_template_ids.'
            ' Expect %s, Got %s' % (
                self.ins_temp_id,
                self.weblist_id.medical_insurance_template_ids,
            )
        )

    @mock.patch('%s.request' % mod_path)
    def test_website_pricelist_template_computation_hide(self, mk):
        self.assertNotIn(
            self.ins2_temp_id,
            self.weblist_id.medical_insurance_template_ids,
            'Insurance template was in medical_insurance_template_ids.'
            ' Expect not include %s, Got %s' % (
                self.ins2_temp_id,
                self.weblist_id.medical_insurance_template_ids,
            )
        )
