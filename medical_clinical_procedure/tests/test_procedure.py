# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase


class TestProcedure(TransactionCase):

    def setUp(self):
        res = super(TestProcedure, self).setUp()
        self.patient = self.browse_ref('medical_administration.patient_01')
        self.plan = self.browse_ref('medical_workflow.mr_knee')
        return res

    def open_procedure(self):
        procedure = self.env['medical.procedure'].create({
            'patient_id': self.patient.id,
        })
        self.assertEqual(procedure.state, 'preparation')
        procedure.preparation2in_progress()
        self.assertTrue(procedure.is_editable)
        self.assertEqual(procedure.state, 'in-progress')
        self.assertTrue(procedure.performed_initial_date)
        self.assertTrue(procedure.is_editable)
        return procedure

    def test_procedure_completed_flow(self):
        procedure = self.open_procedure()
        procedure.in_progress2suspended()
        self.assertEqual(procedure.state, 'suspended')
        self.assertFalse(procedure.is_editable)
        procedure.suspended2in_progress()
        self.assertEqual(procedure.state, 'in-progress')
        self.assertTrue(procedure.is_editable)
        procedure.in_progress2completed()
        self.assertEqual(procedure.state, 'completed')
        self.assertFalse(procedure.is_editable)
        self.assertTrue(procedure.performed_end_date)

    def test_procedure_aborted_flow(self):
        procedure = self.open_procedure()
        procedure.in_progress2aborted()
        self.assertEqual(procedure.state, 'aborted')
        self.assertFalse(procedure.is_editable)
