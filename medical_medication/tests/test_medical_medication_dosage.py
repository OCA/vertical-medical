# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from psycopg2 import IntegrityError


class TestMedicalMedicationDosage(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicationDosage, self).setUp()
        self.dosage_1 = self.env.ref(
            'medical_medication.229797004'
        )

    def test_check_name_unique(self):
        """ Test non-unique name raises IntegrityError """
        with self.assertRaises(IntegrityError):
            self.dosage_1.name = '1 time per day in the morning'

    def test_check_non_unique_abbreviation(self):
        """ Test non-unique abbreviation raises ValidationError """
        with self.assertRaises(ValidationError):
            self.dosage_1.abbreviation = 'om'

    def test_check_unique_abbreviation(self):
        """ Test unique abbreviation does not raise ValidationError """
        try:
            self.dosage_1.abbreviation = 'test abbreviation'
            self.assertTrue(True)
        except ValidationError:
            self.fail(
                'Unique abbreviation should not raise ValidationError'
            )

    def test_check_unique_code(self):
        """ Test unique code does not raise ValidationError """
        try:
            self.dosage_1.code = 'test code'
            self.assertTrue(True)
        except ValidationError:
            self.fail(
                'Unique code should not raise ValidationError'
            )

    def test_check_non_unique_code(self):
        """ Test non-unique code raises ValidationError """
        with self.assertRaises(ValidationError):
            self.dosage_1.code = '396147000'
