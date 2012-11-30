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


class ResPartner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        #'insurance_plan_ids': fields.one2many('oemedical.insurance.plan',
        #                                       'relation_id',
        #                                       string='Insurance Plans', ),
        'is_insurance_company': fields.boolean(string='Insurance Company'),
        'relationship': fields.char(size=256, string='Relationship',
            required=True),
        'insurance_company_type': fields.selection([
            ('state', 'State'),
            ('labour_union', 'Labour Union / Syndical'),
            ('private', 'Private'), ],
            string='Insurance Type'),
        'is_institution': fields.boolean(string='Institution'),
        'relative_id': fields.many2one('res.partner', string='Contact', ),
        'is_doctor': fields.boolean(string='Health Prof'),
        'is_patient': fields.boolean(string='Patient'),
        'alias': fields.char(size=256, string='Alias', required=True),
        'internal_user': fields.many2one('res.users',
            string='Internal User', ),
        'activation_date': fields.date(string='Activation date'),
        'lastname': fields.char(size=256, string='Last Name', required=True),
        'is_work': fields.boolean(string='Work'),
        'is_person': fields.boolean(string='Person'),
        'is_school': fields.boolean(string='School'),
        'is_pharmacy': fields.boolean(string='Pharmacy'),
        'ref': fields.char(size=256, string='SSN', required=True),
        #'insurance': fields.one2many('oemedical.insurance', 'relation_id',
        #                               string='Insurance', ),
    }

ResPartner()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
