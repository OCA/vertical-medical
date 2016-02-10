# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Ken Mak <kmak@laslabs.com>
#    Copyright: 2014-2016 LasLabs, Inc. [https://laslabs.com]
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


class MedicalPhysician(models.Model):
    _name = 'medical.physician'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Medical Physicians'
    id = fields.Integer(
        string='ID',
        help='ID',
        readonly=True,
    )
    partner_id = fields.Many2one(
        string='Related Partner',
        help='Partner related data of the physician',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
    )
    code = fields.Char(
        string='ID',
        help='Physician Code',
        size=256,
    )
    specialty_id = fields.Many2one(
        string='Specialty',
        help='Specialty Code',
        comodel_name='medical.specialty',
        default=lambda self: self.env['medical.specialty'].search(
            [('name', '=', 'General Practitioner')]).id,
        required=True,
    )
    info = fields.Text(
        string='Extra info',
        help='Extra Info',
    )
    active = fields.Boolean(
        string='Active',
        help='If unchecked, it will allow you to hide the physician without '
             'removing it.',
        default=True,
    )
    schedule_template_ids = fields.One2many(
        string='Related schedules',
        help='Schedule template of the physician',
        comodel_name='medical.physician.schedule.template',
        inverse_name='physician_id',
    )
    supplier = fields.Boolean(
        string='Is a Vendor',
        help='Check this box if this contact is a vendor. '
             'If it\'s not checked, purchase people will not see it when'
             'encoding a purchase order.',
        default=True,
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals,):
        vals['is_doctor'] = True
        if not vals.get('code'):
            sequence = self.env['ir.sequence'].next_by_code(
                'medical.physician'
            )
            vals['code'] = sequence
        return super(MedicalPhysician, self).create(vals)
