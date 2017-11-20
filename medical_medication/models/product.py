# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Product(models.Model):
    # FHIR Model: Medication (https://www.hl7.org/fhir/medication.html)
    _inherit = 'product.template'

    is_medication = fields.Boolean(default=False)
    sct_code_id = fields.Many2one(
        string='SNOMED CT code',
        comodel_name='medical.sct.concept',
        domain=[('is_medication_code', '=', True)],
        help='SNOMED CT Medication Codes',
    )  # FHIR Field: code
    atc_code_id = fields.Many2one(
        string='ATC code',
        comodel_name='medical.atc.concept',
        help='ATC medication classification',
    )
    over_the_counter = fields.Boolean(
        default=False,
        help='True if medication does not require a prescription',
    )  # FHIR Field: isOverTheCounter
    form_id = fields.Many2one(
        string='Form code',
        comodel_name='medical.sct.concept',
        domain=[('is_medication_form', '=', True)],
        help='SNOMED CT Form Codes',
    )  # FHIR Field: form

    @api.constrains('type', 'is_medication')
    def _check_medication(self):
        if self.is_medication:
            if self.type not in ['product', 'consu']:
                raise ValidationError(_(
                    'Medication must be a stockable product'))
