# -*- coding: utf-8 -*-
##############################################################################
#    Copyright (C) LasLabs, Inc [https://laslabs.com]. All Rights Reserved
##############################################################################
#    Collaborators of this module:
#       Written By: Dave Lasley <dave@laslabs.com>
#
##############################################################################
#    This project is mantained by Medical Team:
#    https://github.com/OCA/vertical-medical/
#
##############################################################################
#    It is a collaborative effort between several companies that want to join
#    efforts in have a proposal solid and strong in the Health Care environment
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
##############################################################################
{

    'name': 'Pharmacy',
    'version': '8.0.1.0',
    'author': "LasLabs, Odoo Medical Team, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'sale',
        'stock',
        'medical_prescription',
    ],
    "website": "http://github.com/oca/vertical-medical",
    "licence": "AGPL-3",
    "data": [
        # Views
        'views/medical_abstract_prescription_state_view.xml',
        'views/medical_prescription_order_line_state_view.xml',
        'views/medical_prescription_order_state_view.xml',
        'views/prescription_order_view.xml',
        'views/prescription_order_line_view.xml',
        'views/sale_order_view.xml',
        
        # Wizards
        'wizard/medical_prescription_to_sale_wizard_view.xml',
        'wizard/medical_sale_wizard_view.xml',
        
        # Menu & Access
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'test': [

    ],
    'installable': True,
    'auto_install': False,
}
