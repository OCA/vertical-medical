# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) LasLabs, Inc [https://laslabs.com]. All Rights Reserved
#
##############################################################################
#
#    Collaborators of this module:
#       Written By: James Foster <jfoster@laslabs.com>
#
##############################################################################
#
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

    'name': 'Medical Pathology',
    'version': '9.0.2.0.0',
    'author': 'LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)',
    'maintainer': 'LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'medical',
    ],
    'website': 'https://laslabs.com/',
    'licence': 'AGPL-3',
    'data': [
        'views/medical_pathology_category_view.xml',
        'views/medical_pathology_group_view.xml',
        'views/medical_pathology_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        'tests/medical_pathology_category.yml',
        'tests/medical_pathology_group.yml',
        'tests/medical_pathology.yml',
    ],
    'installable': True,
    'auto_install': False,
}
