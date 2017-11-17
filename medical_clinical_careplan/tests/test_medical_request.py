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
        # care plans
        careplan = self.env['medical.careplan'].create({
            'patient_id': self.patient.id
        })
        careplan._compute_careplan_ids()
        self.assertEqual(careplan.careplan_count, 0)
        careplan.with_context(
            inverse_id='active_id', model_name='medical.careplan')\
            .action_view_request()
        # 1 care plan
        careplan2 = self.env['medical.careplan'].create({
            'patient_id': self.patient.id,
            'careplan_id': careplan.id,
        })
        careplan._compute_careplan_ids()
        self.assertEqual(careplan.careplan_ids.ids, [careplan2.id])
        self.assertEqual(careplan.careplan_count, 1)
        careplan.with_context(
            inverse_id='active_id', model_name='medical.careplan')\
            .action_view_request()
        # 2 care plans
        careplan3 = self.env['medical.careplan'].create({
            'patient_id': self.patient.id,
            'careplan_id': careplan.id,
        })
        careplan._compute_careplan_ids()
        self.assertEqual(careplan.careplan_count, 2)
        self.assertEqual(careplan.careplan_ids.ids, [careplan2.id,
                                                     careplan3.id])
        careplan.with_context(
            inverse_id='active_id', model_name='medical.careplan')\
            .action_view_request()
