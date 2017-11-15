# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalAdministrationPractitioner(TransactionCase):

    def setUp(self):
        super(TestMedicalAdministrationPractitioner, self).setUp()
        self.practitioner_model = self.env['res.partner']
        self.role_model = self.env['medical.role']

    def test_security(self):
        role_vals = {
            'name': 'Nurse',
            'description': 'Nurse'
        }
        role_1 = self.role_model.create(role_vals)
        practitioner_vals = {
            'is_practitioner': True,
            'name': 'Nurse X',
            'practitioner_role_ids': [(6, 0, role_1.ids)]
        }
        practitioner_1 = self.practitioner_model.create(practitioner_vals)
        self.assertNotEquals(practitioner_1, False)
        self.assertNotEquals(practitioner_1.practitioner_role_ids, False)
