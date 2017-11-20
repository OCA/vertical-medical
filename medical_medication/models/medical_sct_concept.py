# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalSCTConcept(models.Model):
    _inherit = 'medical.sct.concept'

    is_medication_form = fields.Boolean(
        store=True,
        index=True,
        compute='_compute_is_medication_form',
    )

    is_medication_code = fields.Boolean(
        store=True,
        index=True,
        compute='_compute_is_medication_code',
    )

    @api.depends('parent_ids')
    def _compute_is_medication_form(self):
        for record in self:
            record.is_medication_form = record.check_property(
                'is_medication_form',
                ['421967003']
            )

    @api.depends('parent_ids')
    def _compute_is_medication_code(self):
        for record in self:
            record.is_medication_code = record.check_property(
                'is_medication_code',
                ['373873005', '106181007', '410942007']
            )
