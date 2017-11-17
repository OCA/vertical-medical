# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalCareplan(models.Model):
    _inherit = 'medical.careplan'

    procedure_request_ids = fields.One2many(
        inverse_name='careplan_id'
    )
