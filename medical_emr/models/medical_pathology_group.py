# -*- coding: utf-8 -*-
# #############################################################################
#
# Tech-Receptives Solutions Pvt. Ltd.
# Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import fields, models


class MedicalPathologyGroup(models.Model):
    _name = 'medical.pathology.group'
    _description = 'Medical Pathology Group'

    name = fields.Char(string='Name', required=True, translate=True)
    notes = fields.Text(string='Notes')
    code = fields.Char(
        string='Code', required=True, help='for example MDG6 code will contain'
        ' the Millennium Development Goals # 6 diseases : Tuberculosis, '
        'Malaria and HIV/AIDS')
    desc = fields.Char(string='Short Description', required=True)
