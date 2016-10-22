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
from odoo.exceptions import ValidationError


class MedicalHospitalZone(models.Model):
    _name = 'medical.hospital.zone'
    _inherit = ['abstract.medical.hospital']
    _description = 'Medical Hospital Zone'
    _rec_name = 'display_name'

    @api.one
    @api.constrains('name', 'parent_id')
    def _check_unicity_name(self):
        domain = [
            ('name', '=', self.name),
            ('parent_id', '=', self.parent_id.id),
        ]
        if len(self.search(domain)) > 1:
            raise ValidationError('"name" Should be unique per Parent Zone')

    @api.one
    @api.constrains('parent_id')
    def _check_recursion_parent_id(self):
        if not self._check_recursion():
            raise ValidationError('Error! You can not create recursive zone.')

    @api.one
    @api.depends('name', 'parent_id', 'parent_id.name',
                 'parent_id.display_name')
    def _compute_display_name(self):
        if self.parent_id:
            self.display_name =\
                '%s/%s' % (self.parent_id.display_name, self.name)
        else:
            self.display_name = self.name

    name = fields.Char(required=True)
    display_name = fields.Char(compute='_compute_display_name', store=True)
    label = fields.Char()
    notes = fields.Text()
    active = fields.Boolean(default=True)
    partner_id = fields.Many2one(
        string='Institution', comodel_name='res.partner',
        domain=[('is_institution', '=', True)], index=True)
    parent_id = fields.Many2one(
        string='Parent Zone', comodel_name='medical.hospital.zone', index=True)
    child_ids = fields.One2many(
        string='Children', comodel_name='medical.hospital.zone',
        inverse_name='parent_id')
    room_ids = fields.One2many(
        string='Rooms', comodel_name='medical.hospital.room',
        inverse_name='zone_id')
