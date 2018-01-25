# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestCrmLead(TransactionCase):

    def setUp(self):
        super(TestCrmLead, self).setUp()

        self.crm_lead_1 = self.env.ref(
            'sale_crm_medical_prescription.crm_lead_medical_lead_1'
        )
        self.rx_order_9 = self.env.ref(
            'sale_crm_medical_prescription.'
            'medical_prescription_prescription_order_9'
        )
        self.rx_order_10 = self.env.ref(
            'sale_crm_medical_prescription.'
            'medical_prescription_prescription_order_10'
        )

    def test_compute_prescription_order(self):
        """ Test prescription orders properly calculated """
        self.assertEquals(
            [self.rx_order_9.id, self.rx_order_10.id],
            self.crm_lead_1.prescription_order_ids.ids
        )

    def test_compute_patient_ids(self):
        """ Test patient ids properly calculated """
        patient = self.env.ref(
            'sale_crm_medical_prescription.'
            'medical_patient_patient_10'
        )
        self.assertEquals(
            [patient.id],
            self.crm_lead_1.patient_ids.ids,
        )

    def test_compute_is_prescription(self):
        """ Test is_prescription set to True """
        self.assertTrue(
            self.crm_lead_1.is_prescription
        )
