# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests.common import TransactionCase
from openerp import api, fields, models
from openerp.exceptions import ValidationError


class MedicalDeaAbstractTestMixer(TransactionCase):

    def setUp(self):
        super(MedicalDeaAbstractTestMixer, self).setUp()

        MedicalTestDea._build_model(self.registry, self.cr)
        self.model_obj = self.env[MedicalTestDea._name]
        self.model_obj._prepare_setup()
        self.model_obj._setup_base(False)
        self.model_obj._setup_fields(False)
        self.model_obj._setup_complete()

        self.valid = [
            'AP5836727',
        ]
        self.invalid = [
            'AP5836729',
            'Invalid00',
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
        """ Test _dea_is_valid returns True if valid str input """
        for i in self.valid:
            self.assertTrue(
                self.model_obj._dea_is_valid(i),
                'DEA validity check on str %s did not pass for valid' % i,
            )

    def test_invalid(self):
        """ Test _dea_is_valid returns False if invalid str input """
        for i in self.invalid:
            self.assertFalse(
                self.model_obj._dea_is_valid(i),
                'DEA validity check on str %s did not fail for invalid' % i,
            )

    def test_false(self):
        """ Test _dea_is_valid fails gracefully if given no/Falsey data """
        self.assertFalse(
            self.model_obj._dea_is_valid(False),
            'DEA validity check on False did not fail gracefully',
        )

    def test_constrain_valid_us(self):
        """ Test _dea_constrains_helper no ValidationError if valid ref """
        test_model = self.env['medical.test.dea'].new({
            'ref': self.valid[0],
            'country_id': self.country_us.id,
        })

        try:
            test_model._check_ref()
        except ValidationError:
            self.fail('A ValidationError was raised and should not have been.')

    def test_constrain_invalid_us(self):
        """ Test _dea_constrains_helper raise ValidationError invalid ref """
        test_model = self.env['medical.test.dea'].new({
            'ref': self.invalid[0],
            'country_id': self.country_us.id,
        })

        with self.assertRaises(ValidationError):
            test_model._check_ref()

    def test_constrain_invalid_non_us(self):
        """ Test _dea_constrains_helper skips validation if not US """
        test_model = self.env['medical.test.dea'].new({
            'ref': self.invalid[0],
            'country_id': self.country_us.id + 1,
        })

        try:
            test_model._check_ref()
        except ValidationError:
            self.fail('A ValidationError was raised and should not have been.')
