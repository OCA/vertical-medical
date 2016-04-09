# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp import models, fields, api
from openerp.exceptions import ValidationError


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


class MedicalTestDea(models.Model):
    _name = 'medical.test.dea'
    _inherit = 'medical.abstract.dea'
    ref = fields.Char()
    country_id = fields.Many2one('res.country')

    @api.multi
    @api.constrains('ref')
    def _check_ref(self):
        self._dea_constrains_helper('ref')


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

    def test_constrain_valid_us(self):
        self.assertTrue(
            self.env['medical.test.dea'].create({
                'ref': self.valid[0],
                'country_id': self.country_us.id,
            })
        )

    def test_constrain_invalid_us(self):
        with self.assertRaises(ValidationError):
            self.env['medical.test.dea'].create({
                'ref': self.invalid[0],
                'country_id': self.country_us.id,
            })

    def test_constrain_invalid_non_us(self):
        self.assertTrue(
            self.env['medical.test.dea'].create({
                'ref': self.invalid[0],
                'country_id': self.country_us.id + 1,
            })
        )
