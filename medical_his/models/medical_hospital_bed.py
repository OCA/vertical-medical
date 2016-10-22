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

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MedicalHospitalBed(models.Model):
    _name = 'medical.hospital.bed'
    _inherit = ['abstract.medical.hospital']
    _description = 'Medical Hospital Bed'

    @api.one
    @api.constrains('name', 'room_id')
    def _check_unicity_name(self):
        domain = [
            ('name', '=', self.name),
            ('room_id', '=', self.room_id.id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError('"name" Should be unique per Room')

    @api.one
    @api.constrains('room_id', 'active')
    def _check_room_id(self):
        if self.active and not self.room_id:
            raise ValidationError('Room is mandatory for an available bed')

    @api.one
    @api.depends('name', 'room_id', 'room_id.name',
                 'room_id.display_name')
    def _compute_display_name(self):
        if self.room_id:
            self.display_name =\
                '%s/%s' % (self.room_id.display_name, self.name)
        else:
            self.display_name = self.name

    name = fields.Char(required=True)
    display_name = fields.Char(compute='_compute_display_name', store=True)
    phone = fields.Char()
    notes = fields.Text()
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('free', 'Free'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
    ], default='free')
    bed_type_id = fields.Many2one(
        string='Bed Type', comodel_name='medical.hospital.bed.type',
        index=True)
    room_id = fields.Many2one(
        string='Room', comodel_name='medical.hospital.room', index=True)
    expire_date = fields.Datetime()


class BedType(models.Model):
    _name = 'medical.hospital.bed.type'
    _description = 'Medical Hospital Bed Type'

    name = fields.Char()
    code = fields.Char()
