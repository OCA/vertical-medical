# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of medical_operational,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     medical_operational is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     medical_operational is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with one2many_groups.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import openerp.tests.common as common


class TestMedicalHospitalArea(common.TransactionCase):

    def setUp(self):
        common.TransactionCase.setUp(self)
