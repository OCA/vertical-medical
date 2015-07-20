# -*- coding: utf-8 -*-
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
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

from openerp import fields, models


class MedicalHospitalZone(models.Model):
    _name = 'medical.hospital.zone'
    _description = 'Medical Hospital Zone'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    notes = fields.Text(string='Notes')
    partner_id = fields.Many2one(
        string='Institution', comodel_name='res.partner', index=1)
    parent_id = fields.Many2one(
        string='Parent Zone', comodel_name='medical.hospital.zone', index=1)
