# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.multi
    def _is_descendant_of(self, category_id):
        """ Compute whether provided category is an ancestor of the input """
        self.ensure_one()
        if not self.parent_id:
            return False
        if self.parent_id == category_id:
            return True
        return self.parent_id._is_descendant_of(category_id)
