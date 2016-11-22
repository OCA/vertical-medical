# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

import json


class WebsiteSale(WebsiteSale):

    form_name_map = {}

    @http.route(['/shop/payment'], type='http', auth="public", website=True)
    def payment(self, **post):
        """ Inject prescription_info stage if necessary """
        rx_step = request.env['ir.model.data'].xmlid_to_object(
            'website_sale_medical_prescription.prescription_info_option',
            raise_if_not_found=True
        )
        if rx_step.active and not post.get('__rx_pass__'):
            return request.redirect('/shop/checkout/medical/prescription')
        else:
            return super(WebsiteSale, self).payment(**post)

    @http.route(
        ['/shop/checkout/medical/prescription'],
        type='http',
        auth="public",
        website=True,
        methods=["GET"],
    )
    def get_cart_prescription_info(self, **kwargs):

        # check that cart is valid
        order_id = request.website.sale_get_order(context=request.env.context)
        redirection = self.checkout_redirection(order_id)
        if redirection:
            return redirection

        prescription_obj = request.env['medical.prescription.order.line']
        sale_line_ids = order_id.order_line.filtered(
            lambda r: (r.product_id.medicament_ids and
                       r.product_id.medicament_ids[0].is_prescription
                       )
        )
        missing_sale_line_ids = sale_line_ids.filtered(
            lambda r: not r.prescription_order_line_id
        )

        if not len(missing_sale_line_ids):
            return self.payment(__rx_pass__=True)

        partner_id = order_id.partner_id
        patient_ids = request.env['medical.patient'].search([
            '|',
            ('partner_id', 'child_of', partner_id.id),
            ('parent_id', 'child_of', partner_id.id),
        ])
        prescription_line_ids = prescription_obj.search([
            ('patient_id', 'in', [p.id for p in patient_ids]),
        ])

        # Sudo to circumvent website_published on Products
        prescription_line_ids = prescription_line_ids.sudo()

        values = {
            'website_sale_order': order_id,
            'sale_lines': sale_line_ids,
            'prescription_lines': prescription_line_ids,
            'user': request.env.user,
            'error': {},
        }

        return request.website.render(
            "website_sale_medical_prescription.prescription_details",
            values,
        )

    @http.route(
        ['/shop/checkout/medical/prescription'],
        type='http',
        auth="public",
        website=True,
        methods=["POST"],
    )
    def post_cart_prescription_info(self, **kwargs):
        order_id = request.website.sale_get_order(context=request.env.context)
        wizard_obj = request.env['medical.prescription.checkout']
        wizard_id = wizard_obj.search(
            [('order_id', '=', order_id.id)], limit=1,
        )
        if not wizard_id:
            wizard_id = wizard_obj.create({
                'order_id': order_id.id,
            })
        res = wizard_id.action_process_data(**kwargs)
        if not len(res['errors']):
            # Useless ID, but will provide form success
            res.update({
                'id': wizard_id.id,
            })

        return json.dumps(res)
