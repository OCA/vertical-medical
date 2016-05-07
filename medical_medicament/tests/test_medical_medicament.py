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


class TestMedicalMedicament(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicament, self).setUp()
        self.medical_medicament_obj = self.env['medical.medicament']
        self.name = 'ProductMedicament'
        self.vals = {
            'name': self.name,
            'drug_form_id': self.env.ref('medical_medicament.AEM').id,
        }

    def _test_record(self, ):
        return self.medical_medicament_obj.create(self.vals)

    def test_create(self):
        """
        Test create to assure second level inherits works fine
        """
        medicament_id = self._test_record()
        self.assertTrue(medicament_id)
        self.assertTrue(medicament_id.product_id)
        self.assertTrue(medicament_id.product_id.is_medicament)

    def test_name_get(self, ):
        ''' Verify that name is product and form '''
        medicament_id = self._test_record()
        expect = '%s - %s' % (medicament_id.product_id.name,
                              medicament_id.drug_form_id.name)
        self.assertTrue(expect, medicament_id)
