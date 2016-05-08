# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError


class TestMedicalPathology(TransactionCase):

    def setUp(self,):
        super(TestMedicalPathology, self).setUp()
        self.model_obj = self.env['medical.pathology']
        self.vals = {
            'name': 'Test Pathology',
            'code': 'TESTPATH',
        }
        self.record_id = self._test_record()

    def _test_record(self, ):
        return self.model_obj.create(self.vals)

    def test_check_unique_code(self, ):
        with self.assertRaises(IntegrityError):
            self._test_record()
