# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase


class TestCareplan(TransactionCase):
    def setUp(self):
        res = super(TestCareplan, self).setUp()
        self.patient = self.browse_ref('medical_administration.patient_01')
        self.plan = self.browse_ref('medical_workflow.mr_knee')
        return res

    def test_careplan_workflow(self):
        request = self.env['medical.careplan'].create({
            'patient_id': self.patient.id
        })
        self.assertNotEqual(request.internal_identifier, '/')
        self.assertTrue(request.is_editable)
        self.assertEqual(request.state, 'draft')
        self.assertFalse(request.start_date)
        request.draft2active()
        self.assertTrue(request.start_date)
        self.assertFalse(request.is_editable)
        self.assertEqual(request.state, 'active')
        request.active2suspended()
        self.assertFalse(request.is_editable)
        self.assertEqual(request.state, 'suspended')
        request.reactive()
        request.active2error()
        self.assertFalse(request.is_editable)
        self.assertEqual(request.state, 'entered-in-error')
        request.reactive()
        self.assertFalse(request.end_date)
        request.active2completed()
        self.assertFalse(request.is_editable)
        self.assertEqual(request.state, 'completed')
        self.assertTrue(request.end_date)
        request.reactive()
        request.cancel()
        self.assertFalse(request.is_editable)
        self.assertEqual(request.state, 'cancelled')

    def test_execute_plan(self):
        careplan = self.env['medical.careplan'].create({
            'patient_id': self.patient.id
        })
        self.env['medical.careplan.add.plan.definition'].create({
            'careplan_id': careplan.id,
            'plan_definition_id': self.plan.id
        }).run()
        procedure_requests = self.env['medical.procedure.request'].search([
            ('careplan_id', '=', careplan.id)
        ])
        self.assertGreater(len(procedure_requests), 0)
