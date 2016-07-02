# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.exceptions import ValidationError
from openerp.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()

        self.human = self.env.ref('medical_patient_species.human')
        self.dog = self.env.ref('medical_patient_species.dog')
        partner = self.env['res.partner']

        self.patient_1 = self.env['medical.patient'].create({
            'name': 'Patient 1',
            'gender': 'm',
            'species_id': self.human.id,
            'parent_id': None,
            'is_person': True,
        })
        self.patient_2 = self.env['medical.patient'].create({
            'name': 'Patient 2',
            'gender': 'm',
            'species_id': self.dog.id,
            'parent_id': partner.search([('name', '=', 'Patient 1')]).id,
            'is_person': False,
        })

    def test_check_parent_id_exists_no_parent(self):
        ''' Pet with no parent_id should raise ValidationError '''
        self.patient_1.species_id = self.dog.id

        with self.assertRaises(ValidationError):
            self.patient_1._check_parent_id_exists()

    def test_check_parent_id_exists_with_parent(self):
        ''' Pet with parent_id should not raise ValidationError '''
        try:
            self.patient_2._check_parent_id_exists()
        except:
            self.fail('Should not raise exception if valid parent_id')
