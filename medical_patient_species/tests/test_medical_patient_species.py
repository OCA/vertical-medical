# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPatientSpecies(TransactionCase):

    def setUp(self):
        super(TestMedicalPatientSpecies, self).setUp()
        self.human = self.env.ref('medical_patient_species.human')
        self.dog = self.env.ref('medical_patient_species.dog')

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
