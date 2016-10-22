# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalPhysician(TransactionCase):

    def setUp(self, ):
        super(TestMedicalPhysician, self).setUp()
        vals = {
            'name': 'Test Specialty',
            'code': 'TS',
        }
        specialty_id = self.env['medical.specialty'].create(vals)
        vals = {
            'name': 'Test Physician',
            'specialty_id': specialty_id.id,
        }
        self.physician_id = self.env['medical.physician'].create(vals)

    def test_is_doctor(self, ):
        self.assertTrue(self.physician_id.is_doctor)

    def test_sequence(self, ):
        self.assertTrue(self.physician_id.code)
