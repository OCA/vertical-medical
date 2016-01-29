# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import mock
from openerp.tests.common import TransactionCase
from openerp.addons.base.res.res_partner import res_partner


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
        ''' Validate is_pharmacy is set on partner '''
        rec_id = self._new_record()
        self.assertTrue(rec_id.is_pharmacy)

    def test_onchange_state_passthru(self, ):
        ''' Validate that onchange_state is passed thru to partner '''
        rec_id = self._new_record()
        with mock.patch.object(res_partner, 'onchange_state') as mk:
            expect = 'Expect'
            rec_id.onchange_state(expect)
            mk.assert_called_once_with(expect)
