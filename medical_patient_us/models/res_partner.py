# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api
from openerp.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = ['res.partner', 'medical.luhn.abstract']
    _name = 'res.partner'

    @api.multi
    @api.constrains('country_id', 'ref', 'is_patient')
    def _check_ref(self):
        """ Implement Luhns Formula to validate social security numbers """
        for rec_id in self:
            if rec_id.country_id.code == 'US' and rec_id.is_patient:
                if not self._luhn_is_valid(rec_id.ref):
                    raise ValidationError('Invalid Social Security Number.')
