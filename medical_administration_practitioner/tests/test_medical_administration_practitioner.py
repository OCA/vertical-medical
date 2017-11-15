# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalAdministrationPractitioner(TransactionCase):

    def setUp(self):
        super(TestMedicalAdministrationPractitioner, self).setUp()
        self.practitioner_model = \
            self.env['medical.administration.practitioner']
        self.role_model = self.env['medical.role']
        self.medical_user_group = \
            self.env.ref('medical_base.group_medical_user')
        self.medical_user = self._create_user('medical_user',
                                              self.medical_user_group.id)

    def _create_user(self, name, group_ids):
        return self.env['res.users'].with_context(
            {'no_reset_password': True}).create(
            {'name': name,
             'password': 'demo',
             'login': name,
             'email': '@'.join([name, '@test.com']),
             'groups_id': [(6, 0, [group_ids])]
             })

    def test_security(self):
        role_vals = {
            'name': 'Nurse',
            'description': 'Nurse'
        }
        role_1 = self.role_model.create(role_vals)
        practitioner_vals = {
            'name': 'Nurse X',
            'role_ids': [(6, 0, role_1.ids)]
        }
        practitioner_1 = self.practitioner_model.sudo(self.medical_user).\
            create(practitioner_vals)
        self.assertNotEquals(practitioner_1, False)
