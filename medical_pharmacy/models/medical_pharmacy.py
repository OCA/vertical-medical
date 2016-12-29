# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class MedicalPharmacy(models.Model):
    _name = 'medical.pharmacy'
    _description = 'Medical Pharmacy'
    _inherit = 'medical.abstract.entity'

    @api.model
    def _create_vals(self, vals):
        vals.update({
            'is_company': True,
            'customer': False,
        })
        return vals
