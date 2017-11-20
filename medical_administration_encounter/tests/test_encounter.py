# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalEncounter(TransactionCase):

    def setUp(self):
        super(TestMedicalEncounter, self).setUp()
        self.medical_user_group = \
            self.env.ref('medical_base.group_medical_configurator')
        self.medical_user = self._create_user('medical_user',
                                              self.medical_user_group.id)
        self.patient_model = self.env['medical.patient']
        self.location_model = self.env['medical.location']
        self.encounter_model = self.env['medical.encounter']
        self.patient_1 = self._create_patient()
        self.location_1 = self._create_location()

    def _create_patient(self):
        return self.patient_model.create({
            'name': 'Test patient',
            'gender': 'female',
        })

    def _create_location(self):
        return self.location_model.create({
            'name': 'Test location',
        })

    def _create_user(self, name, group_ids):
        return self.env['res.users'].with_context(
            {'no_reset_password': True}).create(
            {'name': name,
             'password': 'demo',
             'login': name,
             'email': '@'.join([name, '@test.com']),
             'groups_id': [(6, 0, [group_ids])]
             })

    def _create_encounter(self, state):
        return self.encounter_model.create({
            'name': 'test encounter',
            'patient_id': self.patient_1.id,
            'location_id': self.location_1.id,
            'state': state,
        })

    def test_security(self):
        encounter_vals = {
            'name': 'test encounter',
            'patient_id': self.patient_1.id,
            'location_id': self.location_1.id,
            'state': 'arrived',
        }
        encounter = self.encounter_model.sudo(self.medical_user).create(
            encounter_vals)
        self.assertNotEquals(encounter, False)

    def test_encounter_complete_flow(self):
        encounter_vals = {
            'name': 'test encounter',
            'patient_id': self.patient_1.id,
            'location_id': self.location_1.id,
            'state': 'planned',
        }
        encounter = self.encounter_model.create(encounter_vals)
        self.assertEqual(encounter.state, 'planned')
        encounter.planned2arrived()
        self.assertTrue(encounter.is_editable)
        self.assertEqual(encounter.state, 'arrived')
        encounter.arrived2inprogress()
        self.assertFalse(encounter.is_editable)
        self.assertEqual(encounter.state, 'in-progress')
        encounter.inprogress2onleave()
        self.assertFalse(encounter.is_editable)
        self.assertEqual(encounter.state, 'onleave')
        encounter.onleave2finished()
        self.assertFalse(encounter.is_editable)
        self.assertEqual(encounter.state, 'finished')

    def test_encounter_cancelled_flow(self):
        # planned2cancelled
        encounter_1 = self._create_encounter('planned')
        self.assertEqual(encounter_1.state, 'planned')
        encounter_1.planned2cancelled()
        self.assertFalse(encounter_1.is_editable)
        self.assertEqual(encounter_1.state, 'cancelled')
        # arrived2cancelled
        encounter_2 = self._create_encounter('arrived')
        self.assertEqual(encounter_2.state, 'arrived')
        encounter_2.arrived2cancelled()
        self.assertFalse(encounter_2.is_editable)
        self.assertEqual(encounter_2.state, 'cancelled')
        # inprogress2cancelled
        encounter_3 = self._create_encounter('in-progress')
        self.assertEqual(encounter_3.state, 'in-progress')
        encounter_3.inprogress2cancelled()
        self.assertFalse(encounter_3.is_editable)
        self.assertEqual(encounter_3.state, 'cancelled')
        # onleave2cancelled
        encounter_4 = self._create_encounter('onleave')
        self.assertEqual(encounter_4.state, 'onleave')
        encounter_4.onleave2cancelled()
        self.assertFalse(encounter_4.is_editable)
        self.assertEqual(encounter_4.state, 'cancelled')
