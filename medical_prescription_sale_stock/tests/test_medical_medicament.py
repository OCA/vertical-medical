# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalMedicament(TransactionCase):

    def test_create_uses_product_type_product(self):
        test_medicament = self.env['medical.medicament'].create({
            'name': 'Test Medicament',
            'drug_form_id': self.env.ref('medical_medicament.AEM').id,
        })

        self.assertEqual(test_medicament.type, 'product')
