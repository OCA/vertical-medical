# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from mock import patch
from odoo import modules
from odoo.tests.common import TransactionCase

SUPER_FILE_PATH = 'odoo.addons.medical.models.medical_abstract_entity'
SUPER_PATH = SUPER_FILE_PATH + '.MedicalAbstractEntity._get_default_image_path'


class TestMedicalPractitioner(TransactionCase):

    def setUp(self):
        super(TestMedicalPractitioner, self).setUp()
        self.practitioner_model = self.env['medical.practitioner']
        self.role_model = self.env['medical.role']
        assitant_group = self.env.ref('medical.group_medical_assistant')
        self.medical_assistant = self._create_user('medical_assistant',
                                                   [assitant_group.id])

    def _create_user(self, name, group_ids):
        return self.env['res.users'].with_context(
            {'no_reset_password': True}).create(
            {'name': name,
             'password': 'demo',
             'login': name,
             'email': '@'.join([name, '@test.com']),
             'groups_id': [(6, 0, group_ids)]
             })

    def test_security(self):
        role_vals = {
            'name': 'Nurse',
            'description': 'Nurse'
        }
        role_1 = self.role_model.create(role_vals)
        practitioner_vals = {
            'name': 'Nurse X',
            'role_ids': [(6, 0, [role_1.ids])]
        }
        practitioner_1 = self.practitioner_model.sudo(
            self.medical_assistant).create(practitioner_vals)
        self.assertNotEquals(practitioner_1, False)
        self.assertEquals(practitioner_1.type, 'medical.practitioner')

    @patch(SUPER_PATH)
    def test_get_default_image_path_super_result(self, super_mock):
        """It should call super and return result if not falsy"""
        test_vals = 'Test Vals'
        super_mock.return_value = test_image_path = 'Test Image Path'
        result = self.practitioner_model._get_default_image_path(test_vals)

        super_mock.assert_called_once_with(test_vals)
        self.assertEquals(result, test_image_path)

    @patch(SUPER_PATH)
    def test_get_default_image_path_no_super_result_male(self, super_mock):
        """It should return correct path if result falsy and gender male"""
        super_mock.return_value = None
        result = self.practitioner_model._get_default_image_path({
            'gender': 'male',
        })

        expected = modules.get_module_resource(
            'medical_practitioner',
            'static/src/img',
            'practitioner-male-avatar.png',
        )
        self.assertEquals(result, expected)

    @patch(SUPER_PATH)
    def test_get_default_image_path_no_super_result_female(self, super_mock):
        """It should return correct path if result falsy and gender female"""
        super_mock.return_value = None
        result = self.practitioner_model._get_default_image_path({
            'gender': 'female',
        })

        expected = modules.get_module_resource(
            'medical_practitioner',
            'static/src/img',
            'practitioner-female-avatar.png',
        )
        self.assertEquals(result, expected)

    @patch(SUPER_PATH)
    def test_get_default_image_path_no_super_result_other(self, super_mock):
        """It should return male path if result falsy and gender other"""
        super_mock.return_value = None
        result = self.practitioner_model._get_default_image_path({
            'gender': 'other',
        })

        expected = modules.get_module_resource(
            'medical_practitioner',
            'static/src/img',
            'practitioner-male-avatar.png',
        )
        self.assertEquals(result, expected)

    @patch(SUPER_PATH)
    def test_get_default_image_path_no_super_result_none(self, super_mock):
        """It should return male path if result falsy and gender unspecified"""
        super_mock.return_value = None
        result = self.practitioner_model._get_default_image_path({})

        expected = modules.get_module_resource(
            'medical_practitioner',
            'static/src/img',
            'practitioner-male-avatar.png',
        )
        self.assertEquals(result, expected)
