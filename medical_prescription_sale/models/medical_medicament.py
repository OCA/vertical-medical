# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalMedicament(models.Model):
    _inherit = 'medical.medicament'
    is_prescription = fields.Boolean(
        string='Prescription Required',
        help='Check this if a prescription is required for this medicament',
    )
    is_controlled = fields.Boolean(
        string='Controlled Substance',
        help='Check this if the medicament is a controlled substance',
    )
