# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestMedicalAppointment(TransactionCase):

    def setUp(self):
        super(TestMedicalAppointment, self).setUp()
        vals = {
            'name': 'Test Patient',
            'email': 'testpatient@example.com',
        }
        self.patient_id = self.env['medical.patient'].create(vals)
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
        vals = {
            'name': 'default',
            'is_default': True,
        }
        self.env['medical.appointment.stage'].create(vals)
        vals = {
            'name': 'review',
            'is_default': False,
        }
        self.env['medical.appointment.stage'].create(vals)
        vals = {
            'name': 'cancelled',
            'is_default': False,
        }
        self.env['medical.appointment.stage'].create(vals)
        vals = {
            'name': 'Test Institution',
            'is_institution': True,
        }
        self.institution_id = self.env['res.partner'].create(vals)
        self.appointment_id = self._new_appointment()

    def _new_appointment(self, time='11:00:00', force=False):
        vals = {
            'name': 'Test Appointment %s' % time,
            'patient_id': self.patient_id.id,
            'physician_id': self.physician_id.id,
            'appointment_type': 'outpatient',
            'appointment_date': '2016-01-01 %s' % time,
            'institution_id': self.institution_id.id,
            'duration': 60,
            'force_schedule': force,
        }
        return self.env['medical.appointment'].create(vals)

    def test_default_stage_id(self):
        default_stage = self.appointment_id._default_stage_id()
        self.assertEqual('default', default_stage.name)

    def test_compute_appointment_end_date(self, ):
        expect = '2016-01-01 12:00:00'
        self.assertEqual(
            expect, self.appointment_id.appointment_end_date,
            'Did not correctly compute end date. Expect %s, Got %s' % (
                expect, self.appointment_id.appointment_end_date,
            )
        )

    def test_get_appointments_gets_correct_appointments(self):
        self._new_appointment('15:00:00')
        got = self.env['medical.appointment']._get_appointments(
            self.physician_id,
            self.institution_id,
            '2016-01-01 11:00:00',
            '2016-01-01 12:00:00',
        )
        self.assertIn(
            self.appointment_id, got,
            'Did not get correct appt. Expect %s, Got %s' % (
                self.appointment_id, got
            )
        )
        self.assertEqual(
            1, len(got),
            'Did not get correct amount of appointments. Expect %d Got %d' % (
                1, len(got)
            )
        )

    def test_clashes_state_to_review(self):
        self._new_appointment('11:30:00', True)
        self.env['medical.appointment']._set_clashes_state_to_review(
            self.physician_id,
            self.institution_id,
            '2016-01-01 11:00:00',
            '2016-01-01 12:00:00',
        )
        self.assertEquals('Pending Review', self.appointment_id.stage_id.name)

    def test_check_not_double_booking_raises_error_when_in_appt(self):
        ''' Appt created while another appt in progress should be rejected '''
        with self.assertRaises(ValidationError):
            self._new_appointment('11:30:00')

    def test_check_not_double_booking_raises_error_when_clash_with_apt(self):
        ''' Appt that will be in progress during already created rejected '''
        with self.assertRaises(ValidationError):
            self._new_appointment('10:30:00')

    def test_check_not_double_booking_no_error_when_not_booked(self):
        ''' Should not raise ValidationError '''
        self._new_appointment('15:00:00')
