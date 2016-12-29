# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


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
