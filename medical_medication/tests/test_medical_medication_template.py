# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalMedicationTemplate(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicationTemplate, self).setUp()
        self.med_template_1 = self.env.ref(
            'medical_medication.medical_medication_template_template_1'
        )

        self.med_template_2 = self.env.ref(
            'medical_medication.medical_medication_template_template_2'
        )

        self.med_template_3 = self.env.ref(
            'medical_medication.medical_medication_template_template_3'
        )

        self.med_template_4 = self.env.ref(
            'medical_medication.medical_medication_template_template_4'
        )

    def test_name_get_dosage_id(self):
        """ Test display_name if dosage_id name chosen """
        self.assertEquals(
            self.med_template_4.display_name, 'as needed',
            'Should show dosage_id name.\rGot: %s\rExpected: %s' % (
                self.med_template_4.display_name, 'as needed'
            )
        )

    def test_name_get_frequency(self):
        """ Test display_name if frequency chosen """
        self.assertEquals(
            self.med_template_1.display_name, '2 / Hour(s)',
            'Should show frequencies.\rGot: %s\rExpected: %s' % (
                self.med_template_1.display_name, '2 / Hour(s)'
            )
        )

    def test_name_get_pathology(self):
        """ Test display_name if pathology_id name chosen """
        self.assertEquals(
            self.med_template_2.display_name, 'Migraine',
            'Should show pathology name.\rGot: %s\rExpected: %s' % (
                self.med_template_2.display_name, 'Migraine'
            )
        )

    def test_name_get_medicament_id(self):
        """ Test display_name if medicament_id name chosen """
        self.assertEquals(
            self.med_template_3.display_name, 'Advil',
            'Should show medicament name.\rGot: %s\rExpected: %s' % (
                self.med_template_3.display_name, 'Advil'
            )
        )
