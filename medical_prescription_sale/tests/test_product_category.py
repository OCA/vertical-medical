# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestProductCategory(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestProductCategory, self).setUp(*args, **kwargs)
        self.vals = {
            'name': 'TestCatParent',
        }

    def _new_record(self, vals=False):
        return self.env['product.category'].create(
            vals if vals else self.vals
        )

    def test_is_descendant_of_direct(self, ):
        parent_id = self._new_record()
        self.vals['parent_id'] = parent_id.id
        child_id = self._new_record()
        self.assertTrue(
            child_id._is_descendant_of(parent_id),
            'Direct product category inheritance is not detected',
        )

    def test_is_descendant_of_recurse(self, ):
        parent_id = self._new_record()
        self.vals['parent_id'] = parent_id.id
        child_id = self._new_record()
        self.vals['parent_id'] = child_id.id
        child_id = self._new_record()
        self.assertTrue(
            child_id._is_descendant_of(parent_id),
            'Recursive product category inheritance is not detected',
        )
