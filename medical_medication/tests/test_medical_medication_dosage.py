# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError
from psycopg2 import IntegrityError


class TestMedicalMedicationDosage(TransactionCase):

    def setUp(self,):
        super(TestMedicalMedicationDosage, self).setUp()
        self.model_obj = self.env['medical.medication.dosage']
        self.vals = {
            'name': 'Test Dosage',
        }

    def _test_record(self, ):
        return self.model_obj.create(self.vals)

    def test_unique_abbreviation_if_defined(self, ):
        self.vals['abbreviation'] = 'TEST'
        self._test_record()
        with self.assertRaises(ValidationError):
            self.vals['name'] = 'TEST2'
            self._test_record()

    def test_unique_code_if_defined(self, ):
        self.vals['code'] = 'TEST'
        self._test_record()
        with self.assertRaises(ValidationError):
            self.vals['name'] = 'TEST2'
            self._test_record()

    def test_unique_name(self, ):
        self._test_record()
        with self.assertRaises(IntegrityError):
            self._test_record()
