# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalMedicament(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicament, self).setUp()

        self.advil_us_1 = self.env.ref(
            'medical_medicament_us.medical_medicament_advil_us_1'
        )
        self.gcn_demo_us_2 = self.env.ref(
            'medical_medicament_us.medical_medicament_gcn_us_2'
        )

    def test_compute_brand_ids_no_gcn_id(self):
        """ Test returns an empty recordset for medicaments without a GCN """
        self.advil_us_1.gcn_id = None
        self.assertEquals(
            len(self.advil_us_1.brand_ids),
            0,
        )

    def test_compute_brand_ids_no_matches(self):
        """ Test returns empty recordset when there are no brand variants """
        self.advil_us_1.gpi = '1'
        self.assertEquals(
            len(self.advil_us_1.brand_ids),
            0,
        )

    def test_compute_brand_ids_valid_matches(self):
        """ Test returns all matching medicaments, including self """
        self.assertEquals(
            len(self.advil_us_1.brand_ids),
            1,
        )

    def test_compute_generic_ids_no_gcn_id(self):
        """ Test returns an empty recordset for medicaments without a GCN """
        self.advil_us_1.gpi = '1'
        self.advil_us_1.gcn_id = None
        self.assertEquals(
            len(self.advil_us_1.generic_ids),
            0,
        )

    def test_compute_generic_ids_no_matches(self):
        """ Test returns empty recordset if there are no generic variants """
        self.assertEquals(
            len(self.advil_us_1.generic_ids),
            0,
        )

    def test_compute_generic_ids_valid_matches(self):
        """ Test returns all matching medicaments, including self """
        self.advil_us_1.gpi = '1'
        self.assertEquals(
            len(self.advil_us_1.generic_ids),
            1,
        )
