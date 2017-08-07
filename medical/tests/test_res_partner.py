# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()
        self.partner_1 = self.env.ref(
            'medical.res_partner_patient_1'
        )
        self.patient_1 = self.env.ref(
            'medical.medical_patient_patient_1'
        )

    def test_get_medical_entity(self):
        """ Test returns correct medical entity """
        self.partner_1.type = 'medical.patient'
        res = self.partner_1._get_medical_entity()
        self.assertEquals(
            res.partner_id,
            self.partner_1,
        )

    def test_get_medical_entity_no_type(self):
        """ Test returns nothing if no type """
        self.partner_1.type = None
        self.assertFalse(
            self.partner_1._get_medical_entity(),
        )

    def test_get_medical_entity_not_medical(self):
        """ Test returns nothing if not medical type """
        self.partner_1.type = 'invoice'
        self.assertFalse(
            self.partner_1._get_medical_entity(),
        )
