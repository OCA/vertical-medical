# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http
from openerp.http import request

from openerp.addons.website_medical.controllers.main import (
    WebsiteMedical
)


class WebsiteMedical(WebsiteMedical):

    @http.route(
        ['/my/medical', '/medical'],
        type='http',
        auth="user",
        website=True
    )
    def my_medical(self, **kw):
        """ Add prescriptions to medical account page """
        response = super(WebsiteMedical, self).my_medical()
        partner_id = request.env.user.partner_id

        rx_obj = request.env['medical.prescription.order.line']
        rx_line_ids = rx_obj.search([
            ('patient_id.parent_id', 'child_of', [partner_id.id]),
        ])

        # @TODO: Real security solution
        response.qcontext.update({
            'prescription_order_lines': rx_line_ids.sudo(),
        })
        return response

    @http.route(
        '/medical/prescription/<int:rx_id>',
        type='http',
        auth='user',
        website=True,
        methods=['GET'],
    )
    def prescription_show(self, rx_id, **kwargs):
        # values = {
        #     'error': {},
        #     'error_message': [],
        #     'success_page': kwargs.get('success_page', '/my/medical')
        # }
        raise NotImplementedError()

    @http.route(
        ['/medical/prescription/<int:rx_id>/line/<int:rx_line_id>'],
        type='http',
        auth='user',
        website=True,
        methods=['GET'],
    )
    def prescription_line_show(self, rx_id, rx_line_id, **kwargs):
        # values = {
        #     'error': {},
        #     'error_message': [],
        #     'success_page': kwargs.get('success_page', '/my/medical')
        # }
        raise NotImplementedError()
