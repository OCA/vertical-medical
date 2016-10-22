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
from odoo.exceptions import ValidationError


class TestMedicalHospitalUnit(SharedSetupTransactionCase):

    _data_files = (
        'data/medical_his_data.xml',
    )

    _module_ns = 'medical_his'

    def setUp(self):
        SharedSetupTransactionCase.setUp(self)

    def test_unicity(self):
        medical_hospital_unit = self.env['medical.hospital.unit']
        unit = self.env.ref('%s.unit_1' % self._module_ns)
        vals = {
            'name': unit.name,
            'label': unit.label,
        }
        with self.assertRaises(ValidationError):
            medical_hospital_unit.create(vals)
