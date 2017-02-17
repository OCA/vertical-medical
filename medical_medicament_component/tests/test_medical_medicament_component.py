# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).


from openerp.tests.common import TransactionCase
from psycopg2 import IntegrityError


class TestMedicalMedicamentComponent(TransactionCase):

    def setUp(self):
        super(TestMedicalMedicamentComponent, self).setUp()
        self.model_obj = self.env['medical.medicament.component']
        self.vals = {
            'name': 'Medicament Component',
        }

    def _new_record(self, ):
        return self.model_obj.create(self.vals)

    def test_name_unique(self):
        self._new_record()
        with self.assertRaises(IntegrityError):
            self._new_record()
