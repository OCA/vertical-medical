# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPhysician(models.Model):
    _inherit = 'medical.physician'

    license_num = fields.Char(
        string='State License #', help='State medical license #'
    )
    dea_num = fields.Char(
        string='DEA #', help='Drug Enforcement Agency #'
    )
    npi_num = fields.Char(
        string='NPI #', help="National Provider Identifier"
    )
