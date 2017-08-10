# -*- coding: utf-8 -*-
# Copyright 2016-2018 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

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
        return super(MedicalPharmacy, self)._create_vals(vals)
