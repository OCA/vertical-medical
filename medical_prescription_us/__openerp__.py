# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription - US Locale',
    'version': '9.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_base_us',
        'medical_prescription',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "data": [
        'views/medical_prescription_order_line_view.xml',
    ],
    "application": False,
    'installable': True,
}
