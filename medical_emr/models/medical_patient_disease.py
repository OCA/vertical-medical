# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Ported to 8.0 by Dave Lasley - LasLabs (https://laslabs.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields, api


class MedicalPatientDisease(models.Model):
    _name = 'medical.patient.disease'
    _description = 'Medical Patient Disease'

    @api.one
    @api.depends('short_comment', 'pathology_id', 'pathology_id.name')
    def _compute_name(self):
        name = self.pathology_id.name
        if self.short_comment:
            name = '%s - %s' % (name, self.short_comment)
        self.name = name

    @api.one
    @api.depends('active')
    def _compute_expire_date(self):
        if self.active:
            self.expire_date = False
        else:
            self.expire_date = fields.Datetime.now()

    @api.one
    def action_invalidate(self):
        self.active = False

    @api.one
    def action_revalidate(self):
        self.active = True

    name = fields.Char(string='Name', compute='_compute_name', store=True)
    treatment_description = fields.Char(string='Treatment Description')
    expire_date = fields.Datetime(
        string='Expire Date', compute='_compute_expire_date', store=True)
    short_comment = fields.Char(string='Short Comment')
    pathology_id = fields.Many2one(
        comodel_name='medical.pathology', string='Pathology', select=True,
        required=True)
    physician_id = fields.Many2one(
        comodel_name='medical.physician', string='Physician', select=True)
    pcs_code = fields.Many2one(
        comodel_name='medical.procedure', string='Procedure code', select=True)
    patient_id = fields.Many2one(
        comodel_name='medical.patient', string='Patient', required=True,
        select=True)
    disease_severity = fields.Selection([
        ('1_mi', 'Mild'),
        ('2_mo', 'Moderate'),
        ('3_sv', 'Severe')
    ], string='Severity')
    state = fields.Selection([
        ('a', 'Acute'),
        ('c', 'Chronic'),
        ('u', 'Unchanged'),
        ('h', 'Healed'),
        ('i', 'Improving'),
        ('w', 'Worsening'),
    ], string='Status of the disease')
    allergy_type = fields.Selection([
        ('da', 'Drug Allergy'),
        ('fa', 'Food Allergy'),
        ('ma', 'Misc Allergy'),
        ('mc', 'Misc Contraindication'),
    ], string='Allergy type')
    weeks_of_pregnancy = fields.Integer(
        string='Contracted in pregnancy week #')
    age = fields.Integer(string='Age when diagnosed')
    active = fields.Boolean(default=True)
    is_infectious = fields.Boolean(string='Infectious Disease')
    is_allergy = fields.Boolean(string='Allergic Disease', default=True)
    is_pregnant = fields.Boolean(string='Pregnancy warning')
    is_on_treatment = fields.Boolean(string='Currently on Treatment')
    date_start_treatment = fields.Date(
        string='Treatment Start Date')
    date_stop_treatment = fields.Date(string='End of treatment date')
    diagnosed_date = fields.Date(string='Date of Diagnosis')
    healed_date = fields.Date(string='Healed')
    notes = fields.Text(string='Notes')
