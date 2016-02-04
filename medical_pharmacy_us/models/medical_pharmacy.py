# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPharmacy(models.Model):
    _inherit = 'medical.pharmacy'
    nabp_num = fields.Integer(
        help='National Boards of Pharmacy Id #',
    )
    medicaid_num = fields.Integer(
        help='Medicaid Id #',
    )
    npi_num = fields.Integer(
        help="National Provider Identifier",
    )
