# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import base64
import threading
from odoo import api, fields, models, tools
from odoo.modules import get_module_resource


class MedicalPatient(models.Model):
    # FHIR Entity: Patient (http://hl7.org/fhir/patient.html)
    _name = 'medical.patient'
    _inherit = ['medical.abstract', 'mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        required=True,
        ondelete='restrict',
    )

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')],
    )   # FHIR Field: gender
    # https://www.hl7.org/fhir/valueset-administrative-gender.html)
    marital_status = fields.Selection(
        [
            ('s', 'Single'),
            ('m', 'Married'),
            ('w', 'Widowed'),
            ('d', 'Divorced'),
            ('l', 'Separated'),
        ]
    )   # FHIR Field: maritalStatus
    # https://www.hl7.org/fhir/valueset-marital-status.html
    birth_date = fields.Date(
        string='Birth date',
    )   # FHIR Field: birthDate
    deceased_date = fields.Date(
        string='Deceased date',
    )   # FHIR Field: deceasedDate
    is_deceased = fields.Boolean(
        compute='_compute_is_deceased',
    )   # FHIR Field: deceasedBoolean

    @api.depends('deceased_date')
    def _compute_is_deceased(self):
        for record in self:
            record.is_deceased = bool(record.deceased_date)

    @api.model
    def _get_internal_identifier(self, vals):
        return self.env['ir.sequence'].next_by_code('medical.patient') or '/'

    @api.model
    def _get_default_image_path(self, vals):
        icon = 'patient-male-avatar.png'
        if vals.get('gender', 'female') == 'female':
            icon = 'patient-female-avatar.png'
        return get_module_resource(
            'medical_administration', 'static/src/img', icon)

    @api.model
    def create(self, vals):
        if not vals.get('image'):
            vals['image'] = self._get_default_medical_image(vals)
        return super(MedicalPatient, self).create(vals)

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

    @api.multi
    def open_parent(self):
        """ Utility method used to add an "Open Parent" button in partner
        views """
        self.ensure_one()
        address_form_id = self.env.ref('base.view_partner_address_form').id
        return {'type': 'ir.actions.act_window',
                'res_model': 'res.partner',
                'view_mode': 'form',
                'views': [(address_form_id, 'form')],
                'res_id': self.parent_id.id,
                'target': 'new',
                'flags': {'form': {'action_buttons': True}}}
