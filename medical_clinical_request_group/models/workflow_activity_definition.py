# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class ActivityDefinition(models.Model):
    _inherit = 'workflow.activity.definition'

    def _get_medical_values(self, vals, parent=False, plan=False, action=False
                            ):
        values = super(ActivityDefinition, self)._get_medical_values(
            vals, parent, plan, action)

        if parent and parent._name == 'medical.request.group':
            values['request_group_id'] = parent.id
        return values
