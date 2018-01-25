# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalPrescriptionOrder(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrder, self).setUp()
        self.rx_1 = self.env.ref(
            'medical_prescription.medical_prescription_prescription_order_1'
        )
        self.rx_6 = self.env.ref(
            'medical_prescription.medical_prescription_prescription_order_6'
        )

    def test_sequence_for_name(self):
        """ Test name created if there is none """
        self.assertTrue(self.rx_1.name)

    def test_compute_active(self):
        """ Test active is True if rx line_ids present """
        self.assertTrue(
            self.rx_1.active,
            'Should be True if line_ids present.\rGot: %s\rExpected: %s' % (
                self.rx_1.active, True
            )
        )

    def test_compute_active_line_ids_inactive(self):
        """ Test active is False if rx line_ids not active """
        self.rx_1.prescription_order_line_ids.write({'active': False})
        self.assertFalse(
            self.rx_1.active,
            'Should be False if line_ids inactive.\rGot: %s\rExpected: %s' % (
                self.rx_1.active, False
            )
        )

    def test_compute_active_no_line_ids(self):
        """ Test active is True if no rx line_ids """
        self.assertTrue(
            self.rx_6.active,
            'Should be True if no line_ids.\rGot: %s\rExpected: %s' % (
                self.rx_6.active, True
            )
        )
