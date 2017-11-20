# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    request_group_id = fields.Many2one(
        string="Parent Request group",
        comodel_name="medical.request.group",
    )   # FHIR Field: BasedOn

    request_group_ids = fields.One2many(
        string="Parent Request group",
        comodel_name="medical.request.group",
        inverse_name='id'
    )
