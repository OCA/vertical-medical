# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPhysician(TransactionCase):

    def setUp(self):
        super(TestMedicalPhysician, self).setUp()
        self.physician_id = self.env.ref(
            'medical_physician.medical_physician_physician_1'
        )

    def test_is_doctor(self):
        """ Test physician is doctor """
        self.assertEqual(
            self.physician_id.type,
            'medical.physician',
        )

    def test_sequence(self):
        """ Test physician code is set to sequence next_by_code if None """
        self.assertTrue(
            self.physician_id.code,
        )

    def test_physician_customer(self):
        """ Test customer set to False when creating physician """
        self.assertFalse(
            self.physician_id.customer,
        )
