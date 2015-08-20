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

from openerp import fields, models, api
from openerp.exceptions import ValidationError


class MedicalHospitalUnit(models.Model):
    _name = 'medical.hospital.unit'
    _inherit = ['abstract.medical.hospital']
    _description = 'Medical Hospital Unit'

    @api.one
    @api.constrains('code')
    def _check_unicity_name(self):
        domain = [
            ('code', '=', self.code),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError('"code" Should be unique')

    name = fields.Char()
    code = fields.Char(required=True)
    notes = fields.Text()
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Institution',
        domain=[('is_institution', '=', True)], index=True)
    parent_id = fields.Many2one(
        string='Parent Unit', comodel_name='medical.hospital.unit', index=True)
