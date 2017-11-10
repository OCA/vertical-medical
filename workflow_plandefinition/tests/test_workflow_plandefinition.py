# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestWorkflowPlandefinition(TransactionCase):

    def setUp(self):
        res = super(TestWorkflowPlandefinition, self).setUp()
        self.type = self.browse_ref('workflow_plandefinition.medical_workflow')
        self.aux_type = self.env['workflow.type'].create({
            'name': 'TEST',
            'model_id': self.browse_ref('medical.model_medical_patient').id,
        })
        return res

    def test_activity(self):
        activity = self.env['workflow.activity.definition'].new({
            'name': 'Activity',
            'type_id': self.type.id,
            'model_id': self.type.model_id.id
        })
        activity.type_id = self.aux_type
        activity._onchange_type_id()
        self.assertFalse(activity.model_id)

    def test_activity_constrains(self):
        activity = self.browse_ref('workflow_plandefinition.check_up_activity')
        with self.assertRaises(ValidationError):
            activity.type_id = self.aux_type

    def test_action(self):
        plan = self.browse_ref('workflow_plandefinition.basic_check_up')
        plan_02 = self.browse_ref('workflow_plandefinition.ct_abdominal')
        activity = self.browse_ref('workflow_plandefinition.check_up_activity')
        activity_02 = self.browse_ref('workflow_plandefinition.ct_activity')
        action = self.env['workflow.plan.definition.action'].new({
            'name': 'Activity',
            'type_id': self.type.id,
            'model_id': self.type.model_id.id,
            'plan_definition_id': plan.id,
            'activity_definition_id': activity.id
        })
        action.plan_definition_id = plan_02
        action._onchange_activity_definition_id()
        action.activity_definition_id = activity_02
        action._onchange_activity_definition_id()
        self.assertEqual(action.name, activity_02.name)

    def test_action_constrain(self):
        action = self.browse_ref(
            'workflow_plandefinition.basic_check_up_ct_action')
        with self.assertRaises(ValidationError):
            action.parent_id = action

    def test_execution_ct(self):
        patient = self.browse_ref('medical.medical_patient_patient_1')
        requests = self.env['medical.request.group'].search([
            ('patient_id', '=', patient.id)
        ])
        self.assertEqual(len(requests), 0)
        plan = self.browse_ref('workflow_plandefinition.ct_abdominal')
        with self.assertRaises(ValidationError):
            plan.execute_plan_definition({})
        plan.execute_plan_definition({'patient_id': patient.id})
        requests = self.env['medical.request.group'].search([
            ('patient_id', '=', patient.id)
        ])
        self.assertGreater(len(requests), 0)

    def test_execution_check_up(self):
        patient = self.browse_ref('medical.medical_patient_patient_1')
        service = self.browse_ref('workflow_plandefinition.check_up_product')
        requests = self.env['medical.request.group'].search([
            ('patient_id', '=', patient.id),
            ('service_id', '=', service.id)
        ])
        self.assertEqual(len(requests), 0)
        plan = self.browse_ref('workflow_plandefinition.basic_check_up')
        with self.assertRaises(ValidationError):
            plan.execute_plan_definition({})
        self.env['medical.add.plan.definition'].create({
            'patient_id': patient.id,
            'plan_definition_id': plan.id
        }).run()
        requests = self.env['medical.request.group'].search([
            ('patient_id', '=', patient.id),
            ('service_id', '=', service.id)
        ])
        self.assertGreater(len(requests), 0)

    def test_main_activity(self):
        plan = self.env['workflow.plan.definition'].create({
            'name': 'Head MR',
            'description': 'Head magnetic ressonance',
            'type_id': self.type.id,
            'state': 'active',
            'activity_definition_id': self.browse_ref(
                'workflow_plandefinition.mr_activity'
            ).id
        })
        patient = self.browse_ref('medical.medical_patient_patient_1')
        requests = self.env['medical.request.group'].search([
            ('patient_id', '=', patient.id)
        ])
        self.assertEqual(len(requests), 0)
        self.env.user.groups_id = [(4, self.browse_ref(
            'workflow_plandefinition.group_main_activity_plan_definition').id)]
        plan.execute_plan_definition({'patient_id': patient.id})
        requests = self.env['medical.request.group'].search([
            ('patient_id', '=', patient.id)
        ])
        self.assertGreater(len(requests), 0)
