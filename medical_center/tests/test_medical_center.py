# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalCenter(TransactionCase):

    def setUp(self):
        super(TestMedicalCenter, self).setUp()
        self.partner_center_1 = self.env.ref(
            'medical_center.partner_center_1'
        )
        self.medical_center_1 = self.env.ref(
            'medical_center.medical_center_1'
        )

    def test_is_center(self):
        """ It should set type to center on create """
        self.assertEqual(
            self.partner_center_1.type,
            'medical.center',
        )

    def test_is_company(self):
        """ Validate is_company is set to True on partner """
        self.assertTrue(
            self.partner_center_1.is_company,
        )

    def test_customer(self):
        """ Test customer is set to False on partner """
        self.assertFalse(
            self.partner_center_1.customer,
        )

    def test_create_vals_get_default_image_encoded(self):
        """ It should get the default image for entity on create. """
        Center = self.env['medical.center'].with_context(
            __image_create_allow=True,
        )
        vals = {'name': 'test'}
        center = Center.create(vals)
        self.assertTrue(center.image)

    def test_get_default_image_encoded(self):
        """ It should return the default image for the entity. """
        Center = self.env['medical.center']
        image = Center._get_default_image_encoded({})
        self.assertTrue(image)

    def test_allow_image_create_no_test(self):
        """ It should not perform default image manipulation when testing. """
        Center = self.env['medical.center']
        can_create = Center._allow_image_create({})
        self.assertFalse(can_create)
