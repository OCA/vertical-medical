# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class MedicalInsuranceCompany(models.Model):
    _name = 'medical.insurance.company'
    _description = 'Medical Insurance Providers'
    _inherit = 'medical.abstract.entity'

    @api.model
    def _create_vals(self, vals):
        vals.update({
            'is_company': True,
        })
        return super(MedicalInsuranceCompany, self)._create_vals(vals)
