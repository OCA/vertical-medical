# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.patient_1 = self.env.ref(
            'medical.medical_patient_patient_1'
        )
        self.lang = 'en_US'
        self.lang_obj = self.env['res.lang'].search([('code', '=', self.lang)])
        self.lang_obj.date_format = '%m/%d/%Y'

    def test_change_date_format(self):
        """ Test date format changed in display_name if adjusted """
        self.lang_obj.date_format = '%Y-%m-%d'
        self.assertEquals(
            self.patient_1.display_name, 'Emma Fields [1920-02-23]',
            'Should correctly adjust date format.\rGot: %s\rExpected: %s' % (
                self.patient_1.display_name, 'Emma Fields [1920-02-23]'
            )
        )

    def test_name_includes_dob(self):
        """ Test display name includes dob if present """
        self.assertEquals(
            self.patient_1.display_name, 'Emma Fields [02/23/1920]',
            'Should include dob in display name.\rGot: %s\rExpected: %s' % (
                self.patient_1.display_name, 'Emma Fields [02/23/1920]'
            )
        )

    def test_name_without_dob(self):
        """ Test display name includes [No DoB] if no dob present """
        self.patient_1.dob = None
        self.assertEquals(
            self.patient_1.display_name, 'Emma Fields [No DoB]',
            'Should include [No DoB].\rGot: %s\rExpected: %s' % (
                self.patient_1.display_name, 'Emma Fields [No DoB]'
            )
        )

    def test_name_no_lang(self):
        """ Test for a default date format if none existing on lang """
        self.lang_obj.date_format = False
        self.assertEquals(
            self.patient_1.display_name, 'Emma Fields [02/23/1920]',
            'Should include dob in display name.\rGot: %s\rExpected: %s' % (
                self.patient_1.display_name, 'Emma Fields [02/23/1920]'
            )
        )
