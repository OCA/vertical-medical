# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical_his,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical_his is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     medical_his is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with one2many_groups.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from anybox.testing.openerp import SharedSetupTransactionCase
from openerp.exceptions import ValidationError


class TestMedicalHospitalZone(SharedSetupTransactionCase):

    _data_files = (
        'data/medical_his_data.xml',
    )

    _module_ns = 'medical_his'

    def setUp(self):
        SharedSetupTransactionCase.setUp(self)

    def test_unicity(self):
        medical_hospital_zone = self.env['medical.hospital.zone']
        zone = self.env.ref('%s.zone_1_l14' % self._module_ns)
        vals = {
            'name': zone.name,
            'code': zone.code,
            'parent_id': zone.parent_id.id,
        }
        with self.assertRaises(ValidationError):
            medical_hospital_zone.create(vals)

    def test_recursion_parent_id(self):
        child_zone = self.env.ref('%s.zone_1_l14' % self._module_ns)
        parent_zone = self.env.ref('%s.zone_1' % self._module_ns)
        with self.assertRaises(ValidationError):
            parent_zone.parent_id = child_zone.id
