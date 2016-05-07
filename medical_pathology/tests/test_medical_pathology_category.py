# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestMedicalPathologyCategory(TransactionCase):

    def setUp(self,):
        super(TestMedicalPathologyCategory, self).setUp()
        self.model_obj = self.env['medical.pathology.category']
        self.vals = {
            'name': 'Test Category',
        }
        self.record_id = self._test_record()

    def _test_record(self, ):
        return self.model_obj.create(self.vals)

    def test_check_recursive_parent(self, ):
        with self.assertRaises(ValidationError):
            new_record_id = self._test_record()
            new_record_id.parent_id = self.record_id.id
            self.record_id.parent_id = new_record_id.id
