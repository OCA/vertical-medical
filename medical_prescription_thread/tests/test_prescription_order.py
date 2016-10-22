# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestPrescriptionOrder(TransactionCase):

    def test_inherits_mail_thread(self):
        model_obj = self.env['medical.prescription.order']
        self.assertTrue(hasattr(model_obj, 'message_new'))
