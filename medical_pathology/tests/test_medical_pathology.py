# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError


class TestMedicalPathology(TransactionCase):

    def setUp(self):
        super(TestMedicalPathology, self).setUp()
        self.pathology_1 = self.env.ref(
            'medical_pathology.medical_pathology_medical_pathology_1'
        )

    def test_check_unique_code(self):
        """ Test 2 same codes per code_type raises integrity error """
        with self.assertRaises(IntegrityError):
            self.pathology_1.code = 'B54'

    def test_check_recursive_parent(self):
        """ Test category recursive parent raises ValidationError """
        with self.assertRaises(ValidationError):
            self.pathology_1.parent_id = self.env.ref(
                'medical_pathology.medical_pathology_2'
            ).id
