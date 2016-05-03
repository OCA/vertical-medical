# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'
    insurance_template_ids = fields.One2many(
        string='Insurance Templates',
        comodel_name='medical.insurance.template',
        inverse_name='pricelist_id',
        help='Insurance template related to this pricelist',
    )
