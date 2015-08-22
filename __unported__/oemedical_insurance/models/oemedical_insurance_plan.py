# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
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
#/#############################################################################

from openerp.osv import fields, orm
from openerp.tools.translate import _


class OeMedicalInsurancePlan(orm.Model):
    _name = 'oemedical.insurance.plan'

    _columns = {
        'name': fields.char(
            string='Name',
            size=264,
            required=True,
            help='Insurance company plan'),
        'is_default': fields.boolean(
            string='Default plan',
            help='Check if this is the default plan when assigning this insurance'
            ' company to a patient'),
        'company': fields.many2one(
            'res.partner',
            string='Insurance Company',
            required=True),
        'notes': fields.text(
            string='Extra info'),
        'plan': fields.many2one(
            'product.product',
            string='Plan'),
    }

OeMedicalInsurancePlan()