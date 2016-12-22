# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestHooks(TransactionCase):

    def test_post_init(self):
        '''It should convert pre-existing medicaments to new type'''
        test_medicament = self.env.ref(
            'medical_medicament.medical_medicament_advil_1'
        )

        self.assertEqual(test_medicament.type, 'product')
