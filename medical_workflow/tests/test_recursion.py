# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError


class TestRecursion(TransactionCase):

    def test_recursion(self):
        plan_obj = self.env['workflow.plan.definition']
        action_obj = self.env['workflow.plan.definition.action']
        workflow_type = self.browse_ref('medical_workflow.medical_workflow')
        plan_1 = plan_obj.create({
            'name': 'P1',
            'type_id': workflow_type.id
        })
        with self.assertRaises(ValidationError):
            action_obj.create({
                'direct_plan_definition_id': plan_1.id,
                'name': plan_1.name,
                'execute_plan_definition_id': plan_1.id
            })
        plan_2 = plan_obj.create({
            'name': 'P2',
            'type_id': workflow_type.id
        })
        action_obj.create({
            'direct_plan_definition_id': plan_1.id,
            'name': plan_2.name,
            'execute_plan_definition_id': plan_2.id
        })
        with self.assertRaises(ValidationError):
            action_obj.create({
                'direct_plan_definition_id': plan_2.id,
                'name': plan_1.name,
                'execute_plan_definition_id': plan_1.id
            })
        plan_3 = plan_obj.create({
            'name': 'P3',
            'type_id': workflow_type.id
        })
        action_obj.create({
            'direct_plan_definition_id': plan_2.id,
            'name': plan_3.name,
            'execute_plan_definition_id': plan_3.id
        })
        with self.assertRaises(ValidationError):
            action_obj.create({
                'direct_plan_definition_id': plan_3.id,
                'name': plan_1.name,
                'execute_plan_definition_id': plan_1.id
            })
        action = action_obj.create({
            'direct_plan_definition_id': plan_1.id,
            'name': 'AUX'
        })
        with self.assertRaises(ValidationError):
            action_obj.create({
                'parent_id': action.id,
                'name': plan_1.name,
                'execute_plan_definition_id': plan_1.id
            })
