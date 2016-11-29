# -*- coding: utf-8 -*-
# Copyright 2016 Ursa Information Systems <http://ursainfosystems.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from openerp import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    weight = fields.Float("Weight")
    weight_uom = fields.Many2one(
        "product.uom", "Weight UoM",
        domain=lambda self: [('category_id', '=',
                              self.env.ref('product.product_uom_categ_kgm').id)
                             ]
    )
