# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class RequestGroup(models.Model):
    """
    FHIR entity: Request Group
    link: https://www.hl7.org/fhir/requestgroup.html)
    """
    _name = 'medical.request.group'
    _description = 'Request Group'
    _inherit = 'medical.request'

    procedure_request_ids = fields.One2many(
        inverse_name="request_group_id",
    )
    request_group_ids = fields.One2many(
        inverse_name="request_group_id",
    )

    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code(
            'medical.request.group') or '/'
