# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalInsuranceCompany(TransactionCase):

    def setUp(self,):
        super(TestMedicalInsuranceCompany, self).setUp()
        self.model_obj = self.env['medical.insurance.company']
        self.vals = {
            'name': 'Test Insurance Co',
        }

    def _new_record(self, ):
        return self.model_obj.create(self.vals)

    def test_is_insurance_company(self, ):
        ''' Validate is_insurance_company is set on partner '''
        rec_id = self._new_record()
        self.assertEqual(rec_id.type, 'medical.insurance.company')
