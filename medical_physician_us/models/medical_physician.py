# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models, api
from openerp.exceptions import ValidationError


class MedicalPhysician(models.Model):
    _inherit = ['medical.physician', 'medical.abstract.luhn']
    _name = 'medical.physician'

    license_num = fields.Char(
        string='State License #', help='State medical license #'
    )
    dea_num = fields.Char(
        string='DEA #', help='Drug Enforcement Agency #'
    )
    npi_num = fields.Char(
        string='NPI #', help="National Provider Identifier"
    )

    @api.multi
    @api.constrains('country_id', 'npi_num')
    def _check_npi_num(self):
        """ Implement Luhns Formula to validate NPI """
        for rec_id in self:
            if rec_id.country_id.code == 'US':
                if not self._luhn_is_valid(rec_id.npi_num):
                    raise ValidationError('Invalid NPI Number.')

    @api.multi
    @api.constrains('country_id', 'dea_num')
    def _check_dea_num(self, ):
        """ Implement DEA Formula to validate NPI """
        for rec_id in self:
            if rec_id.country_id.code == 'US':
                if not self._luhn_is_valid(rec_id.npi_num):
                    raise ValidationError('Invalid NPI Number.')
