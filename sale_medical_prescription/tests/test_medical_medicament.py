# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalMedicament(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicament, self).setUp()
        self.simv_1 = self.env.ref(
            'sale_medical_prescription.medical_medicament_simv_1'
        )
        self.simv_2 = self.env.ref(
            'sale_medical_prescription.medical_medicament_simv_2'
        )

    def test_compute_is_prescription_rx_categ_id(self):
        """ Test is_prescription True if categ_id is rx """
        self.assertTrue(
            self.simv_1.is_prescription,
        )

    def test_compute_is_prescription_desc_categ_id(self):
        """ Test is_prescription True if categ_id child of rx_categ_id """
        self.assertTrue(
            self.simv_2.is_prescription,
        )

    def test_compute_is_prescription_non_desc_categ_id(self):
        """ Test is_prescription False if categ_id not child of rx_categ_id """
        self.simv_2.categ_id = self.env.ref(
            'sale_medical_prescription.product_category_otc'
        )
        self.assertFalse(
            self.simv_2.is_prescription,
        )
