# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import mock
from openerp.tests.common import TransactionCase


class TestMedicalPharmacy(TransactionCase):

    def setUp(self):
        super(TestMedicalPharmacy, self).setUp()
        self.pharmacy_4 = self.env.ref(
            'sale_medical_prescription.medical_pharmacy_4'
        )

    def test_compute_verified_by_id(self):
        """ Test verified_by_id properly set to user """
        self.assertEquals(
            self.pharmacy_4.verified_by_id.id,
            self.env.user.id,
        )

    @mock.patch('openerp.addons.sale_medical_prescription.'
                'models.medical_pharmacy.fields.Datetime')
    def test_compute_verified_date(self, mock_datetime):
        """ Test verified_date set with datetime """
        exp = '2016-12-13 05:15:23'
        mock_datetime.now.return_value = exp
        self.pharmacy_4.is_verified = True
        res = self.pharmacy_4.verified_date
        self.assertEquals(
            res, exp,
        )
