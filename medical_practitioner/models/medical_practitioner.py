# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo import api, fields, models, modules


class MedicalPractitioner(models.Model):
    _name = 'medical.practitioner'
    _description = 'Medical Practitioner'
    _inherit = 'medical.abstract.entity'

    _sql_constraints = [(
        'medical_practitioner_unique_code',
        'UNIQUE (code)',
        'Internal ID must be unique',
    )]

    role_ids = fields.Many2many(
        string='Roles',
        comodel_name='medical.role',
    )
    practitioner_type = fields.Selection(
        string='Entity Type',
        selection=[('internal', 'Internal Entity'),
                   ('external', 'External Entity')],
        readonly=False,
    )
    code = fields.Char(
        string='Internal ID',
        help='Unique ID for this physician',
        required=True,
        default=lambda s: s.env['ir.sequence'].next_by_code(s._name + '.code'),
    )
    specialty_ids = fields.Many2many(
        string='Specialties',
        comodel_name='medical.specialty',
    )

    @api.model
    def _get_default_image_path(self, vals):
        res = super(MedicalPractitioner, self)._get_default_image_path(vals)
        if res:
            return res

        practitioner_gender = vals.get('gender', 'male')
        if practitioner_gender == 'other':
            practitioner_gender = 'male'

        image_path = modules.get_module_resource(
            'medical_practitioner',
            'static/src/img',
            'practitioner-%s-avatar.png' % practitioner_gender,
        )
        return image_path
