# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import Warning


class TestMedicalPatientSpecies(TransactionCase):

    def setUp(self):
        super(TestMedicalPatientSpecies, self).setUp()
        self.species_model = self.env['medical.patient.species']
        self.human = self.env.ref('medical_patient_species.human')
        self.dog = self.env.ref('medical_patient_species.dog')

    def new_species(self, update_vals=None):
        self.vals = {
            'name': 'Human',
        }
        if update_vals:
            self.vals.update(update_vals)
        return self.species_model.create(self.vals)

    def test_create_is_person(self):
        ''' Tests on creation if Human, is_person is True '''
        self.assertTrue(
            self.human.is_person, 'Should be True if Human'
        )

    def test_create_not_is_person(self):
        ''' Tests on creation if not Human, is_person is False '''
        self.assertFalse(
            self.dog.is_person, 'Should be False if not Human'
        )

    def test_unlink_human(self):
        ''' Test raises Warning if unlinking human '''
        with self.assertRaises(Warning):
            self.human.unlink()
