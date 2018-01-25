# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import fields, models


class StockWarehouse(models.Model):

    _inherit = 'stock.warehouse'

    is_pharmacy = fields.Boolean(
        string='Pharmacy',
        default=True,
        help='Check if prescription orders allowed to be dispensed from'
        ' this warehouse',
    )
    prescription_route_id = fields.Many2one(
        string='Prescription Route',
        comodel_name='stock.location.route',
        domain=lambda s: [('id', 'in', [r.id for r in s.route_ids])],
        help='Stock route for prescription sales',
    )
    otc_route_id = fields.Many2one(
        string='OTC Route',
        comodel_name='stock.location.route',
        domain=lambda s: [('id', 'in', [r.id for r in s.route_ids])],
        help='Stock route for over the counter sales',
    )
