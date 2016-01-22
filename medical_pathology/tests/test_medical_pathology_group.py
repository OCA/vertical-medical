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
        with self.assertRaises(ValidationError):
            self._test_record()
