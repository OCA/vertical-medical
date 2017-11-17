# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalRequestGroup(models.Model):
    _inherit = 'medical.request.group'

    careplan_ids = fields.One2many(
        string="Associated Careplans",
        comodel_name="medical.careplan",
        inverse_name='request_group_id'
    )
