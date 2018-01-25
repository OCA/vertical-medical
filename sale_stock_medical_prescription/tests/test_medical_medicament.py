# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalMedicament(TransactionCase):

    def test_create_uses_product_type_product(self):
        """ Test medicament has type 'product' on creation """
        test_medicament = self.env['medical.medicament'].create({
            'name': 'Test Medicament',
            'drug_form_id': self.env.ref('medical_medicament.AEM').id,
        })
        self.assertEqual(test_medicament.type, 'product')
