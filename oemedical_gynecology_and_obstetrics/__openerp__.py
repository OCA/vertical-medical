##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    OeMedical, HMS Opensource Solution
##############################################################################
#    Collaborators of this module:
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Coded by: Parthiv Patel <parthiv@techreceptives.com>
#    Coded by: Ruchir Shukla <ruchir@techreceptives.com>
#    Planifyied by: Parthiv Patel <parthiv@techreceptives.com>
#    Planifyied by: Nhomar Hernandéz <nhomar@vauxoo.com>
#
##############################################################################
#    This project is mantained by OeMEdical Team:
#    https://launchpad.net/oemedical
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

    'name': 'OeMedical : gynecology and obstetrics',
    'version': '1.0.1',
    'author': "OeMEdical Team,Odoo Community Association (OCA)",
    'category': 'Generic Modules/Others',
    'depends': ['oemedical'],
    'application': True,
    'description': """

About OeMedical gynecology and obstetrics
-----------------------------------------

- Ginecology
    - Mestrual History
- Detection
    - Mammography History
- PAP / COLPO
    - PAP History
    - Colposcopy History
- Obstetrics
    - Pregnancy history



""",
    "website": "http://launchpad.net/oemedical",
    "licence": "LGPL v3",
    "data": [
        'views/oemedical_gynecology_and_obstetrics_view.xml',
        # view has errors, please correct before enabling....
        'views/oemedical_menu.xml',
        'security/ir.model.access.csv',
    ],
    "demo": [

    ],
    'test': [
    ],
    'css': [
    ],
    'js': [
    ],
    'qweb': [
    ],
    "active": False,
    'installable': False,
}