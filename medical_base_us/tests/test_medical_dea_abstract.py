# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class MedicalDeaAbstractTestMixer(TransactionCase):

    def setUp(self, model_name='medical.abstract.dea'):
        super(MedicalDeaAbstractTestMixer, self).setUp()
        self.model_obj = self.env[model_name]
        self.valid = [
            'AP5836727',
        ]
        self.invalid = [
            'AP5836729',
        ]
        self.country_us = self.env['res.country'].search([
            ('code', '=', 'US'),
        ],
            limit=1,
        )


class TestMedicalDeaAbstract(MedicalDeaAbstractTestMixer):

    def test_valid(self):
        for i in self.valid:
            self.assertTrue(
                self.model_obj._dea_is_valid(i),
                'Luhn validity check on str %s did not pass for valid' % i,
            )

    def test_invalid(self):
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._dea_is_valid(i),
                'Luhn validity check on str %s did not fail for invalid' % i,
            )
