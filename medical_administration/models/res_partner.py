# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import base64
import threading
from odoo import api, fields, models, tools


class Partner(models.Model):
    # FHIR Entity: Person (http://hl7.org/fhir/person.html)
    _inherit = 'res.partner'

    is_medical = fields.Boolean(
        default=False,
    )

    @api.model
    def _get_medical_identifiers(self):
        """
        It must return a list of triads of check field, identifier field and
        defintion function
        :return: list
        """
        return []

    @api.model
    def create(self, vals):
        for medical, check, identifier, definition in \
                self._get_medical_identifiers():
            if vals.get(check) and not vals.get(identifier):
                vals[identifier] = definition(vals)
        if not vals.get('image'):
            vals['image'] = self._get_partner_default_image(vals)
        return super(Partner, self).create(vals)

    @api.model
    def _get_partner_default_image(self, vals):
        if self._get_default_image_path(vals):
            return self._get_default_medical_image(vals)
        return super(Partner, self)._get_default_image(
            vals.get('type'), vals.get('is_company'), vals.get('parent_id'))

    @api.model
    def _get_default_image_path(self, vals):
        return False

    @api.model
    def _get_default_medical_image(self, vals):
        if getattr(threading.currentThread(), 'testing',
                   False) or self._context.get('install_mode'):
            return False
        image_path = self._get_default_image_path(vals)
        if not image_path:
            return False
        with open(image_path, 'rb') as f:
            image = f.read()
        return tools.image_resize_image_big(base64.b64encode(image))
