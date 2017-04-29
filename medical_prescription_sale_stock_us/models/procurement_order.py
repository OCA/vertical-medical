# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    ndc_id = fields.Many2one(
        string='NDC',
        comodel_name='medical.medicament.ndc',
    )
