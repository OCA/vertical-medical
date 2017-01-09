# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Physician - US Locale',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    "website": "https://laslabs.com",
    "licence": "AGPL-3",
    'category': 'Medical',
    'depends': [
        'medical_base_us',
        'medical_physician',
    ],
    "data": [
        'views/medical_physician_view.xml',
        'data/res_partner_id_category.xml',
    ],
    "application": False,
    'installable': True,
}
