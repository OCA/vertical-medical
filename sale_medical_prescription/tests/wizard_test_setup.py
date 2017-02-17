# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests.common import TransactionCase


class WizardTestSetup(TransactionCase):

    def setUp(self):
        super(WizardTestSetup, self).setUp()

        # Group 1
        self.rx_order_7 = self.env.ref(
            'sale_medical_prescription.'
            'medical_prescription_prescription_order_7'
        )
        self.order_7 = self.env.ref(
            'sale_medical_prescription.sale_order_medical_order_7'
        )
        self.rx_line_7 = self.env.ref(
            'sale_medical_prescription.medical_prescription_order_order_line_7'
        )
        self.line_7 = self.env.ref(
            'sale_medical_prescription.sale_order_medical_order_line_7'
        )
        self.rx_line_8 = self.env.ref(
            'sale_medical_prescription.medical_prescription_order_order_line_8'
        )
        self.line_8 = self.env.ref(
            'sale_medical_prescription.sale_order_medical_order_line_8'
        )

        # Group 2
        self.rx_order_8 = self.env.ref(
            'sale_medical_prescription.'
            'medical_prescription_prescription_order_8'
        )
        self.rx_line_9 = self.env.ref(
            'sale_medical_prescription.medical_prescription_order_order_line_9'
        )

        self.wizard_1 = self.env['medical.sale.wizard'].with_context(
            active_ids=[self.rx_line_7.id],
        ).create({})

        # Both tied to same rx_order
        self.wizard_2 = self.env['medical.sale.wizard'].with_context(
            active_ids=[self.rx_line_7.id, self.rx_line_8.id],
        ).create({})

        # rx_line_9 has different rx_order than 7 and 8
        self.wizard_3 = self.env['medical.sale.wizard'].with_context(
            active_ids=[
                self.rx_line_9.id,
                self.rx_line_8.id,
                self.rx_line_7.id,
            ]
        ).create({})

        self.order_date = '2016-12-13'
        self.wizard_1.date_order = self.order_date
        self.wizard_2.date_order = self.order_date
        self.wizard_3.date_order = self.order_date
