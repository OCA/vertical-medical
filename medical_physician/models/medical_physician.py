# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api


class MedicalPhysician(models.Model):
    _name = 'medical.physician'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Medical Physicians'

    partner_id = fields.Many2one(
        string='Related Partner',
        help='Partner-related data of the physician',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
    )
    code = fields.Char(
        string='ID',
        help='Physician code',
    )
    specialty_id = fields.Many2one(
        help='Specialty code',
        comodel_name='medical.specialty',
        default=lambda self: self.env.ref(
            'medical_physician.medical_specialty_gp'
        ),
        required=True,
    )
    info = fields.Text(
        string='Extra info',
        help='Other information about the physician',
    )
    active = fields.Boolean(
        default=True,
    )

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals,):
        vals.update({
            'is_doctor': True,
            'customer': False,
        })
        if not vals.get('code'):
            sequence = self.env['ir.sequence'].next_by_code(
                'medical.physician'
            )
            vals['code'] = sequence
        return super(MedicalPhysician, self).create(vals)
