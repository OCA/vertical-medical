# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestProductProduct(TransactionCase):

    def setUp(self):
        super(TestProductProduct, self).setUp()
        self.advil_id = self.env.ref(
            'medical_medicament.product_product_advil_1',
        ).product_tmpl_id

    def test_name_get(self):
        self.assertEqual(
            self.advil_id.display_name,
            'Advil 0.2 g - CAP',
        )
