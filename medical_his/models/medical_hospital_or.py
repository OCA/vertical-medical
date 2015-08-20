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


class MedicalHospitalOr(models.Model):
    _name = 'medical.hospital.or'
    _inherit = ['abstract.medical.hospital']
    _description = 'Medical Hospital Operating Room'

    @api.one
    @api.constrains('name', 'zone_id')
    def _check_unicity_name(self):
        domain = [
            ('name', '=', self.name),
            ('zone_id', '=', self.zone_id.id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError('"name" Should be unique per Zone')

    name = fields.Char()
    active = fields.Boolean(default=True)
    zone_id = fields.Many2one(
        string='Zone', comodel_name='medical.hospital.zone', index=True)
    partner_id = fields.Many2one(
        string='Institution', comodel_name='res.partner',
        domain=[('is_institution', '=', True)], index=True)
    unit_id = fields.Many2one(
        string='Unit', comodel_name='medical.hospital.unit', index=True)
    notes = fields.Text()
