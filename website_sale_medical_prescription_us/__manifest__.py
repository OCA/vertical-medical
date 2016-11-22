# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website Sale Medical Prescription US',
    'summary': 'Adds US context to Website Sale Medical Prescription',
    'version': '10.0.1.0.0',
    'category': 'Website',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'website_sale_medical_prescription',
        'medical_medicament_us',
    ],
    'data': [
        'views/medical_prescription_order_template.xml',
    ],
}
