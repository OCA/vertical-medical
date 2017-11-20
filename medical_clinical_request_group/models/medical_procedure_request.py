# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalProcedureRequest(models.Model):
    _inherit = 'medical.procedure.request'

    request_group_ids = fields.One2many(
        inverse_name="procedure_request_id",
    )
