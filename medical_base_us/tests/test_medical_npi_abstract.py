# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MedicalNpiAbstractTestMixer(TransactionCase):

    def setUp(self, model_name='medical.abstract.npi'):
        super(MedicalNpiAbstractTestMixer, self).setUp()
        self.model_obj = self.env[model_name]
        self.valid = [
            1538596788,
            1659779064,
        ]
        self.invalid = [
            1659779062,
            1538696788,
            4949558680,
        ]
        self.country_us = self.env['res.country'].search([
            ('code', '=', 'US'),
        ],
            limit=1,
        )


class MedicalTestNpi(models.Model):
    _name = 'medical.test.npi'
    _inherit = 'medical.abstract.npi'
    ref = fields.Char()
    country_id = fields.Many2one('res.country')

    @api.multi
    @api.constrains('ref')
    def _check_ref(self):
        self._npi_constrains_helper('ref')


class TestMedicalNpiAbstract(MedicalNpiAbstractTestMixer):

    def test_valid_int(self):
        for i in self.valid:
            self.assertTrue(
                self.model_obj._npi_is_valid(i),
                'Npi validity check on int %s did not pass for valid' % i,
            )

    def test_valid_str(self):
        for i in self.valid:
            self.assertTrue(
                self.model_obj._npi_is_valid(str(i)),
                'Npi validity check on str %s did not pass for valid' % i,
            )

    def test_invalid_int(self):
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._npi_is_valid(i),
                'Npi validity check on int %s did not fail for invalid' % i,
            )

    def test_invalid_str(self):
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._npi_is_valid(str(i)),
                'Npi validity check on str %s did not fail for invalid' % i,
            )

    def test_constrain_valid_us(self):
        self.assertTrue(
            self.env['medical.test.npi'].create({
                'ref': self.valid[0],
                'country_id': self.country_us.id,
            })
        )

    def test_constrain_invalid_us(self):
        with self.assertRaises(ValidationError):
            self.env['medical.test.npi'].create({
                'ref': self.invalid[0],
                'country_id': self.country_us.id,
            })

    def test_constrain_invalid_non_us(self):
        self.assertTrue(
            self.env['medical.test.npi'].create({
                'ref': self.invalid[0],
                'country_id': self.country_us.id + 1,
            })
        )
