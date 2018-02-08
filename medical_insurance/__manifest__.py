# -*- coding: utf-8 -*-
# Copyright 2015 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{

    'name': 'Medical Insurance',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical'
    ],
    "website": "https://laslabs.com",
    "license": "GPL-3",
    "data": [
        'views/medical_insurance_company_view.xml',
        'views/medical_insurance_template_view.xml',
        'views/medical_insurance_plan_view.xml',
        'views/medical_patient_view.xml',
        'security/ir.model.access.csv',
        'views/medical_menu.xml',
    ],
    "demo": [
        "demo/product_product_demo.xml",
        "demo/medical_insurance_company_demo.xml",
        "demo/medical_insurance_template_demo.xml",
        "demo/medical_insurance_plan_demo.xml",
    ],
    'installable': True,
    'auto_install': False,
}
