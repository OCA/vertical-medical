# -*- coding: utf-8 -*-
# #############################################################################
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
# #############################################################################

from openerp.osv import fields, orm


class ProductProduct(orm.Model):
    _inherit = 'product.product'

    _columns = {
        'is_vaccine': fields.boolean(string='Vaccine', help='Check if the '
                                     'product is a vaccine'),
        'is_medical_supply': fields.boolean(string='Medical Supply',
                                            help='Check if the product is a '
                                            'medical supply'),
        'is_insurance_plan': fields.boolean(string='Insurance Plan',
                                            help='Check if the product is an '
                                            'insurance plan'),
    }
