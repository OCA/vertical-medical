# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase
from odoo import _


class TestWorkflowPlandefinition(TransactionCase):

    def setUp(self):
        super(TestWorkflowPlandefinition, self).setUp()

        # Models
        self.model_worfklow = self.env['workflow.type']
        self.model_activity_definition = \
            self.env['workflow.activity.definition']
        self.model_action = self.env['workflow.plan.definition.action']
        self.model_plandefinition = self.env['workflow.plan.definition']

        # Workflow
        self.workflow_type = self._create_workflow_type()

        # Activity 1, 2 and 3
        self.activity_definition_1 = self.\
            _create_activity_definition(self.workflow_type)
        self.activity_definition_2 = self.\
            _create_activity_definition(self.workflow_type)
        self.activity_definition_3 = self.\
            _create_activity_definition(self.workflow_type)

        # Plan Definition
        self.plan_definiton = self._create_plan_definition(self.workflow_type)

    def _create_workflow_type(self):
        """ Create a workflow."""
        return self.model_worfklow.create({
            'name': 'test',
            'description': 'description of the test',
        })

    def _create_activity_definition(self, workflow_type):
        """ Create an activity definition."""
        return self.model_activity_definition.create({
            'name': 'activity',
            'description': 'description of the activity',
            'type_id': workflow_type.id,
        })

    def _create_plan_definition(self, workflow_type):
        """ Create a plan definition."""
        return self.model_plandefinition.create({
            'name': 'Plan Definition',
            'description': 'description of the Plan Definition',
            'type_id': workflow_type.id,
        })

    def _create_action(self, activity_definition, plan_definition):
        """ Create an action."""
        return self.model_action.create({
            'name': 'Action',
            'direct_plan_definition_id': plan_definition.id,
            'activity_definition_id': activity_definition.id,
        })

    def _create_action_with_childs(self, activity_definition,
                                   plan_definition):
        """ Create an action."""
        return self.model_action.create({
            'name': 'Action',
            'direct_plan_definition_id': plan_definition.id,
            'activity_definition_id': activity_definition.id,
            'child_ids': [(0, _, {'name': 'child'})]
        })

    def test_action_belongs_to_plan_definition(self):
        """ Create a new plan definition and add two actions. The second one
        will have a child action its own. """

        self.action_1 = self._create_action(self.activity_definition_1,
                                            self.plan_definiton)
        self.action_1._onchange_activity_definition_id()
        self.assertEquals(self.action_1.name, 'activity',
                          "The name of the action must be 'activity'.")
        self.action_2 = self._create_action_with_childs(
            self.activity_definition_2, self.plan_definiton)
        self.assertEquals(len(self.plan_definiton.direct_action_ids), 2,
                          "The Plan Definition must have 2 direct actions.")
        self.assertEquals(len(self.plan_definiton.action_ids), 3,
                          "The Plan Definition must have 3 actions.")
