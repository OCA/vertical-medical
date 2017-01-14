# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models, tools
from odoo.modules import get_module_resource
from odoo.exceptions import ValidationError


class MedicalPatient(models.Model):
    """
    The concept of Patient included in medical.
    """
    _name = 'medical.patient'
    _description = 'Medical Patient'
    _inherit = 'medical.abstract.entity'

    age = fields.Char(
        compute='_compute_age',
    )
    identification_code = fields.Char(
        string='Internal Identification',
        help='Patient Identifier provided by the Health Center.'
             '(different from the Social Security Number)',
    )
    general_info = fields.Text(
        string='General Information',
    )
    is_deceased = fields.Boolean(
        compute='_compute_is_deceased',
    )
    marital_status = fields.Selection([
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ('z', 'law marriage'),
    ], )
    is_pregnant = fields.Boolean(
        help='Check this if the patient if pregnant',
    )
    date_death = fields.Datetime(
        string='Deceased Date',
    )

    @api.multi
    def _compute_age(self):
        """ Age computed depending based on the birth date in the
         membership request.
        """
        now = datetime.now()
        for record in self:
            if record.birthdate_date:
                birthdate_date = fields.Datetime.from_string(
                    record.birthdate_date,
                )
                if record.is_deceased:
                    date_death = fields.Datetime.from_string(record.date_death)
                    delta = relativedelta(date_death, birthdate_date)
                    is_deceased = _(' (deceased)')
                else:
                    delta = relativedelta(now, birthdate_date)
                    is_deceased = ''
                years_months_days = '%d%s %d%s %d%s%s' % (
                    delta.years, _('y'), delta.months, _('m'),
                    delta.days, _('d'), is_deceased
                )
            else:
                years_months_days = _('No DoB')
            record.age = years_months_days

    @api.multi
    def _compute_is_deceased(self):
        for record in self:
            record.is_deceased = bool(record.date_death)

    @api.multi
    @api.constrains('is_pregnant', 'gender')
    def _check_is_pregnant(self):
        for record in self:
            if record.is_pregnant and record.gender != 'female':
                raise ValidationError(_(
                    'Invalid selection - Only a `Female` may be pregnant.',
                ))

    @api.model
    def _create_vals(self, vals):
        vals = super(MedicalPatient, self)._create_vals(vals)
        if not vals.get('identification_code'):
            Seq = self.env['ir.sequence']
            vals['identification_code'] = Seq.next_by_code(
                self._name,
            )
        vals.update({
            'customer': True,
        })
        return vals

    @api.model
    def _get_default_image(self, vals):
        res = super(MedicalPatient, self)._get_default_image(vals)
        if res:
            return res
        img_path = get_module_resource(
            'medical', 'static/src/img', 'patient-avatar.png',
        )
        with open(img_path, 'r') as image:
            base64_image = image.read().encode('base64')
        return tools.image_resize_image_big(base64_image)
