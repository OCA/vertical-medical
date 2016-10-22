# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MedicalMedicament(models.Model):
    _inherit = 'medical.medicament'

    storage_ids = fields.Many2many(
        help='Selection of applicable storage instructions',
        comodel_name='medical.medicament.storage',
    )
