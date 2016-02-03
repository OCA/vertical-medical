# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: James Foster <jfoster@laslabs.com>
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


class TestMedicalPatient(TransactionCase):
    def setUp(self, ):
        super(TestMedicalPatient, self).setUp()
        vals = {
            'name': 'Patient 1',
            'gender': 'm',
            'dob': '1970-01-01'
        }
        self.patient_id = self.env['medical.patient'].create(vals)

    def test_name_includes_dob(self, ):
        self.assertEquals(
            self.patient_id.name_get()[0][1], 'Patient 1 01/01/1970',
            'Should display name and date of birth'
        )

    def test_name_without_dob(self, ):
        self.patient_id.write({'dob': None})
        self.patient_id.refresh()
        self.assertEquals(
            self.patient_id.name_get()[0][1], 'Patient 1',
            'Should display name and date of birth'
        )
