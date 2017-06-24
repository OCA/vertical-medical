# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
from odoo.modules import get_module_resource


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
    calendar_id = fields.Many2one(
        string='Calendar',
        comodel_name='resource.calendar',
        help='Schedule for this physician.',
    )
    service_ids = fields.Many2many(
        string='Services',
        comodel_name='medical.physician.service',
        help='Services offered by this physician.',
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

    @api.model
    def _get_default_image_path(self, vals):
        super(MedicalPhysician, self)._get_default_image_path(vals)
        img_path = 'physician-%s-avatar.png' % vals.get('gender')
        img_path = get_module_resource(
            'medical_pharmacy', 'static/src/img', img_path,
        )
        if not img_path:
            img_path = get_module_resource(
                'medical_physician',
                'static/src/img',
                'physician-male-avatar.png',
            )
        return img_path
