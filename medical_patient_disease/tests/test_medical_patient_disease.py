# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical, an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical is free software:
#     you can redistribute it and/or
#     modify it under the terms of the GNU Affero General Public License
#     as published by the Free Software Foundation, either version 3 of
#     the License, or (at your option) any later version.
#
#     medical is distributed in the hope that it will
#     be useful but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the
#     GNU Affero General Public License
#     along with medical.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tests.common import TransactionCase


class TestMedicalPatientDisease(TransactionCase):

    def setUp(self):
        super(TestMedicalPatientDisease, self).setUp()
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
        }
        self.disease_id = self.env['medical.patient.disease'].create(vals)

    def test_name(self):
        short_comment = 'test'
        self.disease_id.short_comment = short_comment
        computed_name = '%s - %s' % (
            self.disease_id.pathology_id.name,
            short_comment,
        )
        self.assertEquals(
            self.disease_id.name,
            computed_name,
            'Disease name and computed name should be same.'
            ' Expect %s Got %s' % (
                self.disease_id.name,
                computed_name
            )
        )

    def test_invalidate(self):
        self.assertTrue(
            self.disease_id.active,
            'Disease should be active before invalidation'
        )
        self.disease_id.patient_id.action_invalidate()
        self.assertFalse(
            self.disease_id.active,
            'Disease should be inactive after invalidation'
        )
        self.assertFalse(
            self.disease_id.patient_id.active,
            'Patient should be inactive after invalidation'
        )

    def test_revalidate(self):
        self.disease_id.active = False
        self.disease_id.patient_id.active = False
        self.disease_id.patient_id.action_revalidate()
        self.assertTrue(
            self.disease_id.patient_id.active,
            'Patient should be active after revalidation'
        )
        self.assertTrue(
            self.disease_id.active,
            'Disease should be active after revalidation'
        )

    def test_compute_disease(self):
        self.assertEquals(
            self.disease_id.patient_id.count_disease_ids, 1,
            'Should have one disease. Got %s' % (
                self.disease_id.patient_id.count_disease_ids
            )
        )
