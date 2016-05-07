# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2016-TODAY LasLabs, Inc. [https://laslabs.com]
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


class TestMedicalDrugRoute(TransactionCase):

    def setUp(self, ):
        super(TestMedicalDrugRoute, self).setUp()
        self.model_obj = self.env['medical.drug.route']
        self.vals = {
            'name': 'DrugRoute',
            'code': 'DR',
        }

    def _test_record(self, ):
        return self.model_obj.create(self.vals)

    def test_name_unique(self, ):
        ''' Validate unique name sql constraint '''
        self._test_record()
        with self.assertRaises(IntegrityError):
            self.model_obj.create({
                'name': self.vals['name'],
            })
