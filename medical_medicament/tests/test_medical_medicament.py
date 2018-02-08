# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical, an Odoo module.
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
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

    def test_create(self):
        """
        Test create to assure second level inherits works fine
        """
        name = 'ProductMedicament'
        vals = {
            'name': name,
            'drug_form_id': self.env.ref('medical_medicament.AEM').id,
        }
        medicament_id = self.medical_medicament_obj.create(vals)
        self.assertTrue(medicament_id)
        self.assertTrue(medicament_id.product_id)
        self.assertTrue(medicament_id.product_id.is_medicament)
