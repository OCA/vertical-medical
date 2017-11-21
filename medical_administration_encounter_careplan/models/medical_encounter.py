# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class MedicalEncounter(models.Model):
    _inherit = 'medical.encounter'

    careplan_ids = fields.One2many(
        comodel_name='medical.careplan',
        inverse_name='encounter_id',
    )

    @api.multi
    def action_view_careplans(self):
        self.ensure_one()
        action = self.env.ref(
            'medical_clinical_careplan.medical_careplan_action')
        result = action.read()[0]

        result['context'] = {
            'default_patient_id': self.patient_id.id,
            'default_encounter_id': self.id,
        }
        result['domain'] = "[('encounter_id', '=', " + \
                           str(self.id) + ")]"
        if len(self.careplan_ids) == 1:
            result['views'] = [(False, 'form')]
            result['res_id'] = self.careplan_ids.id
        return result
