# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPrescriptionOrderLine(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrderLine, self).setUp()
        self.line_model = self.env['medical.prescription.order.line']
        self.advil_1 = self.env.ref(
            'medical_medicament.medical_medicament_advil_1'
        )
        self.patient_1 = self.env.ref(
            'medical.medical_patient_patient_1'
        )

    def test_name_search_medicament_name(self):
        """ Test returns line_ids matching medicament name """
        res = self.line_model.name_search(self.advil_1.name)
        res_len = len(res)
        self.assertEquals(
            res_len, 4,
        )

    def test_name_search_medicament_strength(self):
        """ Test returns line_ids matching medicament strength """
        res = self.line_model.name_search(self.advil_1.strength)
        res_len = len(res)
        self.assertEquals(
            res_len, 4,
        )

    def test_name_search_medicament_uom_name(self):
        """ Test returns line_ids matching medicament strength uom """
        res = self.line_model.name_search(self.advil_1.strength_uom_id.name)
        res_len = len(res)
        self.assertEquals(
            res_len, 6,
        )

    def test_name_search_medicament_drug_form_code(self):
        """ Test returns line_ids matching medicament drug form code """
        res = self.line_model.name_search(self.advil_1.drug_form_id.code)
        res_len = len(res)
        self.assertEquals(
            res_len, 4,
        )

    def test_name_search_patient_name(self):
        """ Test returns line_ids belonging to specified patient """
        res = self.line_model.name_search(self.patient_1.name)
        res_len = len(res)
        self.assertEquals(
            res_len, 2,
        )

    def test_name_search_none(self):
        """ Test returns all line_ids if blank search params """
        res = self.line_model.name_search()
        res_len = len(res)
        self.assertEquals(
            res_len, 6,
        )
