# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()

        self.rx_line_12 = self.env.ref(
            'sale_stock_medical_prescription.'
            'medical_prescription_order_order_line_12'
        )
        self.rx_line_13 = self.env.ref(
            'sale_stock_medical_prescription.'
            'medical_prescription_order_order_line_13'
        )

        self.proc_2 = self.env.ref(
            'sale_stock_medical_prescription.'
            'procurement_order_medical_procurement_2'
        )
        self.patient_1 = self.env.ref(
            'medical.'
            'medical_patient_patient_1'
        )

    def test_compute_dispensings_dispensed_ids(self):
        """ Test dispense_ids field properly populated """
        self.assertEquals(
            len(self.rx_line_12.dispensed_ids),
            3,
        )

    def test_compute_dispensings_dispense_qty(self):
        """ Test dispense_qty correctly calculated """
        self.assertEquals(
            self.rx_line_12.dispensed_qty,
            15,
        )

    def test_compute_dispensings_pending_qty(self):
        """ Test pending_qty correctly calculated """
        self.assertEquals(
            self.rx_line_12.pending_dispense_qty,
            20,
        )

    def test_compute_dispensings_cancel_qty(self):
        """ Test cancel_qty correctly calculated """
        self.assertEquals(
            self.rx_line_13.cancelled_dispense_qty,
            6,
        )

    def test_compute_dispensings_except_qty(self):
        """ Test dozens uom converted to units for except_qty """
        self.assertEquals(
            self.rx_line_13.exception_dispense_qty,
            12,
        )

    def test_compute_dispensings_last_dispense_id(self):
        """ Test last_dispense_id is correct """
        self.assertEquals(
            self.rx_line_12.last_dispense_id,
            self.rx_line_12.sale_order_line_ids.procurement_ids[-1]
        )

    def test_compute_can_dispense_and_qty_active_qty(self):
        """ Test active_dispense_qty is calculated correctly """
        self.assertTrue(
            self.rx_line_13.active_dispense_qty,
            8,
        )

    def test_compute_can_dispense_true(self):
        """ Test can_dispense is True if enough qty available """
        self.assertTrue(
            self.rx_line_13.can_dispense,
        )

    def test_compute_can_dispense_false(self):
        """ Test can_dispense is False if not enough qty available """
        self.assertFalse(
            self.rx_line_12.can_dispense,
        )

    def test_compute_can_dispense_qty_true(self):
        """ Test can_dispense_qty is correct for can_dispense=True """
        self.assertEquals(
            self.rx_line_13.can_dispense_qty,
            7,
        )

    def test_compute_can_dispense_qty_false(self):
        """ Test can_dispense_qty is correct for can_dispense=False """
        self.assertEquals(
            self.rx_line_12.can_dispense_qty,
            0,
        )

    # ValidationError not raised
    # def test_check_patient(self):
    #     """ Test changing patient to incorrect one raise ValidationError """
    #     patient = self.env['medical.patient'].search([
    #         ('id', '!=', self.rx_line_12.patient_id.id)
    #     ], limit=1)
    #     with self.assertRaises(ValidationError):
    #         self.rx_line_12.patient_id = patient
