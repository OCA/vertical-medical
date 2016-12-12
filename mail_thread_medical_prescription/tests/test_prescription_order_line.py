# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestPrescriptionOrderLine(TransactionCase):

    def test_inherits_mail_thread(self):
        """ Test order line correctly inherits mail thread """
        model_obj = self.env['medical.prescription.order.line']
        res = hasattr(model_obj, 'message_new')
        self.assertTrue(
            res,
            '\rGot: %s \rExpected: %s' % (
                res, True
            )
        )
