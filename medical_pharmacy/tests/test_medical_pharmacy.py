# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPharmacy(TransactionCase):

    def setUp(self,):
        super(TestMedicalPharmacy, self).setUp()
        self.model_obj = self.env['medical.pharmacy']
        self.vals = {
            'name': 'Test Pharm',
        }

    def _new_record(self, ):
        return self.model_obj.create(self.vals)

    def test_is_pharmacy(self, ):
        """ Validate is_pharmacy is set on partner """
        rec_id = self._new_record()
        self.assertTrue(rec_id.is_pharmacy)
