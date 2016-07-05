# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_medicament = fields.Boolean(
        readonly=True,
        help=_('Check if the product is a medicament'),
    )
    is_vaccine = fields.Boolean(
        string='Vaccine',
        help=_('Check if the product is a vaccine'),
    )
