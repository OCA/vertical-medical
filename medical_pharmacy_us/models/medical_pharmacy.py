# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api
from openerp.exceptions import ValidationError


class MedicalPharmacy(models.Model):
    _inherit = ['medical.pharmacy', 'medical.luhn.abstract']
    _name = 'medical.pharmacy'

    nabp_num = fields.Char(
        help='National Boards of Pharmacy Id #',
    )
    medicaid_num = fields.Char(
        help='Medicaid Id #',
    )
    npi_num = fields.Char(
        help="National Provider Identifier",
    )

    @api.multi
    @api.constrains('country_id', 'npi_num')
    def _check_ref(self):
        """ Implement Luhns Formula to validate NPI """
        for rec_id in self:
            if rec_id.country_id.code == 'US':
                if not self._luhn_is_valid(rec_id.npi_num):
                    raise ValidationError('Invalid NPI Number.')
