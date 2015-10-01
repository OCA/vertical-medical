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
    'name': 'Odoo Medical : Operational areas and sectors',
    'version': '8.0.1.0',
    'category': 'Medical',
    'author': "Odoo Medical Team, Odoo Community Association (OCA)",
    'depends': [
        'medical_emr',
    ],
    "website": "http://github.com/oca/vertical-medical",
    'data': [
        'security/ir.model.access.csv',
        'views/medical_operational_area_view.xml',
        'views/medical_operational_sector_view.xml',
        'views/medical_family_view.xml',
        'views/medical_operational_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
}
