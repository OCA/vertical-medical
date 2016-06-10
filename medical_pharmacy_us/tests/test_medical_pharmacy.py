# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestMedicalPharmacy(TransactionCase):

    def setUp(self,):
        super(TestMedicalPharmacy, self).setUp()
        self.model_obj = self.env['medical.pharmacy']
        self.valid = [
            1538596788,
            1659779064,
        ]
        self.invalid = [
            1659779062,
            1538696788,
            4949558680,
        ]
        self.country_id = self.env['res.country'].search([
            ('code', '=', 'US'),
        ],
            limit=1
        )

    def _new_record(self, npi_num, country_id=None):
        if not country_id:
            country_id = self.country_id
        return self.model_obj.create({
            'name': 'Test Partner',
            'npi_num': npi_num,
            'country_id': country_id.id,
        })

    def test_valid_int(self):
        for i in self.valid:
            self.assertTrue(self._new_record(i))

    def test_valid_str(self):
        for i in self.valid:
            self.assertTrue(self._new_record(str(i)))

    def test_invalid_int(self):
        for i in self.invalid:
            with self.assertRaises(ValidationError):
                self._new_record(i)

    def test_invalid_str(self):
        for i in self.invalid:
            with self.assertRaises(ValidationError):
                self._new_record(i)

    def test_invalid_but_not_us(self):
        country_id = self.env['res.country'].search([
            ('code', '!=', 'US'),
        ],
            limit=1,
        )
        for i in self.invalid:
            self.assertTrue(self._new_record(i, country_id))
