# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalRequest(TransactionCase):
    def setUp(self):
        super(TestMedicalRequest, self).setUp()
        self.patient = self.env['medical.patient'].create({
            'name': 'Test Patient'
        })

    def test_views(self):
        # procedure
        procedure = self.env['medical.procedure.request'].create({
            'patient_id': self.patient.id
        })
        procedure._compute_procedure_request_ids()
        self.assertEqual(procedure.procedure_request_count, 0)
        procedure.with_context(
            inverse_id='active_id', model_name='medical.procedure.request')\
            .action_view_request()
        # 1 procedure
        procedure2 = self.env['medical.procedure.request'].create({
            'patient_id': self.patient.id,
            'procedure_request_id': procedure.id,
        })
        procedure._compute_procedure_request_ids()
        self.assertEqual(procedure.procedure_request_ids.ids,
                         [procedure2.id])
        self.assertEqual(procedure.procedure_request_count, 1)
        procedure.with_context(
            inverse_id='active_id', model_name='medical.procedure.request')\
            .action_view_request()
        # 2 procedure
        procedure3 = self.env['medical.procedure.request'].create({
            'patient_id': self.patient.id,
            'procedure_request_id': procedure.id,
        })
        procedure._compute_procedure_request_ids()
        self.assertEqual(procedure.procedure_request_count, 2)
        self.assertEqual(procedure.procedure_request_ids.ids, [procedure2.id,
                                                               procedure3.id])
        procedure.with_context(
            inverse_id='active_id', model_name='medical.procedure.request')\
            .action_view_request()
