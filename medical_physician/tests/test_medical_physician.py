# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Ken Mak <kmak@laslabs.com>
#    Copyright: 2014-2016 LasLabs, Inc. [https://laslabs.com]
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


class TestMedicalPhysician(TransactionCase):

    def setUp(self, ):
        super(TestMedicalPhysician, self).setUp()
        vals = {
            'name': 'Test Specialty',
            'code': 'TS',
        }
        specialty_id = self.env['medical.specialty'].create(vals)
        vals = {
            'name': 'Test Physician',
            'specialty_id': specialty_id.id,
        }
        self.physician_id = self.env['medical.physician'].create(vals)

    def test_create(self, ):
        self.assertTrue(self.physician_id.partner_id.is_doctor)
