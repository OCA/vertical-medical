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

from openerp import fields
from openerp.tests.common import TransactionCase
import mock
import pickle


class TestMedicalHistoryEntry(TransactionCase):

    def setUp(self,):
        super(TestMedicalHistoryEntry, self).setUp()
        self.model_obj = self.env['medical.history.entry']
        self.entry_type_id = self.env['medical.history.type'].create({
            'name': 'Created',
            'code': 'CREATE',
            'old_cols_to_save': 'none',
            'new_cols_to_save': 'none',
        })
        self.record_id = self.test_record()
        self.vals = {
            'entry_type_id': self.record_id.id,
            'associated_model_id': self.record_id.model.id,
            'assocaited_record_id': self.record_id.id,
            'state': 'incomplete',
        }

    def new_entry(self, ):
        return self.model_obj.new_entry(
            self.record_id, self.entry_type_id, self.vals,
        )

    def test_record(self, ):
        return self.env['medical.history.example'].create({
            'example_col': 'Test',
        })

    # Computes, inverses, defaults
    def test_compute_old_record_dict(self, ):
        ''' Validate unpickle of old record '''
        self.entry_type_id.old_cols_to_save = 'all'
        rec_id = self.new_entry()
        rec_id.read()
        self.assertDictEqual(
            self.vals, rec_id.old_record_dict,
        )

    # New Entry
    def test_new_entry_calls_do_history_actions_with_correct_params(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions') as mk:
            with mock.patch.object(self.model_obj, 'create') as _:
                self.new_entry()
                mk.assert_called_once_with(self.record_id, vals)

    def test_new_entry_updates_default_with_do_history_actions_return(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions') as mk:
            with mock.patch.object(self.model_obj, 'create') as cr_mk:
                expect = {'state': 'Should be injected', }
                mk.return_value = expect
                self.new_entry()
                call_args = cr_mk.call_args[0][0]
                self.assertEqual(
                    expect['state'], call_args.get('state'),
                )

    def test_new_entry_calls_create_with_entry_vals(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions') as mk:
            with mock.patch.object(self.model_obj, 'create') as cr_mk:
                expect = {
                    'user_id': self.env.user,
                    'entry_type_id': self.entry_type_id.id,
                    'associated_model_id': self.record_id.model.id,
                    'associated_record_id_int': self.record_id.id,
                }
                self.new_entry()
                cr.mk_assert_called_with(expect)
        

