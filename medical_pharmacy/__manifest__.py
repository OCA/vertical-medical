# -*- coding: utf-8 -*-
# Copyright 2016-2018 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Pharmacy',
    'summary': 'Support for storing pharmacy and pharmacist info',
    'version': '10.0.1.0.0',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'medical_center',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/medical_pharmacist.xml',
        'views/medical_pharmacy.xml',
        'views/medical_menu.xml',
    ],
    'demo': [
        'demo/medical_pharmacist.xml',
        'demo/medical_pharmacy.xml',
    ],
}
