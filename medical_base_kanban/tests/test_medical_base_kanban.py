# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import mock

from contextlib import contextmanager

from openerp.tests.common import TransactionCase


model = 'openerp.addons.medical_base_kanban.models.medical_base_kanban'


class TestMedicalBaseKanban(TransactionCase):

    def setUp(self):
        super(TestMedicalBaseKanban, self).setUp()
        self.model = self.env['medical.base.kanban.test']
        self.stage_id = self.env['medical.base.stage'].create({
            'name': 'stage',
            'res_model': self.model._name,
        })
        self.record_id = self.model.create({
            'stage_id': self.stage_id.id,
        })
        self.datetime = '2016-01-01 01:23:45'

    @contextmanager
    def mock_fields(self):
        """ It mocks fields import from model & overrides Datetime.now """
        with mock.patch('%s.fields' % model) as fields:
            fields.Datetime.now.return_value = self.datetime
            yield fields

    def reassign_record(self, user_id):
        self.record_id.write({
            'kanban_user_id': user_id.id
        })

    def test_compute_kanban_date_assign_initial_date(self):
        """ It should set date_assign on initial assignment """
        with self.mock_fields():
            self.reassign_record(self.env.ref('base.user_root'))
            self.assertEqual(
                self.datetime, self.record_id.kanban_date_assign,
            )

    def test_compute_kanban_date_assign_initial_history(self):
        """ It should set history on initial assignment """
        with self.mock_fields():
            self.reassign_record(self.env.ref('base.user_root'))
            self.assertEqual(
                self.env.ref('base.user_root'),
                self.record_id.kanban_assign_history_ids[0].user_id,
            )

    def test_compute_kanban_date_reassign_same_history(self):
        """ It should not set additional history on reassign to same user """
        with self.mock_fields():
            self.reassign_record(self.env.ref('base.user_root'))
            self.reassign_record(self.env.ref('base.user_root'))
            self.assertEqual(1, len(self.record_id.kanban_assign_history_ids))

    def test_compute_kanban_date_reassign_same_user(self):
        """ It should not set assign date on reassign to same user """
        with self.mock_fields() as fields:
            self.reassign_record(self.env.ref('base.user_root'))
            expect = '2016-02-01 00:00:00'
            fields.Datetime.now.return_value = expect
            self.reassign_record(self.env.ref('base.user_root'))
            self.assertNotEqual(expect, self.record_id.kanban_date_assign)

    def test_compute_kanban_date_reassign_history(self):
        """ It should set additional history on reassign to new user """
        with self.mock_fields():
            self.reassign_record(self.env.ref('base.user_root'))
            self.reassign_record(self.env.ref('base.user_demo'))
            self.assertEqual(
                self.env.ref('base.user_demo'),
                self.record_id.kanban_assign_history_ids[0].user_id,
            )

    def test_compute_kanban_date_reassign_new_user(self):
        """ It should set assign date on reassign to new user """
        with self.mock_fields() as fields:
            self.reassign_record(self.env.ref('base.user_root'))
            expect = '2016-02-01 00:00:00'
            fields.Datetime.now.return_value = expect
            self.reassign_record(self.env.ref('base.user_demo'))
            self.assertEqual(expect, self.record_id.kanban_date_assign)
