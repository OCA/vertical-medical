# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MedicalPhysician(models.Model):
    _name = 'medical.physician'
    _inherit = 'medical.abstract.entity'
    _description = 'Medical Physicians'

    code = fields.Char(
        string='ID',
        help='Physician Code',
    )
    specialty_id = fields.Many2one(
        help='Specialty Code',
        comodel_name='medical.specialty',
        default=lambda self: self.env.ref(
            'medical_physician.medical_specialty_gp',
        ),
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

    @api.model
    def _create_vals(self, vals):
        vals['customer'] = False
        if not vals.get('code'):
            sequence = self.env['ir.sequence'].next_by_code(
                self._name,
            )
            vals['code'] = sequence
        return super(MedicalPhysician, self)._create_vals(vals)
