# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalPhysician(models.Model):
    _name = 'medical.physician'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Medical Physicians'

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
        help='Specialty Code',
        comodel_name='medical.specialty',
        default=lambda self: self.env.ref('medical_physician.spe1'),
        required=True,
    )
    info = fields.Text(
        string='Extra info',
        help='Extra Info',
    )
    active = fields.Boolean(
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
