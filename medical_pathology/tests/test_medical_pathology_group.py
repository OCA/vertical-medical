# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError


class TestMedicalPathologyGroup(TransactionCase):

    def setUp(self):
        super(TestMedicalPathologyGroup, self).setUp()
        self.pathology_group_1 = self.env.ref(
            'medical_pathology.medical_pathology_group_1'
        )

    def test_check_unique_code(self):
        """ Test non-unique codes raise IntegrityError """
        with self.assertRaises(IntegrityError):
            self.pathology_group_1.code = '[DEMO] MDG6'
