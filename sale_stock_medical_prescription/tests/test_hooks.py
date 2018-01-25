# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestHooks(TransactionCase):

    def setUp(self):
        super(TestHooks, self).setUp()
        self.rx_line_13 = self.env.ref(
            'sale_stock_medical_prescription.'
            'medical_prescription_order_order_line_13'
        )
        self.medicament_amox_1 = self.env.ref(
            'sale_stock_medical_prescription.'
            'product_product_amoxicillin_1'
        )
        self.medication_template_10 = self.env.ref(
            'sale_stock_medical_prescription.'
            'medical_medication_template_template_10'
        )
        self.medication_10 = self.env.ref(
            'sale_stock_medical_prescription.'
            'medical_patient_medication_medication_10'
        )

    def test_post_init_medicament(self):
        """ It should convert pre-existing medicaments to new type """
        self.assertEqual(
            self.medicament_amox_1.type,
            'product',
        )

    def test_post_init_hook_magic_columns(self):
        """ Test template vals and medication vals are set the same """
        comparison_keys = [
            'medicament_id',
            'quantity',
            'dose_uom_id',
            'frequency',
            'frequency_uom_id',
            'frequency_prn',
            'duration',
            'duration_uom_id',
            'medication_dosage_id',
            'suggested_administration_hours',
        ]
        for k in comparison_keys:
            t_value = getattr(self.medication_10, k)
            m_value = getattr(self.medication_template_10, k)
            self.assertEqual(
                t_value, m_value,
                '%s not the same.\rMedication: %s\rTemplate: %s' % (
                    k, t_value, m_value
                )
            )
