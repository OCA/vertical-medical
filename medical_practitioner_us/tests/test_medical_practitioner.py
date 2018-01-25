# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html)

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestMedicalPractitioner(TransactionCase):
    def setUp(self):
        super(TestMedicalPractitioner, self).setUp()

        self.model_obj = self.env['medical.practitioner']
        self.valid = [
            1538596788,
            1659779064,
        ]
        self.invalid = [
            1659779062,
            1538696788,
            4949558680,
        ]
        self.country_id = self.env['res.country'].search(
            [('code', '=', 'US')],
            limit=1,
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
