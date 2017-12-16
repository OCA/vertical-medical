# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from psycopg2 import IntegrityError
from odoo.tests.common import TransactionCase


class TestMedicalDrugRoute(TransactionCase):

    def setUp(self):
        super(TestMedicalDrugRoute, self).setUp()
        self.drug_route_perfusion = self.env.ref('medical_medicament.route_33')
        self.drug_route_oral = self.env.ref('medical_medicament.route_34')

    def test_name_unique(self):
        """ Validate drug route unique name sql constraint """
        with self.assertRaises(IntegrityError):
            self.drug_route_perfusion.name = self.drug_route_oral.name

    def test_code_unique(self):
        """ Validate drug route unique code sql constraint """
        with self.assertRaises(IntegrityError):
            self.drug_route_perfusion.code = self.drug_route_oral.code
