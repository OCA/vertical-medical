# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, models
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

    @api.model_cr_context
    def _get_default_image_path(self, vals):
        super(MedicalCenter, self)._get_default_image_path(vals)
        return get_module_resource(
            'medical_center', 'static/src/img', 'medical-center-avatar.png',
        )
