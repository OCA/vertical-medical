# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestWorkflowPlandefinition(TransactionCase):

    def setUp(self):
        res = super(TestWorkflowPlandefinition, self).setUp()
        self.type = self.env['workflow.type'].create({
            'name': 'TEST',
            'model_id': self.browse_ref(
                'medical_administration.model_medical_patient').id,
            'model_ids': [(4, self.browse_ref(
                'medical_administration.model_medical_patient').id)],
        })
        self.aux_type = self.env['workflow.type'].create({
            'name': 'TEST',
            'model_id': self.browse_ref(
                'medical_administration.model_medical_patient').id,
            'model_ids': [(4, self.browse_ref(
                'medical_administration.model_medical_patient').id)],
        })
        self.activity = self.env['workflow.activity.definition'].create({
            'name': 'Activity',
            'type_id': self.type.id,
            'model_id': self.type.model_id.id
        })
        self.plan = self.env['workflow.plan.definition'].create({
            'name': 'Plan',
            'type_id': self.type.id,
        })
        self.activity_2 = self.env['workflow.activity.definition'].create({
            'name': 'Activity 2',
            'type_id': self.type.id,
            'model_id': self.type.model_id.id
        })
        self.plan_2 = self.env['workflow.plan.definition'].create({
            'name': 'Plan 2',
            'type_id': self.type.id,
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
        self.env['workflow.plan.definition.action'].create({
            'name': 'Action',
            'direct_plan_definition_id': self.plan.id,
            'activity_definition_id': self.activity.id
        })
        with self.assertRaises(ValidationError):
            self.activity.type_id = self.aux_type

    def test_action(self):
        action = self.env['workflow.plan.definition.action'].new({
            'name': 'Action',
            'direct_plan_definition_id': self.plan.id,
            'activity_definition_id': self.activity.id
        })
        action.plan_definition_id = self.plan_2
        action._onchange_activity_definition_id()
        action.activity_definition_id = self.activity_2
        action._onchange_activity_definition_id()
        self.assertEqual(action.name, self.activity_2.name)

    def test_action_constrain(self):
        action = self.env['workflow.plan.definition.action'].create({
            'name': 'Action',
            'direct_plan_definition_id': self.plan.id,
            'activity_definition_id': self.activity.id
        })
        with self.assertRaises(ValidationError):
            action.parent_id = action
