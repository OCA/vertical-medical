# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestPrescriptionOrderLine(TransactionCase):

    def test_inherits_mail_thread(self):
        model_obj = self.env['medical.prescription.order.line']
        self.assertTrue(hasattr(model_obj, 'message_new'))
