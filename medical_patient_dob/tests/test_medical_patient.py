# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):
    def setUp(self, ):
        super(TestMedicalPatient, self).setUp()
        vals = {
            'name': 'Patient 1',
            'gender': 'm',
            'dob': '1970-01-01'
        }
        self.patient_id = self.env['medical.patient'].create(vals)

    def test_name_includes_dob(self, ):
        self.assertEquals(
            self.patient_id.name_get()[0][1], 'Patient 1 [01/01/1970]',
            'Should display name and date of birth'
        )

    def test_name_without_dob(self, ):
        self.patient_id.write({'dob': None})
        self.patient_id.refresh()
        self.assertEquals(
            self.patient_id.name_get()[0][1], 'Patient 1 [No DoB]',
            'Should display name and date of birth'
        )
