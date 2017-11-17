# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalLocation(TransactionCase):

    def setUp(self):
        super(TestMedicalLocation, self).setUp()
        self.medical_user_group = \
            self.env.ref('medical_base.group_medical_configurator')
        self.medical_user = self._create_user('medical_user',
                                              self.medical_user_group.id)
        self.location_model = self.env['medical.location']
        self.res_partner = self.env['res.partner']
        self.partner_location_1 = self._create_partner()
        self.medical_location_1 = \
            self._create_location(self.partner_location_1)

    def _create_partner(self):
        return self.res_partner.create({
            'name': 'test name',
            'street': 'test street',
        })

    def _create_location(self, partner):
        return self.location_model.create({
            'name': 'test name',
            'description': 'test description',
            'partner_id': partner.id,
            'state': 'active',
        })

    def test_is_company(self):
        """ Validate is_company is set to True on partner """
        self.assertTrue(
            self.medical_location_1.is_company,
        )

    def test_customer(self):
        """ Test customer is set to False on partner """
        self.assertFalse(
            self.medical_location_1.customer,
        )

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
        location_vals = {
            'name': 'Test',
            'description': 'This is a test location',
            'state': 'active',
        }
        location = self.location_model.sudo(self.medical_user).create(
            location_vals)
        self.assertNotEquals(location, False)
