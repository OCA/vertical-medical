# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http
from openerp.http import request

from openerp.addons.website_medical.controllers.main import (
    WebsiteMedical
)
from openerp.exceptions import ValidationError


class WebsiteMedical(WebsiteMedical):

    @http.route(['/my/medical', '/medical'], type='http', auth="user", website=True)
    def my_medical(self, **kw):
        """ Add patients to medical account page """
        response = super(WebsiteMedical, self).my_medical()
        partner_id = request.env.user.partner_id

        patient_obj = request.env['medical.patient']
        patient_ids = patient_obj.search([
            '|',
            ('partner_id', '=', partner_id.id),
            ('parent_id', '=', partner_id.id),
        ])

        response.qcontext.update({
            'patients': patient_ids,
        })
        return response

    def _inject_medical_detail_vals(self, patient_id=0, **kwargs):
        vals = super(WebsiteMedical, self)._inject_medical_detail_vals()
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        patient_id = request.env['medical.patient'].browse(patient_id)
        if len(patient_id):
            partner_id = patient_id.partner_id
        else:
            partner_id = request.env.user.partner_id
        vals.update({
            'countries': countries,
            'states': states,
            'patient': patient_id,
            'patient_website_attr': 'website_url',
            'partner': partner_id,
        })
        return vals

    @http.route(
        ['/medical/patients/<int:patient_id>'],
        type='http',
        auth='user',
        website=True,
        methods=['GET'],
    )
    def patient(self, patient_id=None, redirect=None, **kwargs):
        values = {
            'error': {},
            'error_message': [],
            'success_page': kwargs.get('success_page', '/my/medical')
        }
        values.update(
            self._inject_medical_detail_vals(patient_id)
        )
        return request.website.render(
            'website_medical_patient.patient', values,
        )
