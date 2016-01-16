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

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class MedicalHospitalRoom(models.Model):
    _name = 'medical.hospital.room'
    _inherit = ['abstract.medical.hospital']
    _description = 'Medical Hospital Room'
    _rec_name = 'display_name'

    @api.one
    @api.constrains('name', 'zone_id')
    def _check_unicity_name(self):
        domain = [
            ('name', '=', self.name),
            ('zone_id', '=', self.zone_id.id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError('"name" Should be unique per Zone')

    @api.one
    @api.depends('name', 'zone_id', 'zone_id.name',
                 'zone_id.display_name')
    def _compute_display_name(self):
        self.display_name =\
            '%s/%s' % (self.zone_id.display_name, self.name)

    name = fields.Char(required=True)
    display_name = fields.Char(compute='_compute_display_name', store=True)
    label = fields.Char()
    phone = fields.Char()
    notes = fields.Text()
    capacity = fields.Integer()
    state = fields.Selection([
        ('free', 'Free'),
        ('beds_available', 'Beds available'),
        ('full', 'Full'), ], default='free')
    private = fields.Boolean()
    active = fields.Boolean(default=True)
    unit_id = fields.Many2one(
        string='Unit', comodel_name='medical.hospital.unit', index=True)
    zone_id = fields.Many2one(
        string='Zone', comodel_name='medical.hospital.zone', index=True,
        required=True)
    bed_ids = fields.One2many(
        string='Beds', comodel_name='medical.hospital.bed',
        inverse_name='room_id')
