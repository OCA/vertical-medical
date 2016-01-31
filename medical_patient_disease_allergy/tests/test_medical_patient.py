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


class TestMedicalPatient(TransactionCase):
    def setUp(self, ):
        super(TestMedicalPatient, self).setUp()
        vals = {
            'name': 'Patient 1',
            'gender': 'm',
        }
        patient_id = self.env['medical.patient'].create(vals)
        vals = {
            'name': 'path_1',
            'code': 'path_1',
        }
        pathology_id = self.env['medical.pathology'].create(vals)
        vals = {
            'patient_id': patient_id.id,
            'pathology_id': pathology_id.id,
            'is_allergy': True,
        }
        self.disease_id = self.env['medical.patient.disease'].create(vals)

    def test_invalidate(self, ):
        self.assertTrue(
            self.disease_id.active,
            'Disease should be active before invalidation'
        )
        self.disease_id.patient_id.action_invalidate()
        self.assertFalse(
            self.disease_id.active,
            'Allergy should be inactive after invalidation'
        )
        self.assertFalse(
            self.disease_id.patient_id.active,
            'Patient should be inactive after invalidation'
        )

    def test_compute_allergy(self, ):
        self.assertEquals(
            self.disease_id.patient_id.count_allergy_ids, 1,
            'Should have one allergy'
        )
