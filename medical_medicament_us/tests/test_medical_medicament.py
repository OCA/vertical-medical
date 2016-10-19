# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestMedicalMedicament(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicament, self).setUp()

        self.test_gcn = self.env['medical.medicament.gcn'].create({})
        self.test_drug_form = self.env.ref('medical_medicament.AEM')

    def _new_medicament(self, extra_values):
        base_values = {
            'drug_form_id': self.test_drug_form.id,
            'name': 'Test Medicament',
            'gcn_id': self.test_gcn.id,
        }
        base_values.update(extra_values)

        return self.env['medical.medicament'].create(base_values)

    def test_compute_brand_ids_no_gcn_id(self):
        '''It should return an empty recordset for medicaments without a GCN'''
        test_medicament = self._new_medicament({'gcn_id': None})

        self.assertFalse(test_medicament.brand_ids)

    def test_compute_brand_ids_no_matches(self):
        '''It should return empty recordset when there are no brand variants'''
        test_medicament = self._new_medicament({'gpi': '1'})

        self.assertFalse(test_medicament.brand_ids)

    def test_compute_brand_ids_valid_matches(self):
        '''It should return all matching medicaments, including self'''
        test_medicament = self._new_medicament({'gpi': '2'})
        test_medicament_2 = self._new_medicament({'gpi': '2'})
        self._new_medicament({'gpi': '1'})

        self.assertEqual(
            test_medicament.brand_ids.ids,
            [test_medicament.id, test_medicament_2.id],
        )

    def test_compute_generic_ids_no_gcn_id(self):
        '''It should return an empty recordset for medicaments without a GCN'''
        test_medicament = self._new_medicament({'gcn_id': None})

        self.assertFalse(test_medicament.generic_ids)

    def test_compute_generic_ids_no_matches(self):
        '''It should return empty recordset if there are no generic variants'''
        test_medicament = self._new_medicament({'gpi': '2'})

        self.assertFalse(test_medicament.generic_ids)

    def test_compute_generic_ids_valid_matches(self):
        '''It should return all matching medicaments, including self'''
        test_medicament = self._new_medicament({'gpi': '1'})
        test_medicament_2 = self._new_medicament({'gpi': '1'})
        self._new_medicament({'gpi': '2'})

        self.assertEqual(
            test_medicament.generic_ids.ids,
            [test_medicament.id, test_medicament_2.id],
        )
