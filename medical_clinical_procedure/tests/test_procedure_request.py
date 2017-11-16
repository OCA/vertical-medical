# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase
from odoo.exceptions import UserError, Warning


class TestProcedureRequest(TransactionCase):
    def setUp(self):
        res = super(TestProcedureRequest, self).setUp()
        self.patient = self.browse_ref('medical_administration.patient_01')
        self.plan = self.browse_ref('medical_workflow.mr_knee')
        return res

    def test_procedure(self):
        procedure_requests = self.env['medical.procedure.request'].search([
            ('patient_id', '=', self.patient.id)
        ])
        self.assertEqual(len(procedure_requests), 0)
        self.env['medical.add.plan.definition'].create({
            'patient_id': self.patient.id,
            'plan_definition_id': self.plan.id
        }).run()
        procedure_requests = self.env['medical.procedure.request'].search([
            ('patient_id', '=', self.patient.id)
        ])
        self.assertGreater(len(procedure_requests), 0)
        self.env['procedure.request.make.procedure'].with_context(
            active_ids=procedure_requests.ids).create({}).make_procedure()
        procedures = self.env['medical.procedure'].search([
            ('procedure_request_id', 'in', procedure_requests.ids)
        ])
        self.assertEqual(len(procedure_requests), len(procedures))
        with self.assertRaises(UserError):
            self.env['procedure.request.make.procedure'].with_context(
                active_ids=procedure_requests.ids).create({}).make_procedure()
        for request in procedure_requests:
            self.assertEqual(request.procedure_count, 1)
            with self.assertRaises(Warning):
                request.unlink()
            action = request.action_view_procedure()
            self.assertEqual(
                action['context']['default_procedure_request_id'], request.id)

    def test_procedure_request_workflow(self):
        request = self.env['medical.procedure.request'].create({
            'patient_id': self.patient.id
        })
        self.assertNotEqual(request.internal_identifier, '/')
        procedure = request.generate_event()
        self.assertEqual(procedure.procedure_request_id.id, request.id)
        self.assertTrue(request.is_editable)
        self.assertEqual(request.state, 'draft')
        request.draft2active()
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
        request.active2completed()
        self.assertFalse(request.is_editable)
        self.assertEqual(request.state, 'completed')
        request.reactive()
        request.cancel()
        self.assertFalse(request.is_editable)
        self.assertEqual(request.state, 'cancelled')
