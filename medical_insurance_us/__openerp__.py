# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Insurance - US',
    'version': '9.0.1.0.0',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'medical_insurance'
    ],
    'website': 'https://laslabs.com',
    'license': 'AGPL-3',
    'data': [
        'views/medical_insurance_plan_view.xml',
        'views/medical_insurance_template_view.xml',
    ],
    'test': [
        'tests/medical_insurance_company.yml',
        'tests/medical_insurance_template.yml',
        'tests/medical_insurance_plan.yml',
    ],
    'installable': True,
    'auto_install': False,
}
