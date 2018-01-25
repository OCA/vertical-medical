# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tests.common import SingleTransactionCase


class MedicalTestDea(models.Model):
    _name = 'medical.test.dea'
    _inherit = 'medical.abstract.dea'
    ref = fields.Char()
    country_id = fields.Many2one('res.country')

    @api.multi
    @api.constrains('ref')
    def _check_ref(self):
        self._dea_constrains_helper('ref')


class MedicalDeaAbstractTestMixer(SingleTransactionCase):

    @classmethod
    def setUpClass(cls):
        super(MedicalDeaAbstractTestMixer, cls).setUpClass()

        cls.registry.enter_test_mode()
        cls.old_cursor = cls.cr
        cls.cr = cls.registry.cursor()
        cls.env = api.Environment(cls.cr, cls.uid, {})

        MedicalTestDea._build_model(cls.registry, cls.cr)
        cls.model_obj = cls.env[MedicalTestDea._name].with_context(todo=[])
        cls.model_obj._prepare_setup()
        cls.model_obj._setup_base(partial=False)
        cls.model_obj._setup_fields(partial=False)
        cls.model_obj._setup_complete()
        cls.model_obj._auto_init()
        cls.model_obj.init()
        cls.model_obj._auto_end()

        cls.valid = [
            'AP5836727',
        ]
        cls.invalid = [
            'AP5836729',
            'Invalid00',
        ]
        cls.country_us = cls.env['res.country'].search([
            ('code', '=', 'US'),
        ],
            limit=1,
        )

    @classmethod
    def tearDownClass(cls):
        del cls.registry.models[MedicalTestDea._name]
        cls.registry.leave_test_mode()
        cls.cr = cls.old_cursor
        cls.env = api.Environment(cls.cr, cls.uid, {})

        super(MedicalDeaAbstractTestMixer, cls).tearDownClass()


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
