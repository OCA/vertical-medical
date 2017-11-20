# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    careplan_id = fields.Many2one(
        string="Parent Careplan",
        comodel_name="medical.careplan"
    )   # FHIR Field: BasedOn
    careplan_ids = fields.One2many(
        string="Associated Careplans",
        comodel_name="medical.careplan",
        inverse_name='id'
    )
