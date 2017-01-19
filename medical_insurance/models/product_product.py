# -*- coding: utf-8 -*-
# Copyright 2015-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'
    is_insurance_plan = fields.Boolean(
        string='Insurance Plan',
        help='Check this if the product is an insurance plan',
    )
