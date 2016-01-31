# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api


class MedicalPharmacy(models.Model):
    _inherit = ['medical.pharmacy', 'medical.abstract.npi']
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
    def _check_npi_num(self):
        """ Implement Luhns Formula to validate NPI """
        self._npi_constrains_helper('npi_num')
