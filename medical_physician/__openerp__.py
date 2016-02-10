# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Ken Mak <kmak@laslabs.com>
#    Copyright: 2014-2016 LasLabs, Inc. [https://laslabs.com]
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
    'name': 'Medical Physician',
    'version': '9.0.1.1.0',
    'author': "LasLabs, Odoo Medical Team, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical',
        'product',
    ],
    "website": "https://laslabs.com",
    "licence": "AGPL-3",
    "data": [
        'views/medical_physician_view.xml',
        'views/medical_specialty_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
        'wizard/medical_physician_unavailable_view.xml',
    ],
    "application": False,
    'installable': True,
}
