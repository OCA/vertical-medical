# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http
from openerp.http import request

from openerp.addons.website_medical.controllers.main import (
    WebsiteMedical
)


class WebsiteMedical(WebsiteMedical):

    def _inject_medical_detail_vals(self, patient_id=0, **kwargs):
        vals = super(WebsiteMedical, self)._inject_medical_detail_vals(
            patient_id,
            **kwargs
        )
        species_ids = request.env['medical.patient.species'].search([])
        vals.update({
            'species': species_ids,
        })
        return vals
