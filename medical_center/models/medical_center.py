# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, tools
from odoo.modules import get_module_resource


class MedicalCenter(models.Model):
    _name = 'medical.center'
    _description = 'Medical Center'
    _inherit = 'medical.abstract.entity'

    @api.model
    def _create_vals(self, vals):
        vals.update({
            'is_company': True,
            'customer': False,
        })
        return super(MedicalCenter, self)._create_vals(vals)

    @api.model
    def _get_default_image(self, vals):
        res = super(MedicalCenter, self)._get_default_image(vals)
        if not res:
            return res
        img_path = get_module_resource(
            'medical_center', 'static/src/img', 'medical-center-avatar.png',
        )
        with open(img_path, 'r') as image:
            base64_image = image.read().encode('base64')
            return tools.image_resize_image_big(base64_image)
