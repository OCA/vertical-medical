# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError


class TestEncounter(TransactionCase):
    def setUp(self):
        super(TestEncounter, self).setUp()
        self.patient = self.env['medical.patient'].create({
            'name': 'Patient'
        })
        self.patient_2 = self.env['medical.patient'].create({
            'name': 'Patient 2'
        })
        self.plan = self.browse_ref('medical_workflow.mr_knee')

    def test_create_careplan(self):
        encounter = self.env['medical.encounter'].create({
            'patient_id': self.patient.id
        })
        res = encounter.action_view_careplans()
        self.assertFalse(res.get('res_id'))
        careplan = self.env['medical.careplan'].create({
            'patient_id': self.patient.id,
            'encounter_id': encounter.id
        })
        with self.assertRaises(ValidationError):
            careplan.patient_id = self.patient_2
        res = encounter.action_view_careplans()
        self.assertTrue(res.get('res_id'))
        self.env['medical.careplan'].create({
            'patient_id': self.patient.id,
            'encounter_id': encounter.id
        })
        res = encounter.action_view_careplans()
        self.assertFalse(res.get('res_id'))
        self.env['medical.careplan.add.plan.definition'].create({
            'patient_id': self.patient.id,
            'careplan_id': careplan.id,
            'plan_definition_id': self.plan.id
        }).run()
