# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def post_init_hook_for_new_medicament_type(cr, registry):
    with cr.savepoint():
        cr.execute(
            '''UPDATE product_template
            SET type = 'product'
            WHERE is_medicament = TRUE'''
        )
