# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalMedicationTemplate(models.Model):
    _inherit = 'medical.medication.template'
    dispense_uom_id = fields.Many2one(
        comodel_name='product.uom',
        string='Dispense UoM',
        help='Dispense Unit of Measure',
    )
