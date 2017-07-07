# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


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
