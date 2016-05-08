# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestMedicalPrescriptionOrder(TransactionCase):

    def setUp(self):
        super(TestMedicalPrescriptionOrder, self).setUp()
        patient_id = self.env['medical.patient'].create({
            'name': 'Test Patient',
        })
        specialty_id = self.env['medical.specialty'].create({
            'name': 'Test Specialty',
        })
        physician_id = self.env['medical.physician'].create({
            'name': 'Test Physician',
            'specialty_id': specialty_id.id,
        })
        self.model_obj = self.env['medical.prescription.order']
        self.vals = {
            'patient_id': patient_id.id,
            'physician_id': physician_id.id,
        }

    def _new_record(self):
        return self.model_obj.create(self.vals)

    def test_allowed_change_keys_is_list(self):
        self.assertIsInstance(
            self.model_obj._ALLOWED_CHANGE_KEYS, list
        )

    def test_allowed_change_states_is_list(self):
        self.assertIsInstance(
            self.model_obj._ALLOWED_CHANGE_STATES, list
        )

    def test_write_attrs_not_allowed_when_verified(self):
        record_id = self._new_record()
        record_id.state_type = 'verified'
        with self.assertRaises(ValidationError):
            record_id.write({'name': 'Not Happening.. Hopefully', })

    def test_write_state_not_allowed_when_verified(self):
        record_id = self._new_record()
        record_id.state_type = 'verified'
        stage_id = self.env['medical.prescription.order.state'].create({
            'name': 'Testing123',
        })
        with self.assertRaises(ValidationError):
            record_id.write({'stage_id': stage_id.id, })

    def test_write_state_is_allowed_when_allowed(self):
        record_id = self._new_record()
        record_id.state_type = 'verified'
        stage_id = self.env['medical.prescription.order.state'].create({
            'name': 'Testing123',
            'type': 'cancel',
        })
        record_id.write({'stage_id': stage_id.id, })
        record_id.refresh()
        self.assertEquals('Testing123', record_id.stage_id.name)

    def test_write_is_allowed_when_not_verified(self):
        record_id = self._new_record()
        stage_id = self.env['medical.prescription.order.state'].create({
            'name': 'Testing123',
            'type': 'cancel',
        })
        record_id.write({'stage_id': stage_id.id, })
        record_id.refresh()
        self.assertEquals('Testing123', record_id.stage_id.name)
