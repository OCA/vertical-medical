# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPrescriptionOrder(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrder, self).setUp()
        self.rx_7 = self.env.ref(
            'sale_medical_prescription.'
            'medical_prescription_prescription_order_7'
        )

    def test_compute_verified(self):
        """ Test verify_user_id properly set to user """
        self.assertEquals(
            self.rx_7.verify_user_id.id,
            self.env.user.id,
        )
