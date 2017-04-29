# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from mock import patch

from openerp.tests.common import TransactionCase
from openerp import fields


MOCK_DATETIME = 'openerp.addons.sale_stock_medical_prescription_us.'\
                'models.medical_prescription_order_line.datetime'


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()
        self.rx_line_3 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'medical_prescription_order_order_line_us_3'
        )
        self.procurement_1 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'procurement_order_medical_procurement_us_1'
        )
        # Auto-created procurement tied to rx_line_3
        self.procurement_0 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'medical_prescription_order_order_line_us_3'
        ).dispensed_ids[-1]

        self.rx_line_4 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'medical_prescription_order_order_line_us_4'
        )
        self.procurement_2 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'procurement_order_medical_procurement_us_2'
        )
        # Auto-created procurement tied to rx_line_4
        self.procurement_00 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'medical_prescription_order_order_line_us_4'
        ).dispensed_ids[-1]

        self.uom_day = self.env.ref(
            'medical_medication.product_uom_day'
        )
        self.uom_dozen = self.env.ref(
            'product.product_uom_dozen'
        )

        self.pharmacy_2 = self.env.ref(
            'sale_stock_medical_prescription_us.'
            'company_pharmacy_us_2'
        )

        self.patcher = patch(MOCK_DATETIME)
        self.mock_datetime = self.patcher.start()

        # 10 days after proc_1 and proc_2 date_planned
        self.mock_datetime.now.return_value = \
            fields.Datetime.from_string('2002-10-18')

    def tearDown(self):
        super(TestMedicalPrescriptionOrderLine, self).tearDown()
        self.patcher.stop()

    def test_no_duration_uom_id(self):
        """ Test no dispense_remain_day calcs if no duration_uom_id """
        self.rx_line_3.duration_uom_id = None
        self.assertFalse(
            self.rx_line_3.dispense_remain_qty,
        )

    def test_no_duration(self):
        """ Test no dispense_remain_day calcs if duration is 0 """
        self.rx_line_3.duration = 0
        self.assertFalse(
            self.rx_line_3.dispense_remain_qty,
        )

    def test_compute_dispense_remain_qty_no_procs(self):
        """ Test dispense_remain_qty 0 if no procs """
        self.rx_line_3.dispensed_ids = None
        self.assertEquals(
            self.rx_line_3.dispense_remain_qty,
            0,
        )

    def test_compute_dispense_remain_day_no_procs(self):
        """ Test dispense_remain_day 0 if no procs """
        self.rx_line_3.dispensed_ids = None
        self.assertEquals(
            self.rx_line_3.dispense_remain_day,
            0,
        )

    def test_compute_dispense_remain_qty_duration_uom_id_day(self):
        """ Test remaining units when duration_uom_id is day """
        self.rx_line_3.duration_uom_id = self.uom_day
        self.rx_line_3.duration = 200
        self.assertAlmostEqual(
            self.rx_line_3.dispense_remain_qty,
            7.8,
        )

    def test_compute_dispense_remain_day_uom_day(self):
        """ Test dispense_remain_day when duration_uom_id is day """
        self.rx_line_3.duration_uom_id = self.uom_day
        self.rx_line_3.duration = 200
        self.assertAlmostEqual(
            self.rx_line_3.dispense_remain_day,
            6.39,
            2,
        )

    def test_compute_dispense_remain_qty_0(self):
        """ Test dispense_remain_qty 0 if remaining_units < 0 """
        self.rx_line_3.duration_uom_id = self.uom_day
        self.rx_line_3.duration = 20
        self.assertEquals(
            self.rx_line_3.dispense_remain_qty,
            0,
        )

    def test_compute_dispense_remain_day_0(self):
        """ Test dispense_remain_day 0 if remaining_units < 0 """
        self.rx_line_3.duration_uom_id = self.uom_day
        self.rx_line_3.duration = 20
        self.assertEquals(
            self.rx_line_3.dispense_remain_day,
            0,
        )

    def test_compute_dispense_remain_qty_uom_year(self):
        """ Test remain_qty when duration_uom_id is 1 year """
        self.assertAlmostEqual(
            self.rx_line_3.dispense_remain_qty,
            13.32,
            2,
        )

    def test_compute_dispense_remain_day_uom_year(self):
        """ Test dispense_remain_qty when duration_uom_id is 1 year """
        self.assertAlmostEqual(
            self.rx_line_3.dispense_remain_day,
            19.94,
            2,
        )

    def test_compute_dispense_remain_qty_dispense_dozen(self):
        """ Test remain_qty when product_uom is dozen """
        self.procurement_2.product_uom = self.env.ref(
            'product.product_uom_dozen'
        )
        self.assertAlmostEqual(
            self.rx_line_4.dispense_remain_qty,
            112.53,
            2,
        )

    def test_compute_dispense_remain_day_dispense_dozen(self):
        """ Test remain_qty when product_uom is dozen """
        self.procurement_2.product_uom = self.env.ref(
            'product.product_uom_dozen'
        )
        self.assertAlmostEqual(
            self.rx_line_4.dispense_remain_day,
            150.55,
            2,
        )

    def test_compute_total_allowed_qty(self):
        """ Test total_allowed_qty correctly computed """
        self.assertEquals(
            self.rx_line_3.total_allowed_qty,
            244,
        )

    def test_compute_total_qty_remain(self):
        """ Test total_qty_remain correctly computed """
        self.assertEquals(
            self.rx_line_3.total_qty_remain,
            204,
        )

    def test_compute_refill_qty_remain_active_qty_more_than_qty(self):
        """ Test refill_qty_remain when active_dispense_qty > qty """
        self.procurement_1.product_qty = 62
        self.assertAlmostEqual(
            self.rx_line_3.refill_qty_remain,
            2.66,
            2,
        )

    def test_compute_refill_qty_remain_qty_0(self):
        """ Test refill_qty_remain when qty is 0 """
        self.rx_line_3.qty = 0
        self.assertEquals(
            self.rx_line_3.refill_qty_remain,
            3,
        )

    def test_can_dispense_true_allowed_dispenses(self):
        """ Test can_dispense True if allowed dispenses > 0 """
        self.assertTrue(
            self.rx_line_3.can_dispense,
        )

    def test_can_dispense_qty_cancel_state(self):
        """ Test can_dispense_qty correct with 1 cancel proc """
        self.procurement_1.state = 'cancel'
        self.assertEquals(
            self.rx_line_3.can_dispense_qty,
            41,
        )

    def test_can_dispense_qty_active_dispense_greater_than_qty(self):
        """ Test can_dispense_qty correct """
        self.pharmacy_2.medical_prescription_refill_threshold = 0.95
        self.rx_line_3.qty = 39
        self.assertAlmostEqual(
            self.rx_line_3.can_dispense_qty,
            5.68,
            2
        )

    def test_qty_pending_and_unused_higher_than_threshold(self):
        """ Test can_dispense_qty 0 if pending higher than threshold """
        self.rx_line_3.qty = 39
        self.assertEquals(
            self.rx_line_3.can_dispense_qty,
            0,
        )

    def test_can_dispense_pending_and_unused_higher_than_threshold(self):
        """ Test can_dispense_qty 0 if pending higher than threshold """
        self.rx_line_3.qty = 39
        self.assertFalse(
            self.rx_line_3.can_dispense,
        )
