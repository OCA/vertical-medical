# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestProductTemplate(TransactionCase):

    def setUp(self):
        super(TestProductTemplate, self).setUp()
        advil_ids = self.env['product.template'].search([
            ('name', '=', 'Advil')
        ])
        self.advil_ids = advil_ids.filtered(
            lambda r: r.display_name == 'Advil 3  - BAR'
        )

    def test_name_get(self):
        self.assertEqual(
            self.advil_ids[0].display_name,
            'Advil 3  - BAR',
            'Display name was not Advil 3  - BAR, it was %s' % (
                self.advil_ids[0].display_name
            )
        )
