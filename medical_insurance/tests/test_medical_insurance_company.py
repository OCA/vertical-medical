# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import mock
from openerp.tests.common import TransactionCase
from openerp.addons.base.res.res_partner import res_partner


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
        self.assertTrue(rec_id.is_insurance_company)

    def test_onchange_state_passthru(self, ):
        ''' Validate that onchange_state is passed thru to partner '''
        rec_id = self._new_record()
        with mock.patch.object(res_partner, 'onchange_state') as mk:
            expect = 'Expect'
            rec_id.onchange_state(expect)
            mk.assert_called_once_with(expect)
