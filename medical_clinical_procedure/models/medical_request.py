# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalRequest(models.AbstractModel):
    _inherit = 'medical.request'

    procedure_request_ids = fields.One2many(
        string="Associated Procedure Requests",
        comodel_name="medical.procedure.request",
        inverse_name="procedure_request_id",
    )

    procedure_request_id = fields.Many2one(
        string="Parent Procedure Request",
        comodel_name="medical.procedure.request"
    )
