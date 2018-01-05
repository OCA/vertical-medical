# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class ActivityDefinition(models.Model):
    # FHIR entity: Activity Definition
    # (https://www.hl7.org/fhir/activitydefinition.html)
    _inherit = 'workflow.activity.definition'

    def _get_medical_values(self, vals, parent=False, plan=False, action=False
                            ):
        values = super(ActivityDefinition, self)._get_medical_values(
            vals, parent=False, plan=False, action=False)
        if self.model_id.model == 'medical.medication.request':
            values.update({
                'product_id': self.service_id.id,
                'product_uom_id': self.service_id.uom_id.id,
            })
        return values
