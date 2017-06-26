# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Practitioner',
    'version': '10.0.1.0.0',
    'summary': 'Defines medical practioners',
    'author': 'Eficent, Creu Blanca, LasLabs, '
              'Odoo Community Association (OCA)',
    'website': 'https://odoo-community.org/',
    'license': 'LGPL-3',
    'category': 'Medical',
    'depends': [
        'medical',
    ],
    'data': [
        'data/medical_role.xml',
        'views/medical_role.xml',
        'views/medical_practitioner.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
