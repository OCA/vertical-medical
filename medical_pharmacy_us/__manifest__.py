# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Pharmacy - US Locale',
    "website": "https://laslabs.com",
    "licence": "AGPL-3",
    'installable': True,
    'auto_install': False,
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_base_us',
        'medical_pharmacy',
    ],
    'data': [
        'views/medical_pharmacy_view.xml',
        'data/res_partner_id_category.xml',
    ]
}
