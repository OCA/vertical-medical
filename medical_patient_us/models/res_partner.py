# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class ResPartner(models.Model):
    _inherit = ['res.partner', 'medical.abstract.luhn']
    _name = 'res.partner'

    @api.multi
    @api.constrains('country_id', 'ref', 'is_patient')
    def _check_ref(self):
        """ Implement Luhns Formula to validate social security numbers """
        for rec_id in self:
            if rec_id.is_patient:
                rec_id._luhn_constrains_helper('ref')
