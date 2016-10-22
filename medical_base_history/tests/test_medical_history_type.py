# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


type_mdl = 'openerp.addons.medical_base_history.models.medical_history_type'


class TestMedicalHistoryType(TransactionCase):

    def setUp(self,):
        super(TestMedicalHistoryType, self).setUp()
        self.model_obj = self.env['medical.history.type']
        self.code = 'DERP'
        self.name = 'Derped'
        self.prefix = '#'
        self.suffix = '!'
        self.vals = {
            'name': self.name,
            'code': self.code,
            'old_cols_to_save': 'none',
            'new_cols_to_save': 'none',
            'prefix': self.prefix,
            'suffix': self.suffix,
        }

    def _new_type(self, ):
        return self.model_obj.create(self.vals)

    # Computes, contraints, etc
    def test_compute_display_name(self, ):
        expect = '[%(code)s] %(prefix)s%(name)s%(suffix)s' % {
            'code': self.code,
            'name': self.name,
            'prefix': self.prefix,
            'suffix': self.suffix,
        }
        self.assertEqual(
            expect, self._new_type().display_name
        )

    def test_check_unique_code(self, ):
        self._new_type()
        with self.assertRaises(ValidationError):
            self._new_type()

    # Getter methods
    def test_get_by_code(self, ):
        expect = self._new_type()
        got = self.model_obj.get_by_code(self.code)
        self.assertEqual(expect.id, got.id)

    def test_get_by_name_singleton(self, ):
        expect = self._new_type()
        got = self.model_obj.get_by_name(self.name)
        self.assertEqual(expect.id, got.id)

    def test_get_by_name_multiple(self, ):
        expect = [self._new_type().id]
        self.vals['code'] = 'dsfdfgrg'
        expect.append(self._new_type().id)
        got = self.model_obj.get_by_name(self.name)
        got = [g.id for g in got]
        self.assertListEqual(expect, got)
