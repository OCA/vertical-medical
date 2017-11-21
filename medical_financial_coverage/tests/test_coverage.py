# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalCoverage(TransactionCase):

    def setUp(self):
        super(TestMedicalCoverage, self).setUp()
        self.medical_user_group = \
            self.env.ref('medical_base.group_medical_configurator')
        self.medical_user = self._create_user('medical_user',
                                              self.medical_user_group.id)
        self.patient_model = self.env['medical.patient']
        self.coverage_model = self.env['medical.coverage']
        self.coverage_template_model = self.env['medical.coverage.template']
        self.payor_model = self.env['res.partner']
        self.patient_1 = self._create_patient()
        self.patient_2 = self._create_patient()
        self.payor_1 = self._create_payor()

    def _create_user(self, name, group_ids):
        return self.env['res.users'].with_context(
            {'no_reset_password': True}).create(
            {'name': name,
             'password': 'demo',
             'login': name,
             'email': '@'.join([name, '@test.com']),
             'groups_id': [(6, 0, [group_ids])]
             })

    def _create_patient(self):
        return self.patient_model.create({
            'name': 'Test patient',
            'gender': 'female',
        })

    def _create_payor(self):
        return self.payor_model.create({
            'name': 'Test payor',
            'is_payor': True,
        })

    def _create_coverage_template(self, state=False):
        vals = {
            'name': 'test coverage template',
            'payor_id': self.payor_1.id,
        }
        if state:
            vals.update({'state': state, })
        coverage_template = self.coverage_template_model.create(vals)
        return coverage_template

    def _create_coverage(self, coverage_template, state=False, patient=False):
        vals = {
            'name': 'test coverage',
            'patient_id': self.patient_1.id,
            'coverage_template_id': coverage_template.id,
        }
        if state:
            vals.update({'state': state, })
        if patient:
            vals.update({'patient_id': patient.id, })
        coverage = self.coverage_model.create(vals)
        return coverage

    def test_security(self):
        coverage_template_vals = {
            'name': 'test coverage template',
            'payor_id': self.payor_1.id,
        }
        coverage_template = self.coverage_template_model.\
            sudo(self.medical_user).create(coverage_template_vals)
        self.assertNotEquals(coverage_template, False)
        coverage_vals = {
            'name': 'test coverage',
            'patient_id': self.patient_1.id,
            'subscriber_id': 'abc123',
            'coverage_template_id': coverage_template.id,
        }
        coverage = self.coverage_model.\
            sudo(self.medical_user).create(coverage_vals)
        self.assertEquals(coverage.subscriber_id, 'abc123')
        self.assertNotEquals(coverage, False)

    def test_create_coverage_for_a_patient(self):
        num_coverages = self.patient_1.coverage_count
        self.assertEquals(num_coverages, 0)
        self.patient_1.action_view_coverage()
        coverage_template = self._create_coverage_template()
        self.patient_1.coverage_ids = [(0, 0, {'name': 'test coverage',
                                               'coverage_template_id':
                                                   coverage_template.id, })]
        self.patient_1.action_view_coverage()
        self._create_coverage(coverage_template, 'active', self.patient_2)
        self.patient_2.action_view_coverage()

    def test_payor_coverage_template(self):
        template1 = self._create_coverage_template()
        template2 = self._create_coverage_template()
        templates = self.payor_1.coverage_template_ids.ids
        self.assertEqual(templates, [template1.id, template2.id])
        num = self.payor_1.coverage_template_count
        self.assertEqual(num, 2)

    def test_payor_navigation_to_coverage_template(self):
        # 0 coverage template
        num_coverages_temp = self.payor_1.coverage_template_count
        self.assertEquals(num_coverages_temp, 0)
        self.payor_1.action_view_coverage_template()
        # 1 coverage template
        self._create_coverage_template()
        self.payor_1._compute_coverage_template_count()
        num_coverages_temp = self.payor_1.coverage_template_count
        self.assertEquals(num_coverages_temp, 1)
        self.payor_1.action_view_coverage_template()
        # >1 coverage template
        self._create_coverage_template()
        self.payor_1._compute_coverage_template_count()
        num_coverages_temp = self.payor_1.coverage_template_count
        self.assertEquals(num_coverages_temp, 2)
        self.payor_1.action_view_coverage_template()

    def test_coverage_template_complete_flow(self):
        # draft2active
        coverage_template_1 = self._create_coverage_template('draft')
        self.assertEqual(coverage_template_1.state, 'draft')
        coverage_template_1.draft2active()
        self.assertFalse(coverage_template_1.is_editable)
        self.assertEqual(coverage_template_1.state, 'active')
        # draft2cancelled
        coverage_template_2 = self._create_coverage_template('draft')
        self.assertEqual(coverage_template_2.state, 'draft')
        coverage_template_2.draft2cancelled()
        self.assertFalse(coverage_template_2.is_editable)
        self.assertEqual(coverage_template_2.state, 'cancelled')
        # draft2enteredinerror
        coverage_template_3 = self._create_coverage_template('draft')
        self.assertEqual(coverage_template_3.state, 'draft')
        coverage_template_3.draft2enteredinerror()
        self.assertFalse(coverage_template_3.is_editable)
        self.assertEqual(coverage_template_3.state, 'entered-in-error')
        # active2cancelled
        coverage_template_4 = self._create_coverage_template('active')
        self.assertEqual(coverage_template_4.state, 'active')
        coverage_template_4.active2cancelled()
        self.assertFalse(coverage_template_4.is_editable)
        self.assertEqual(coverage_template_4.state, 'cancelled')
        # active2enteredinerror
        coverage_template_5 = self._create_coverage_template('active')
        self.assertEqual(coverage_template_5.state, 'active')
        coverage_template_5.active2enteredinerror()
        self.assertFalse(coverage_template_5.is_editable)
        self.assertEqual(coverage_template_5.state, 'entered-in-error')
        # cancelled2enteredinerror
        coverage_template_6 = self._create_coverage_template('cancelled')
        self.assertEqual(coverage_template_6.state, 'cancelled')
        coverage_template_6.cancelled2enteredinerror()
        self.assertFalse(coverage_template_6.is_editable)
        self.assertEqual(coverage_template_6.state, 'entered-in-error')
        # active2draft
        coverage_template_7 = self._create_coverage_template('active')
        self.assertEqual(coverage_template_7.state, 'active')
        coverage_template_7.active2draft()
        self.assertTrue(coverage_template_7.is_editable)
        self.assertEqual(coverage_template_7.state, 'draft')
        # cancelled2draft
        coverage_template_8 = self._create_coverage_template('cancelled')
        self.assertEqual(coverage_template_8.state, 'cancelled')
        coverage_template_8.cancelled2draft()
        self.assertTrue(coverage_template_8.is_editable)
        self.assertEqual(coverage_template_8.state, 'draft')
        # cancelled2active
        coverage_template_9 = self._create_coverage_template('cancelled')
        self.assertEqual(coverage_template_9.state, 'cancelled')
        coverage_template_9.cancelled2active()
        self.assertFalse(coverage_template_9.is_editable)
        self.assertEqual(coverage_template_9.state, 'active')

    def test_coverage_complete_flow(self):
        coverage_template = self._create_coverage_template()
        # draft2active
        coverage_1 = self._create_coverage(coverage_template, 'draft')
        self.assertEqual(coverage_1.state, 'draft')
        coverage_1.draft2active()
        self.assertFalse(coverage_1.is_editable)
        self.assertEqual(coverage_1.state, 'active')
        # draft2cancelled
        coverage_2 = self._create_coverage(coverage_template, 'draft')
        self.assertEqual(coverage_2.state, 'draft')
        coverage_2.draft2cancelled()
        self.assertFalse(coverage_2.is_editable)
        self.assertEqual(coverage_2.state, 'cancelled')
        # draft2enteredinerror
        coverage_3 = self._create_coverage(coverage_template, 'draft')
        self.assertEqual(coverage_3.state, 'draft')
        coverage_3.draft2enteredinerror()
        self.assertFalse(coverage_3.is_editable)
        self.assertEqual(coverage_3.state, 'entered-in-error')
        # active2cancelled
        coverage_4 = self._create_coverage(coverage_template, 'active')
        self.assertEqual(coverage_4.state, 'active')
        coverage_4.active2cancelled()
        self.assertFalse(coverage_4.is_editable)
        self.assertEqual(coverage_4.state, 'cancelled')
        # active2enteredinerror
        coverage_5 = self._create_coverage(coverage_template, 'active')
        self.assertEqual(coverage_5.state, 'active')
        coverage_5.active2enteredinerror()
        self.assertFalse(coverage_5.is_editable)
        self.assertEqual(coverage_5.state, 'entered-in-error')
        # cancelled2enteredinerror
        coverage_6 = self._create_coverage(coverage_template, 'cancelled')
        self.assertEqual(coverage_6.state, 'cancelled')
        coverage_6.cancelled2enteredinerror()
        self.assertFalse(coverage_6.is_editable)
        self.assertEqual(coverage_6.state, 'entered-in-error')
        # active2draft
        coverage_7 = self._create_coverage(coverage_template, 'active')
        self.assertEqual(coverage_7.state, 'active')
        coverage_7.active2draft()
        self.assertTrue(coverage_7.is_editable)
        self.assertEqual(coverage_7.state, 'draft')
        # cancelled2draft
        coverage_8 = self._create_coverage(coverage_template, 'cancelled')
        self.assertEqual(coverage_8.state, 'cancelled')
        coverage_8.cancelled2draft()
        self.assertTrue(coverage_8.is_editable)
        self.assertEqual(coverage_8.state, 'draft')
        # cancelled2active
        coverage_9 = self._create_coverage(coverage_template, 'cancelled')
        self.assertEqual(coverage_9.state, 'cancelled')
        coverage_9.cancelled2active()
        self.assertFalse(coverage_9.is_editable)
        self.assertEqual(coverage_9.state, 'active')
