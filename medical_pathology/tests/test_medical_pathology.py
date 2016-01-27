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
