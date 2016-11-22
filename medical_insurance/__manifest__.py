# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Insurance',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical'
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "data": [
        'views/medical_insurance_company_view.xml',
        'views/medical_insurance_template_view.xml',
        'views/medical_insurance_plan_view.xml',
        'views/medical_patient_view.xml',
        'security/ir.model.access.csv',
        'views/medical_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
}
