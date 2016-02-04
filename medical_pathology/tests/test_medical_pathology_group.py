# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError


class TestMedicalPathologyGroup(TransactionCase):

    def setUp(self,):
        super(TestMedicalPathologyGroup, self).setUp()
        self.model_obj = self.env['medical.pathology.group']
        self.vals = {
            'name': 'Test Group',
            'code': 'TESTGRP',
            'description': 'This is a test pathology group',
            'notes': 'Used in unit testing so we know our code doesn\tt suck',
        }
        self.record_id = self._test_record()

    def _test_record(self, ):
        return self.model_obj.create(self.vals)

    def test_check_unique_code(self, ):
        with self.assertRaises(IntegrityError):
            self._test_record()
