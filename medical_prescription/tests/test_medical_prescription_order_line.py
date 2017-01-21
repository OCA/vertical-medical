# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


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
        self.rx_line_1 = self.env.ref(
            'medical_prescription.'
            'medical_prescription_order_order_line_1'
        )

    def test_default_name(self):
        """ Test name added to rx_line as default """
        self.assertTrue(self.rx_line_1.name)

    def test_name_search_medicament_name(self):
        """ Test returns line_ids matching medicament name """
        exp = self.line_model.search([
            ('medicament_id.product_id.name', 'ilike', self.advil_1.name)],
            limit=100,
        )
        res = self.line_model.name_search(self.advil_1.name)
        exp_len = len(exp)
        res_len = len(res)
        self.assertEquals(
            res_len, exp_len,
            'Should return lines matching product.\rGot: %s\rExpected: %s' % (
                res_len, exp_len
            )
        )

    def test_name_search_medicament_strength(self):
        """ Test returns line_ids matching medicament strength """
        exp = self.line_model.search([
            ('medicament_id.strength', 'ilike', self.advil_1.strength)],
            limit=100,
        )
        res = self.line_model.name_search(self.advil_1.strength)
        exp_len = len(exp)
        res_len = len(res)
        self.assertEquals(
            res_len, exp_len,
            'Should return lines matching strength.\rGot: %s\rExpected: %s' % (
                res_len, exp_len
            )
        )

    def test_name_search_medicament_uom_name(self):
        """ Test returns line_ids matching medicament strength uom """
        exp = self.line_model.search(
            [(
                'medicament_id.strength_uom_id.name',
                'ilike',
                self.advil_1.strength_uom_id.name,
            )],
            limit=100,
        )
        res = self.line_model.name_search(self.advil_1.strength_uom_id.name)
        exp_len = len(exp)
        res_len = len(res)
        self.assertEquals(
            res_len, exp_len,
            'Should return lines matching uom.\rGot: %s\rExpected: %s' % (
                res_len, exp_len
            )
        )

    def test_name_search_medicament_drug_form_code(self):
        """ Test returns line_ids matching medicament drug form code """
        exp = self.line_model.search(
            [(
                'medicament_id.drug_form_id.code',
                'ilike',
                self.advil_1.drug_form_id.code,
            )],
            limit=100,
        )
        res = self.line_model.name_search(self.advil_1.drug_form_id.code)
        exp_len = len(exp)
        res_len = len(res)
        self.assertEquals(
            res_len, exp_len,
            'Should find rx lines matching form.\rGot: %s\rExpected: %s' % (
                res_len, exp_len
            )
        )

    def test_name_search_patient_name(self):
        """ Test returns line_ids belonging to specified patient """
        exp = self.line_model.search([
            ('patient_id.name', 'ilike', self.patient_1.name)],
            limit=100,
        )
        res = self.line_model.name_search(self.patient_1.name)
        exp_len = len(exp)
        res_len = len(res)
        self.assertEquals(
            res_len, exp_len,
            'Should find rx lines matching patient.\rGot: %s\rExpected: %s' % (
                res_len, exp_len
            )
        )

    def test_name_search_none(self):
        """ Test returns all line_ids if blank search params """
        exp = self.line_model.search([])
        res = self.line_model.name_search()
        exp_len = len(exp)
        res_len = len(res)
        self.assertEquals(
            res_len, exp_len,
            'Should return all rx lines.\rGot: %s\rExpected: %s' % (
                res_len, exp_len
            )
        )
