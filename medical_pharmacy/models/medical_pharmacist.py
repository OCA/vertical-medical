# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, tools
from odoo.modules import get_module_resource


class MedicalPharmacist(models.Model):
    _name = 'medical.pharmacist'
    _description = 'Medical Pharmacist'
    _inherit = 'medical.abstract.entity'

    @api.model
    def _create_vals(self, vals):
        vals.update({
            'is_company': False,
            'customer': False,
        })
        return super(MedicalPharmacist, self)._create_vals(vals)

    @api.model
    def _get_default_image(self, vals):
        res = super(MedicalPharmacist, self)._get_default_image(vals)
        if not res:
            return res
        img_path = 'pharmacist-%s-avatar.png' % vals.get('gender')
        img_path = get_module_resource(
            'medical_pharmacy', 'static/src/img', img_path,
        )
        if not img_path:
            img_path = get_module_resource(
                'medical_pharmacy',
                'static/src/img',
                'pharmacist-female-avatar.png',
            )
        with open(img_path, 'r') as image:
            base64_image = image.read().encode('base64')
            return tools.image_resize_image_big(base64_image)
