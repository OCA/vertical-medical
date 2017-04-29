# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{

    'name': 'Medical Prescription Sale Stock - US',
    'summary': 'Provides US Locale to Medical Prescription Sale Stock',
    'version': '9.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_base_us',
        'medical_prescription_sale_stock',
        'medical_prescription_us',
    ],
    'data': [
        'views/procurement_order_view.xml',
        'views/res_company_view.xml',
    ],
    "website": "https://laslabs.com",
    "license": "LGPL-3",
    'installable': True,
    'auto_install': False,
}
