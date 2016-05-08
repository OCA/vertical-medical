# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _
from datetime import datetime
from dateutil.relativedelta import relativedelta


class MedicalPatient(models.Model):
    '''
    The concept of Patient included in medical.
    '''
    _name = 'medical.patient'
    _description = 'Medical Patient'
    _inherits = {'res.partner': 'partner_id', }

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
    dob = fields.Date(
        string='Date of Birth',
    )
    dod = fields.Datetime(
        string='Deceased Date',
    )
    active = fields.Boolean(
        default=True,
    )
    deceased = fields.Boolean()
    partner_id = fields.Many2one(
        string='Related Partner',
        comodel_name='res.partner',
        required=True,
        ondelete='cascade',
        index=True,
    )
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female'),
    ], )
    medical_center_id = fields.Many2one(
        string='Medical Center',
        comodel_name='res.partner',
        domain="[('is_institution', '=', True)]",
    )
    marital_status = fields.Selection([
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ('z', 'law marriage'),
    ], )

    @api.multi
    def _compute_age(self):
        """
        Age computed depending of the birth date of the
        membership request
        """
        now = datetime.now()
        for rec_id in self:
            if rec_id.dob:
                dob = fields.Datetime.from_string(rec_id.dob)

                if rec_id.deceased:
                    dod = fields.Datetime.from_string(rec_id.dod)
                    delta = relativedelta(dod, dob)
                    deceased = _(' (deceased)')
                else:
                    delta = relativedelta(now, dob)
                    deceased = ''
                years_months_days = '%s%s %s%s %s%s%s' % (
                    delta.years, _('y'), delta.months, _('m'),
                    delta.days, _('d'), deceased
                )
            else:
                years_months_days = _('No DoB !')
            rec_id.age = years_months_days

    @api.multi
    def action_invalidate(self):
        for rec_id in self:
            rec_id.active = False
            rec_id.partner_id.active = False

    @api.model
    @api.returns('self', lambda value: value.id)
    def create(self, vals):
        vals['is_patient'] = True
        if not vals.get('identification_code'):
            sequence = self.env['ir.sequence'].next_by_code('medical.patient')
            vals['identification_code'] = sequence
        return super(MedicalPatient, self).create(vals)
