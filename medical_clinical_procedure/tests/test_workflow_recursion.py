# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase


class TestProcedure(TransactionCase):
    def setUp(self):
        res = super(TestProcedure, self).setUp()
        self.patient = self.browse_ref('medical_administration.patient_01')
        self.plan_mr = self.browse_ref('medical_workflow.mr_knee')
        self.plan_ct = self.browse_ref('medical_workflow.ct_abdominal')
        self.plan_check_up = self.browse_ref('medical_workflow.basic_check_up')
        return res

    def test_recursion(self):
        action_obj = self.env['workflow.plan.definition.action']
        action_obj.create({
            'direct_plan_definition_id': self.plan_check_up.id,
            'name': self.plan_mr.name,
            'execute_plan_definition_id': self.plan_mr.id,
        })
        action_obj.create({
            'direct_plan_definition_id': self.plan_check_up.id,
            'name': self.plan_ct.name,
            'execute_plan_definition_id': self.plan_ct.id,
        })
        procedure_requests = self.env['medical.procedure.request'].search([
            ('patient_id', '=', self.patient.id)
        ])
        self.assertEqual(len(procedure_requests), 0)
        self.plan_check_up.execute_plan_definition({
            'patient_id': self.patient.id,
        })
        procedure_requests = self.env['medical.procedure.request'].search([
            ('patient_id', '=', self.patient.id)
        ])
        self.assertGreater(len(procedure_requests), 0)
