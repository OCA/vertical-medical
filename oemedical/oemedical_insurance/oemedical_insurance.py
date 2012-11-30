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
from osv import osv
from osv import fields


class OeMedicalInsurance(osv.osv):
    _name = 'oemedical.insurance'

    _columns = {
        'name': fields.char(size=256, string='Name'),
        'category': fields.char(size=256, string='Category', required=True),
        'plan_id': fields.many2one('oemedical.insurance.plan', string='Plan',
        ),
        'insurance_type': fields.selection([
            ('state', 'State'),
            ('labour_union', 'Labour Union / Syndical'),
            ('private', 'Private'),
        ], string='Insurance Type'),
        'member_since': fields.date(string='Member since'),
        'company': fields.many2one('res.partner',
            string='Insurance Company', ),
        'number': fields.char(size=256, string='Number', required=True),
        'member_exp': fields.date(string='Expiration date'),
        'notes': fields.text(string='Extra Info'),
        'owner': fields.many2one('res.partner', string='Owner'),
    }

OeMedicalInsurance()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
