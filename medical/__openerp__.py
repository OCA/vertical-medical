# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    Odoo Medical, HMS Opensource Solution
#
##############################################################################
#
#    Collaborators of this module:
#    8.0 & 9.0: Dave Lasley <dave@laslabs.com>
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Coded by: Parthiv Patel <parthiv@techreceptives.com>
#    Coded by: Ruchir Shukla <ruchir@techreceptives.com>
#    Coded by: Mario Arias   <support@cysfuturo.com>
#    Planifyied by: Parthiv Patel <parthiv@techreceptives.com>
#    Planifyied by: Nhomar Hernandéz <nhomar@vauxoo.com>
#
##############################################################################
#
#    This project is mantained by Odoo Community Association:
#    http://github.com/oca/vertical-medical
#
##############################################################################
#
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
    'name': 'Odoo Medical',
    'version': '9.0.2.0.0',
    'category': 'Medical',
    'depends': [
        'base',
        'product',
    ],
    'author': 'LasLabs, Odoo Medical Team, Odoo Community Association (OCA)',
    'website': 'http://github.com/oca/vertical-medical',
    'license': 'AGPL-3',
    'data': [
        'data/ir_sequence_data.xml',
        'views/res_partner_view.xml',
        'wizard/medical_physician_unavailable_view.xml',
        'views/medical_physician_view.xml',
        'views/medical_patient_view.xml',
        'views/medical_specialty_view.xml',
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'views/medical_menu.xml',
    ],
    'test': [
        'tests/physician.yml',
        'tests/patient.yml',
        'tests/partners.yml',
        'tests/physician_speciality.yml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
