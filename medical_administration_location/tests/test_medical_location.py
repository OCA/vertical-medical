# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests.common import TransactionCase


class TestMedicalLocation(TransactionCase):

    def test_location(self):
        location_vals = {
            'name': 'test name',
            'description': 'test description',
            'is_location': True,
        }
        location = self.env['res.partner'].create(location_vals)
        self.assertTrue(location.is_location)
