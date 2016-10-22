# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    is_pharmacy = fields.Boolean(
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
