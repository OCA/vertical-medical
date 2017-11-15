# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import base64
import threading
from odoo import api, fields, models, tools


class MedicalAbstractPartner(models.AbstractModel):
    # FHIR entity: Person (https://www.hl7.org/fhir/person.html)
    _name = 'medical.abstract.partner'
    _inherit = ['medical.abstract', 'mail.thread']
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        required=True,
        ondelete='restrict'
    )

    @api.model
    def create(self, vals):
        if not vals.get('image'):
            vals['image'] = self._get_default_medical_image(vals)
        return super(MedicalAbstractPartner, self).create(vals)

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
