# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import http
from openerp.http import request
from openerp.exceptions import ValidationError
from openerp.addons.base.ir.ir_qweb import nl2br

from openerp.addons.website_form.controllers.main import WebsiteForm as Ctrl
from openerp.addons.website_portal.controllers.main import website_account

import json
from psycopg2 import IntegrityError


import logging
_logger = logging.getLogger(__name__)


class WebsiteForm(Ctrl):
    # @TODO: Integrate this more w/ existing WebsiteForm instead of copy code

    def __init__(self, *args, **kwargs):
        super(WebsiteForm, self).__init__(*args, **kwargs)
        self._input_filters.update({
            'date': Ctrl.identity,
        })

    @http.route(
        ['/medical_website_form/<string:model_name>/<int:id>',
         '/medical_website_form/<string:model_name>/'],
        type='http',
        auth="user",
        methods=['POST'],
        website=True
    )
    def website_medical_form(self, model_name, **kwargs):
        model_record = request.env['ir.model'].search([
            ('model', '=', model_name),
            # ('website_form_access', '=', True),
        ])
        if not model_record:
            return json.dumps(False)

        try:
            data = self.extract_data(model_record, ** kwargs)
        # If we encounter an issue while extracting data
        except ValidationError, e:
            # I couldn't find a cleaner way to pass data to an exception
            return json.dumps({'error_fields' : e.args[0]})

        try:
            id_record = self.insert_or_update_record(
                request,
                model_record,
                data['record'],
                data['custom'],
                kwargs.get('id', 0),
                data.get('meta'),
            )
            if id_record:
                self.insert_attachment(
                    model_record, id_record, data['attachments'],
                )

        # Some fields have additionnal SQL constraints that we can't check generically
        # Ex: crm.lead.probability which is a float between 0 and 1
        # TODO: How to get the name of the erroneous field ?
        except IntegrityError:
            return json.dumps(False)

        request.session['form_builder_model'] = model_record.name
        request.session['form_builder_id']    = id_record

        return json.dumps({'id': id_record})

    @http.route(
        ['/medical_website_form/<string:model_name>/<int:id>',
         '/medical_website_form/<string:model_name>/'],
        type='http',
        auth="user",
        methods=['DELETE'],
        website=True
    )
    def website_medical_form_delete(self, model_name, **kwargs):
        model_record = request.env['ir.model'].search([
            ('model', '=', model_name),
            # ('website_form_access', '=', True),
        ])
        if not model_record:
            return json.dumps(False)
        rec_id = kwargs.get('id')
        if not rec_id:
            return json.dumps(False)
        rec_id = int(rec_id)
        _logger.debug('Rec_id %s', rec_id)
        record = request.env[model_record.model].browse(rec_id)
        try:
            record.action_invalidate()
        except ValidationError, e:
            # I couldn't find a cleaner way to pass data to an exception
            return json.dumps({'error_fields' : e.args[0]})
        return json.dumps({
            'rec_id': rec_id,
            'model_name': model_name,
        })

    def insert_or_update_record(self, request, model, values,
                                custom, rec_id=0, meta=None):

        _logger.debug(values)
        record = False
        if rec_id:
            if not isinstance(rec_id, int):
                rec_id = int(rec_id)
            record = request.env[model.model].browse(rec_id)
            _logger.debug('Writing %s with %s', record, values)
            record.write(values)
        if not record:
            record = request.env[model.model].create(values)

        if custom or meta:
            default_field = model.website_form_default_field_id
            default_field_data = values.get(default_field.name, '')
            custom_content = (default_field_data + "\n\n" if default_field_data else '') \
                           + (self._custom_label + custom + "\n\n" if custom else '') \
                           + (self._meta_label + meta if meta else '')

            # If there is a default field configured for this model, use it.
            # If there isn't, put the custom data in a message instead
            if default_field.name:
                if default_field.ttype == 'html' or model.model == 'mail.mail':
                    custom_content = nl2br(custom_content)
                record.update({default_field.name: custom_content})
            else:
                values = {
                    'body': nl2br(custom_content),
                    'model': model.model,
                    'message_type': 'comment',
                    'no_auto_thread': False,
                    'res_id': record.id,
                }
                mail_id = request.env['mail.message'].sudo().create(values)

        return record.id


class WebsiteAccount(website_account):

    def _format_date(self, date):
        if not date:
            return ""
        split = date.split('-')
        return '%s/%s/%s' % (split[1], split[2], split[0])

    def _inject_detail_vals(self):
        return {
            '_format_date': self._format_date,
        }
