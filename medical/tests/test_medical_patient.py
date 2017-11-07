# Copyright 2015 ACSONE SA/NV
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import mock

from odoo import fields
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

import logging
import math
_logger = logging.getLogger(__name__)

MOCK_PATH = 'odoo.addons.medical.models.medical_patient.date'


class TestMedicalPatient(TransactionCase):

    def setUp(self):
        super(TestMedicalPatient, self).setUp()
        self.patient_1 = self.env.ref('medical.medical_patient_patient_1')
        self.partner_patient_1 = self.env.ref('medical.res_partner_patient_1')
        self.patient_3 = self.env.ref('medical.medical_patient_patient_3')

    def test_sequence_for_identification_code(self):
        """ Test identification_code created if there is none """
        self.assertTrue(
            self.patient_1.identification_code,
        )

    def test_partner_is_patient(self):
        """ Test that medical patient type is correctly set on partner """
        self.assertEqual(
            self.partner_patient_1.type,
            'medical.patient',
        )

    def test_pregnant_male_raises_error(self):
        """ Test raises ValidationError if male pregnant """
        with self.assertRaises(ValidationError):
            self.patient_3.is_pregnant = True

    def test_pregnant_female_no_error(self):
        """ Test no ValidationError if female is pregnant """
        self.patient_1.is_pregnant = True
        self.assertTrue(True)

    def test_compute_age(self):
        """ Test compute_age with no special cases """
        now = datetime.now()
        birthdate_date = fields.Datetime.from_string(
            self.patient_1.birthdate_date,
        )
        delta = relativedelta(now, birthdate_date)
        age = '%s%s %s%s %s%s' % (
            delta.years, 'y',
            delta.months, 'm',
            delta.days, 'd',
        )
        self.assertEqual(
            self.patient_1.age, age,
        )

    def test_compute_age_patient_deceased(self):
        """ Test age properly set if patient deceased """
        self.assertEqual(
            self.patient_3.age, '36y 1m 20d (deceased)',
        )

    def test_compute_age_no_birthdate_date_set(self):
        """ Test age equals 'No DoB' if no birthdate_date present """
        self.patient_1.birthdate_date = None
        self.assertEqual(
            self.patient_1.age, 'No DoB',
        )

    def test_toggle_active(self):
        """ Test invalidate patient also invalidates partner """
        self.patient_1.toggle_active()
        self.assertEqual(
            [self.partner_patient_1.active, self.patient_1.active],
            [False, False],
        )
        self.patient_1.toggle_active()
        self.assertEqual(
            [self.partner_patient_1.active, self.patient_1.active],
            [True, True],
        )

    def test_patient_deceased_if_date_death_exists(self):
        """ Test deceased is True if value set on date_death """
        self.assertTrue(
            self.patient_3.is_deceased,
        )

    def test_patient_not_deceased_if_no_date_death(self):
        """ Test deceased is False if no value set on date_death """
        self.assertFalse(
            self.patient_1.is_deceased,
        )

    def test_create_as_partner(self):
        """ It should create the entity if created as a partner. """
        partner = self.env['res.partner'].create({
            'name': 'test',
            'type': 'medical.patient',
        })
        self.assertEqual(
            len(partner.patient_ids), 1,
        )

    def test_create_vals_get_default_image_encoded(self):
        """ It should get the default image for entity on create. """
        Patient = self.env['medical.patient'].with_context(
            __image_create_allow=True,
        )
        vals = {'name': 'test'}
        patient = Patient.create(vals)
        self.assertTrue(patient.image)

    def test_get_default_image_encoded(self):
        """ It should return the default image for the entity. """
        Patient = self.env['medical.patient']
        image = Patient._get_default_image_encoded({})
        self.assertTrue(image)

    def test_allow_image_create_no_test(self):
        """ It should not perform default image manipulation when testing. """
        Patient = self.env['medical.patient']
        can_create = Patient._allow_image_create({})
        self.assertFalse(can_create)

    def test_check_birthdate_date(self):
        """ It should not allow birth dates in the future. """
        now = datetime.now()
        with self.assertRaises(ValidationError):
            self.env['medical.patient'].create({
                'name': 'Future Baby',
                'birthdate_date': fields.Datetime.to_string(
                    now + timedelta(days=20),
                )
            })

    def test_search_age(self):
        """
        When patients are searched by age,
        it should return patients with the corresponding birth dates
        """
        birthdate = datetime.strptime(
            self.patient_1.birthdate_date, "%Y-%m-%d"
        ).date()
        current_date = date.today()
        delta = current_date - birthdate
        years = math.floor(delta.days/365)
        result = self.env['medical.patient'].search(
            [('age_years', '=', years)]
        )
        self.assertIn(self.patient_1, result)
        result = self.env['medical.patient'].search(
            [('age_years', '>=', years)]
        )
        self.assertIn(self.patient_1, result)
        result = self.env['medical.patient'].search(
            [('age_years', '<=', years)]
        )
        self.assertIn(self.patient_1, result)
        result = self.env['medical.patient'].search(
            [('age_years', '>', years)]
        )
        self.assertNotIn(self.patient_1, result)
        result = self.env['medical.patient'].search(
            [('age_years', '<', years)]
        )
        self.assertNotIn(self.patient_1, result)

    @mock.patch(MOCK_PATH)
    def test_search_age_on_birthday(self, date_mock):
        """Should correctly treat patients as being 1 year older on birthday"""
        date_mock.today.return_value = date(2017, 4, 15)
        p1_birth = date(2016, 4, 15)
        self.patient_1.birthdate_date = fields.Datetime.to_string(p1_birth)
        p3_birth = date(2015, 4, 16)
        self.patient_3.birthdate_date = fields.Datetime.to_string(p3_birth)

        result = self.env['medical.patient'].search([('age_years', '=', 1)])
        self.assertIn(self.patient_1, result)
        self.assertIn(self.patient_3, result)

    @mock.patch(MOCK_PATH)
    def test_search_age_end_of_month(self, date_mock):
        """Should return correct result when current date at end of month"""
        date_mock.today.return_value = date(2017, 4, 30)
        p1_birth = date(2015, 5, 1)
        self.patient_1.birthdate_date = fields.Datetime.to_string(p1_birth)

        result = self.env['medical.patient'].search([('age_years', '=', 1)])
        self.assertIn(self.patient_1, result)

    def test_toggle_is_pregnant(self):
        self.patient_1.write({'is_pregnant': False})
        self.patient_1.toggle_is_pregnant()
        self.patient_1.refresh()
        self.assertEqual(
            self.patient_1.is_pregnant, True
        )
