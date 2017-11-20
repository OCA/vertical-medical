# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.exceptions import ValidationError
from odoo.tests import TransactionCase


class TestMedication(TransactionCase):
    def setUp(self):
        super(TestMedication, self).setUp()
        self.product_obj = self.env['product.template']
        self.sct_obj = self.env['medical.sct.concept']
        self.sct_code = self.sct_obj.search(
            [('is_medication_code', '=', True)], limit=1)
        self.sct_obj = self.env['medical.sct.concept']
        self.atc_code = self.env['medical.atc.concept'].search(
            [('parent_id', '!=', False)], limit=1)
        self.form = self.sct_obj.search([('is_medication_form', '=', True)],
                                        limit=1)
        self.vals = {
            'name': 'Name',
            'type': 'consu',
            'is_medication': True,
            'form_id': self.form.id,
            'sct_code_id': self.sct_code.id,
            'atc_code_id': self.atc_code.id
        }

    def test_codification(self):
        product = self.product_obj.create(self.vals)
        self.assertTrue(product.is_medication)

    def test_constrains(self):
        self.vals['type'] = 'service'
        with self.assertRaises(ValidationError):
            self.product_obj.create(self.vals)
