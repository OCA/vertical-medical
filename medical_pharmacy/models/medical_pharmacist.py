# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, models
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
    def _get_default_image_path(self, vals):
        super(MedicalPharmacist, self)._get_default_image_path(vals)
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
        return img_path
