# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class MedicalMedicament(models.Model):
    _inherit = 'medical.medicament'

    @api.model
    def create(self, vals):
        if not vals.get('type'):
            vals['type'] = 'product'
        return super(MedicalMedicament, self).create(vals)
