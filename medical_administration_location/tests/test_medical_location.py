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

    def _create_location(self, partner, state=False):
        location_vals = {
            'name': 'test name',
            'description': 'test description',
            'partner_id': partner.id,
        }
        if state:
            location_vals.update({'state': state})
        location = self.location_model.create(location_vals)
        return location

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

    def test_location_check_complete_flow(self):
        # active2suspended
        location_1 = self._create_location(self.partner_location_1)
        self.assertEqual(location_1.state, 'active')
        location_1.active2suspended()
        self.assertFalse(location_1.is_editable)
        self.assertEqual(location_1.state, 'suspended')
        # suspended2active
        location_2 = self._create_location(
            self.partner_location_1, 'suspended')
        self.assertEqual(location_2.state, 'suspended')
        location_2.suspended2active()
        self.assertTrue(location_2.is_editable)
        self.assertEqual(location_2.state, 'active')
        # active2inactive
        location_3 = self._create_location(self.partner_location_1)
        self.assertEqual(location_3.state, 'active')
        location_3.active2inactive()
        self.assertFalse(location_3.is_editable)
        self.assertEqual(location_3.state, 'inactive')
        # inactive2active
        location_4 = self._create_location(
            self.partner_location_1, 'inactive')
        self.assertEqual(location_4.state, 'inactive')
        location_4.inactive2active()
        self.assertTrue(location_4.is_editable)
        self.assertEqual(location_4.state, 'active')
        # suspended2inactive
        location_5 = self._create_location(
            self.partner_location_1, 'suspended')
        self.assertEqual(location_5.state, 'suspended')
        location_5.suspended2inactive()
        self.assertFalse(location_5.is_editable)
        self.assertEqual(location_5.state, 'inactive')
