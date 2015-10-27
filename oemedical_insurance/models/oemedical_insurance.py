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


class OeMedicalInsurance(orm.Model):
    _name = 'oemedical.insurance'

    def _get_name(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = record.company.name
        return res


    _columns = {
        'name': fields.function(_get_name, type='char', string='Name', help="", multi=False),
        'company': fields.many2one('res.partner', 'Insurance Company', required=True),
        'patient_id':fields.many2one('medical.patient', 'Patient'),
        'plan_id': fields.many2one('oemedical.insurance.plan', string='Plan',  help='Insurance company plan'),
        'insurance_type': fields.selection([
            ('state', 'State'),
            ('labour_union', 'Labour Union / Syndical'),
            ('private', 'Private'),
        ], string='Insurance Type',select=True),
        'number': fields.char(size=256, string='Number', required=True),
        'member_since': fields.date(string='Member since'),
        'member_exp': fields.date(string='Expiration date'),
        'notes': fields.text(string='Extra Info'),
        'owner': fields.many2one('res.partner', string='Owner'),
    }

OeMedicalInsurance()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
