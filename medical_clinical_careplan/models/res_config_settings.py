# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_medical_careplan_add_plan_definition = fields.Boolean(
        string="Add Plan definition on careplans",
        implied_group='medical_clinical_careplan.'
                      'group_medical_careplan_add_plan_definition'
    )
