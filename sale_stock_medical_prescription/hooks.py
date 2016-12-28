# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import openerp


def post_init_hook_for_new_medicament_type_and_rx_line_uom(cr, registry):
    with cr.savepoint():
        cr.execute(
            """UPDATE product_template
            SET type = 'product'
            WHERE is_medicament = TRUE"""
        )
    # with cr.savepoint():
    #     rx_line_mod = registry['medical.prescription.order.line']
    #     rx_lines = rx_line_mod.search(
    #         cr, openerp.SUPERUSER_ID, [], {}
    #     )
    #     for line in rx_line_mod.browse(
    #             cr, openerp.SUPERUSER_ID, rx_lines, {}):
    #         line.dispense_uom_id = line.medicament_id.uom_id
