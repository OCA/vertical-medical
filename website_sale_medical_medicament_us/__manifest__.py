# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medicament Sales - Brand/Generic Links',
    'summary': 'Links to brand/generic alternatives on medicament shop pages',
    'version': '10.0.1.0.0',
    'category': 'Medical',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': [
        'medical_medicament_us',
        'website_sale_medical_medicament',
    ],
    'data': [
        'views/website_sale_medical_medicament_us.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/medical_medicament_gcn.xml',
        'demo/medical_medicament.xml',
    ],
}
