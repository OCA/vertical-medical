# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests.common import TransactionCase


class TestPrescriptionOrder(TransactionCase):

    def test_inherits_mail_thread(self):
        """ Test order correctly inherits mail thread """
        model_obj = self.env['medical.prescription.order']
        res = hasattr(model_obj, 'message_new')
        self.assertTrue(
            res,
            '\rGot: %s \rExpected: %s' % (
                res, True
            )
        )
