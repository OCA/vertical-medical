# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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
            'associated_model_name': self.record_id._name,
            'associated_record_id_int': self.record_id.id,
            'state': 'incomplete',
        }

    def _new_entry(self, ):
        return self.model_obj.new_entry(
            self.record_id, self.entry_type_id, self.vals,
        )

    def _history_action(self, ):
        return self.model_obj._do_history_actions(
            self.record_id, self.entry_type_id, self.vals
        )

    def _test_record(self, ):
        return self.env['medical.history.example'].create({
            'example_col': 'Test',
        })

    # # Computes, inverses, defaults
    # @mock.patch('%s.pickle' % entry_mdl)
    # def test_compute_old_record_dict_calls_pickle_loads_with_rec(self, mk, ):
    #     self.entry_type_id.old_cols_to_save = 'all'
    #     rec_id = self._new_entry()
    #     self.model_obj.env.invalidate_all()
    #     rec_id.read(['old_record_dict'])
    #     mk.loads.assert_called_with(self.vals)
    #
    # @mock.patch('%s.pickle' % entry_mdl)
    # def test_compute_old_record_dict_sets_property_to_pickle(self, mk, ):
    #     expect = 'Expect'
    #     mk.loads.return_value = expect
    #     self.entry_type_id.old_cols_to_save = 'all'
    #     rec_id = self._new_entry()
    #     self.model_obj.env.invalidate_all()
    #     got = rec_id.old_record_dict
    #     self.assertEqual(
    #         expect, got,
    #     )
    #
    # @mock.patch('%s.pickle' % entry_mdl)
    # def test_write_old_record_dict_calls_pickle_dumps_with_rec(self, mk, ):
    #     self.entry_type_id.new_cols_to_save = 'all'
    #     self._new_entry()
    #     mk.dumps.assert_called_with(self.vals)

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
            rec_id.unlink()

    # Get associated record
    def test_get_associated_record_id_ensures_one(self, ):
        entry_ids = self._new_entry()
        entry_ids += self._new_entry()
        with self.assertRaises(ValueError):
            entry_ids.get_associated_record_id()

    def test_get_associated_record_id_browses_model_for_id(self, ):
        entry_id = self._new_entry()
        with mock.patch.object(self.model_obj, 'env') as mk:
            entry_id.get_associated_record_id()
            mk[self.record_id._name].browse.called_once_with(
                self.record_id.id
            )

    def test_get_associated_record_id_returns_result_of_browse(self, ):
        entry_id = self._new_entry()
        result = entry_id.get_associated_record_id()
        self.assertEqual(self.record_id.id, result.id)

    # Default History Actions
    def test_do_history_actions_calls_doesnt_call_get_changed_for_none(self, ):
        with mock.patch.object(self.model_obj, 'env'):
            with mock.patch.object(self.model_obj, 'get_changed_cols') as mk:
                self._history_action()
                mk.assert_not_called()

    def test_do_history_actions_calls_get_changed_cols_with_args(self, ):
        self.entry_type_id.old_cols_to_save = 'changed'
        with mock.patch.object(self.model_obj, 'env'):
            with mock.patch.object(self.model_obj, 'get_changed_cols') as mk:
                self._history_action()
                mk.assert_called_with(self.record_id, self.vals)

    def test_do_history_actions_saved_old_changed_cols(self, ):
        self.entry_type_id.old_cols_to_save = 'changed'
        with mock.patch.object(self.model_obj, 'get_changed_cols') as mk:
            expect = 'Expect'
            mk.return_value = expect
            vals = self._history_action()
            self.assertEqual(expect, vals.get('old_record_dict'))

    def test_do_history_actions_saved_old_all_cols(self, ):
        self.entry_type_id.old_cols_to_save = 'all'
        mk = mock.MagicMock()
        self.record_id = mk
        self._history_action()
        mk.read.assert_called_once_with()

    def test_do_history_actions_saved_new_changed_cols(self, ):
        self.entry_type_id.new_cols_to_save = 'changed'
        vals = self._history_action()
        self.assertDictEqual(self.vals, vals.get('new_record_dict'))

    # New Entry
    def test_new_entry_calls_do_history_actions_with_correct_params(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions') as mk:
            with mock.patch.object(self.model_obj, 'create'):
                self._new_entry()
                mk.assert_called_once_with(
                    self.record_id, self.entry_type_id, self.vals
                )

    def test_new_entry_updates_default_with_do_history_actions_return(self, ):
        with mock.patch.object(self.model_obj, '_do_history_actions') as mk:
            with mock.patch.object(self.model_obj, 'create') as cr_mk:
                expect = {'state': 'Should be injected', }
                mk.return_value = expect
                self._new_entry()
                call_args = cr_mk.call_args[0][0]
                self.assertEqual(
                    expect['state'], call_args.get('state'),
                )

    def test_new_entry_returns_new_entry_obj(self, ):
        rec_id = self._new_entry()
        expect = {
            'user_id': self.model_obj.env.user,
            'entry_type_id': self.entry_type_id,
            'associated_model_name': self.record_id._name,
            'associated_record_id_int': self.record_id.id,
        }
        for key, val in expect.items():
            self.assertEqual(
                getattr(rec_id, key), val
            )
