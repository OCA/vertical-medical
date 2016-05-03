# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class WebsitePricelist(models.Model):
    _inherit = 'website_pricelist'
    medical_insurance_template_ids = fields.One2many(
        string='Insurance Templates',
        comodel_name='medical.insurance.template',
        compute=lambda s: s._compute_medical_insurance_template_ids()
    )

    @api.multi
    def _compute_medical_insurance_template_ids(self):
        ins_obj = self.env['medical.insurance.template']
        for rec_id in self:
            rec_id.medical_insurance_template_ids = ins_obj.search([
                ('pricelist_id', '=', rec_id.pricelist_id.id),
            ])
