# -*- coding: utf-8 -*-
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from psycopg2 import IntegrityError

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMedicalPathology(TransactionCase):

    def test_check_unique_code(self):
        """ Test 2 same codes per code_type raises integrity error """
        pathology = self.env.ref(
            'medical_pathology.medical_pathology_medical_pathology_1'
        )
        with self.assertRaises(IntegrityError):
            pathology.code = '[DEMO] B54'

    def test_check_recursive_parent(self):
        """ Test category recursive parent raises ValidationError """
        parent = self.env.ref(
            'medical_pathology.medical_pathology_medical_pathology_A00',
        )
        with self.assertRaises(ValidationError):
            parent.parent_id = self.env.ref(
                'medical_pathology.medical_pathology_medical_pathology_A00_0',
            ).id
