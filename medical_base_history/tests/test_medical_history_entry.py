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


entry_mdl = 'openerp.addons.medical_base_history.models.medical_history_entry'


class TestMedicalHistoryEntry(TransactionCase):

    def setUp(self,):
        super(TestMedicalHistoryEntry, self).setUp()
        self.model_obj = self.env['medical.history.entry']
        self.entry_type_id = self.env['medical.history.type'].create({
            'name': 'Derped',
            'code': 'DERP',
            'old_cols_to_save': 'none',
            'new_cols_to_save': 'none',
        })
        self.record_id = self._test_record()
        self.vals = {
            'associated_model_id': self.record_id._model.id,
            'associated_record_id_int': self.record_id.id,
            'state': 'incomplete',
        }

    def _new_entry(self, ):
        return self.model_obj.new_entry(
            self.record_id, self.entry_type_id, self.vals,
        )

    def _history_action(self, ):
        return self.model_obj._do_history_action(
            self.record_id, self.vals
        )

    def _test_record(self, ):
        return self.env['medical.history.example'].create({
            'example_col': 'Test',
        })

    # Computes, inverses, defaults
    @mock.patch('%s.pickle' % entry_mdl)
    def test_compute_old_record_dict_calls_pickle_loads_with_rec(self, mk, ):
        self.entry_type_id.old_cols_to_save = 'all'
        rec_id = self._new_entry()
        rec_id.read('old_record_dict')
        mk.loads.assert_called_with(self.vals)

    @mock.patch('%s.pickle' % entry_mdl)
    def test_compute_old_record_dict_sets_property_to_pickle(self, mk, ):
        expect = 'Expect'
        mk.loads.return_value = expect
        self.entry_type_id.old_cols_to_save = 'all'
        rec_id = self._new_entry()
        got = rec_id.read('old_record_dict')
        self.assertEqual(
            expect, got,
        )

    @mock.patch('%s.pickle' % entry_mdl)
    def test_write_old_record_dict_calls_pickle_dumps_with_rec(self, mk, ):
        self.entry_type_id.new_cols_to_save = 'all'
        self._new_entry()
        mk.dumps.assert_called_with(self.vals)

    # @TODO: Figure out how to test attr assignment without triggering compute

    # Standard CRUD overloads
    def test_write_is_disabled_on_complete_records(self, ):
        rec_id = self._new_entry()
        rec_id.state = 'complete'
        with self.assertRaises(ValidationError):
            rec_id.write({'state': 'incomplete'})

    def test_unlink_is_disabled_on_all_records(self, ):
        rec_id = self._new_entry()
        with self.assertRaises(ValidationError):
            rec_id.write({'state': 'incomplete'})

    # Get associated record
    def test_get_associated_record_id_ensures_one(self, ):
        entry_ids = [self._new_entry(), self._new_entry()]
        with self.assertRaises(AssertionError):
            entry_ids.get_associated_record_id()

    def test_get_associacted_record_id_gets_model_obj(self, ):
        with mock.patch.object(self.model_obj, 'env') as mk:
            entry_id = self._new_entry()
            entry_id.get_associated_record_id()
            mk.__getitem__.called_once_with(self.record_id._name)

    def test_get_associated_record_id_browses_model_for_id(self, ):
        with mock.patch.object(self.model_obj, 'env') as mk:
            entry_id = self._new_entry()
            get_mk = mock.MagicMock()
            mk.__getitem__.return_value = get_mk
            entry_id.get_associated_record_id()
            get_mk.browse.called_once_with(self.record_id.id)

    def test_get_associated_record_id_returns_result_of_browse(self, ):
        with mock.patch.object(self.model_obj, 'env') as mk:
            entry_id = self._new_entry()
            expect = 'Expect'
            get_mk = mock.MagicMock()
            mk.__getitem__.return_value = get_mk
            get_mk.browse.return_value = expect
            result = entry_id.get_associated_record_id()
            self.assertEqual(expect, result)

    # Default History Actions
    def test_do_history_actions_gets_entry_type_model(self, ):
        with mock.patch.object(self.model_obj, 'env') as mk:
            with mock.patch.object(self.model_obj, 'get_changed_cols'):
                get_mk = mock.MagicMock()
                mk.__getitem__.return_value = get_mk
                self._history_action()
                get_mk.assert_called_once_with('medical.history.type')

    def test_do_history_actions_gets_entry_type_id(self, ):
        with mock.patch.object(self.model_obj, 'env') as mk:
            with mock.patch.object(self.model_obj, 'get_changed_cols'):
                get_mk = mock.MagicMock()
                mk.__getitem__.return_value = get_mk
                self._history_action()
                get_mk.browse().assert_called_once_with(
                    self.entry_type_id.id
                )

    def test_do_history_actions_calls_get_changed_cols_with_args(self, ):
        with mock.patch.object(self.model_obj, 'env'):
            with mock.patch.object(self.model_obj, 'get_changed_cols') as mk:
                self._history_action()
                mk.assert_called_with(self.record_id, self.vals)

    def test_do_history_actions_saved_old_changed_cols(self, ):
        self.entry_type_id.old_cols_to_save = 'changed'
        with mock.patch.object(self.model_obj, 'env'):
            with mock.patch.object(self.model_obj, 'get_changed_cols') as mk:
                expect = 'Expect'
                mk.return_value = expect
                vals = self._history_action()
                self.assertEqual(expect, vals['old_record_dict'])

    def test_do_history_actions_saved_old_all_cols(self, ):
        self.entry_type_id.old_cols_to_save = 'all'
        with mock.patch.object(self.model_obj, 'env'):
            expect = 'Expect'
            mk = mock.MagicMock()
            mk.read.return_value = expect
            self.record_id = mk
            self._history_action()
            mk.assert_called_once_with()

    def test_do_history_actions_saved_new_changed_cols(self, ):
        self.entry_type_id.new_cols_to_save = 'changed'
        with mock.patch.object(self.model_obj, 'env'):
            vals = self._history_action()
            self.assertDictEqual(self.vals, vals['new_record_dict'])

    # New Entry
    def test__new_entry_calls_do_history_actions_with_correct_params(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions') as mk:
            with mock.patch.object(self.model_obj, 'create'):
                self._new_entry()
                mk.assert_called_once_with(self.record_id, self.vals)

    def test__new_entry_updates_default_with_do_history_actions_return(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions') as mk:
            with mock.patch.object(self.model_obj, 'create') as cr_mk:
                expect = {'state': 'Should be injected', }
                mk.return_value = expect
                self._new_entry()
                call_args = cr_mk.call_args[0][0]
                self.assertEqual(
                    expect['state'], call_args.get('state'),
                )

    def test__new_entry_calls_create_with_entry_vals(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions'):
            with mock.patch.object(self.model_obj, 'create') as cr_mk:
                expect = {
                    'user_id': self.env.user,
                    'entry_type_id': self.entry_type_id.id,
                    'associated_model_id': self.record_id._model.id,
                    'associated_record_id_int': self.record_id.id,
                }
                self._new_entry()
                cr_mk.assert_called_with(expect)
