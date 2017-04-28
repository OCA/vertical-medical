# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp import api, SUPERUSER_ID


def _update_medicament_type(cr, registry):
    with cr.savepoint():
        cr.execute(
            """UPDATE product_template
            SET type = 'product'
            WHERE is_medicament = TRUE"""
        )

    with cr.savepoint():
        env = api.Environment(cr, SUPERUSER_ID, {})
        medication_model = env['medical.patient.medication']
        medications = medication_model.search([])

        for medication in medications:
            medication.onchange_template_id()
