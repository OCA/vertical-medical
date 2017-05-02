# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProcurementOrder(models.Model):

    _inherit = 'procurement.order'

    ndc_id = fields.Many2one(
        string='NDC',
        comodel_name='medical.medicament.ndc',
    )
