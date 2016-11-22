# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()

        self.medical_patient_model = self.env['medical.patient']
        self.human = self.env.ref('medical_patient_species.human')
        self.dog = self.env.ref('medical_patient_species.dog')

    def new_patient(self, update_vals=None):
        self.vals = {
            'name': 'Patient',
            'species_id': self.human.id,
            'parent_id': None,
        }
        if update_vals:
            self.vals.update(update_vals)
        return self.medical_patient_model.create(self.vals)

    def test_check_parent_id_exists_no_parent(self):
        """ Test create pet with no parent_id raises ValidationError """
        with self.assertRaises(ValidationError):
            self.new_patient({'species_id': self.dog.id})

    def test_check_parent_id_exists_with_parent(self):
        """ Test create pet with parent_id not raises ValidationError """
        patient_1 = self.new_patient()
        try:
            self.new_patient({
                'species_id': self.dog.id,
                'parent_id': patient_1.partner_id.id,
            })
            self.assertTrue(True)
        except ValidationError:
            self.fail("Should not raise ValidationError if parent_id exists")

    def test_check_species_id(self):
        """ Test create medical patient no species raises ValidationError """
        patient = self.new_patient({'species_id': None})
        self.assertEquals(
            self.human.id,
            patient.species_id.id,
        )
