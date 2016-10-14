# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.patient_1 = self.env.ref(
            'medical.medical_patient_patient_1'
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
