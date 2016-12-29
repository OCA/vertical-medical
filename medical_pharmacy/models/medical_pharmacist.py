# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


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
        return vals
