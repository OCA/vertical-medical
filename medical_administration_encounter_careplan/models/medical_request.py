# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    encounter_id = fields.Many2one(
        comodel_name='medical.encounter',
    )

    @api.constrains('patient_id', 'encounter_id')
    def _check_patient_encounter(self):
        if self.encounter_id:
            if self.encounter_id.patient_id != self.patient_id:
                raise ValidationError(_(
                    'Inconsistency between patient and encounter'))
