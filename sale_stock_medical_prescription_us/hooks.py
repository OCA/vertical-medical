# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, SUPERUSER_ID


def _inherit_medication_template_vals(cr, registry):
    with cr.savepoint():
        env = api.Environment(cr, SUPERUSER_ID, {})
        medication_model = env['medical.patient.medication']
        medications = medication_model.search([])

        for medication in medications:
            medication.onchange_template_id()
