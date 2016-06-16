# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'
    medicament_ids = fields.One2many(
        string='Medicament',
        comodel_name='medical.medicament',
        inverse_name='product_id',
    )

    @api.multi
    def name_get(self):
        res = []
        for rec_id in self:
            if rec_id.is_medicament and len(rec_id.medicament_ids):
                try:
                    med_name = rec_id.medicament_ids.name_get()[0]
                    res.append((rec_id.id, med_name[1]))
                    continue
                except IndexError:
                    pass
            res.extend(super(ProductProduct, rec_id).name_get())
        return res
