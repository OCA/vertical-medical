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

from odoo import fields, models, api
from odoo.tools.translate import _


class MedicalOperationalArea(models.Model):
    _name = 'medical.operational.area'
    _description = 'Medical Operational Area'

    name = fields.Char(string='Name', required=True)
    notes = fields.Text(string='Notes')
    sector_ids = fields.One2many(
        'medical.operational.sector', 'area_id', string='Operational Sectors')

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Area name must be unique!'),
    ]

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        default = default or {}
        if 'name' not in default:
            default['name'] = _('%s (copy)') % self.name
        return super(MedicalOperationalArea, self).copy(
            default=default)
