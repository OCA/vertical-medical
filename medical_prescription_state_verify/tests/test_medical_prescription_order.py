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

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError
import mock
import __builtin__


rx_mdl = '%s.%s' % ('openerp.addons.medical_base_history.models',
                    'medical_prescription_order')


class TestMedicalPrescriptionOrder(TransactionCase):

    def setUp(self,):
        super(TestMedicalHistoryType, self).setUp()
        self.model_obj = self.env['medical.prescription.order']
        self.line_vals = {
            
        }
        self.vals = {
            'patient_id': [(0, 0, {'name': 'Patient',})],
            'physician_id': [(0, 0, {'name': 'Physician'})],
            'prescription_order_line_ids': [(0, 0, self.line_vals)]
        }

    def _new_record(self, ):
        return self.model_obj.create(self.vals)

    def test_allowed_change_keys_is_list(self, ):
        self.assertIsInstance(
            self.model_obj._ALLOWED_CHANGE_KEYS, list
        )

    def test_allowed_change_states_is_list(self, ):
        self.assertIsInstance(
            self.model_obj._ALLOWED_CHANGE_STATES, list
        )

    def test_write_attrs_not_allowed_when_verified(self, ):
        record_id = self._new_record()
        record_id.state = 'verified'
        with self.assertRaises(ValidationError):
            record_id.write({'name': 'Not Happening.. Hopefully', })

    def test_write_state_not_allowed_when_verified(self, ):
        record_id = self._new_record()
        record_id.state = 'verified'
        state_id = self.env['medical.prescription.order.state'].create({
            'name': 'Testing123',
        })
        with self.assertRaises(ValidationError):
            record_id.write({'state_id': state_id.id, })

    @mock.patch('%s.__builtin__.super' % rx_mdl)
    def test_write_state_is_allowed_when_allowed(self, mk):
        record_id = self._new_record()
        record_id.state = 'verified'
        state_id = self.env['medical.prescription.order.state'].create({
            'name': 'Testing123',
            'type': 'cancel',
        })
        expect = {'state_id': state_id.id, }
        record_id.write(expect)
        mk.assert_called_with_args(expect)

    @mock.patch('%s.__builtin__.super' % rx_mdl)
    def test_write_is_allowed_when_not_verified(self, mk):
        record_id = self._new_record()
        state_id = self.env['medical.prescription.order.state'].create({
            'name': 'Testing123',
            'type': 'cancel',
        })
        expect = {'state_id': state_id.id,
                  'name': 'Testing123', }
        record_id.write(expect)
        mk.assert_called_with_args(expect)
