# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

{
    'name': 'Medical Procedures',
    'summary': 'Adds notion of medical procedure used elsewhere in medical',
    'version': '10.0.1.0.0',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'medical',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/medical_procedure.xml',
    ],
    'demo': [
        'demo/medical_procedure.xml',
    ],
}
