# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http
from openerp.http import request

from openerp.addons.website_portal.controllers.main import website_account
from openerp.exceptions import ValidationError


class WebsiteAccount(website_account):

    @http.route(['/my/home'], type='http', auth="user", website=True)
    def account(self, **kw):
        """ Add patients to main account page """
        response = super(WebsiteAccount, self).account()
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

    def detail_vals(self, patient_id):
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        patient_id = request.env['medical.patient'].browse(patient_id)
        return {
            'countries': countries,
            'states': states,
            'patient': patient_id,
        }

    @http.route(
        ['/my/patients/<int:patient_id>'],
        type='http',
        auth='user',
        website=True,
    )
    def patient(self, patient_id=None, redirect=None, **post):
        values = {
            'error': {},
            'error_message': []
        }
        if patient_id is None:
            return request.redirect('/my/patients/new')
        values.update(self.detail_vals(patient_id))
        return request.website.render(
            'website_medical_patient.patient', values,
        )

    @http.route(
        ['/my/patients/new'],
        type='http',
        auth='user',
        website=True,
    )
    def patient_new(self, redirect=None, **post):
        values = {
            'error': {},
            'error_message': []
        }
        return request.website.render(
            'website_medical_patient.patient_new', values,
        )
