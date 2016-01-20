# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError
import mock


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
        expect.append(seof._new_type().id)
        got = self.model_obj.get_by_name(self.name)
        got = [g.id for g in got]
        self.assertListEqual(expect, got)
