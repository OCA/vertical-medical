# -*- coding: utf-8 -*-
# Copyright 2004 Tech-Receptives
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta


class MedicalPatient(models.Model):
    """
    The concept of Patient included in medical.
    """
    _name = 'medical.patient'
    _description = 'Medical Patient'
    _inherits = {'res.partner': 'partner_id'}

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
    active = fields.Boolean(
        default=True,
    )
    is_deceased = fields.Boolean(
        compute='_compute_is_deceased',
    )
    partner_id = fields.Many2one(
        string='Related Partner',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
        index=True,
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
        """
        Age computed depending of the birth date of the
        membership request
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

    @api.constrains('is_pregnant', 'gender')
    def _check_is_pregnant(self):
        for record in self:
            if record.is_pregnant and record.gender != 'female':
                raise ValidationError(_(
                    'Invalid selection - Only a `Female` may be pregnant.',
                ))

    @api.multi
    def action_invalidate(self):
        for record in self:
            record.active = False
            if not any(record.partner_id.patient_ids.mapped('active')):
                record.partner_id.active = False

    @api.model
    def create(self, vals):
        vals.update({
            'customer': True,
            'type': self._name,
        })
        if not vals.get('identification_code'):
            sequence = self.env['ir.sequence'].next_by_code(
                self._name,
            )
            vals['identification_code'] = sequence
        return super(MedicalPatient, self).create(vals)
