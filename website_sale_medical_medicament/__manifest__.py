# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Website - Medicament Sales',
    'version': '10.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_prescription_sale_stock',
        'website_sale',
        'sale_medical_medicament',
    ],
    "website": "https://laslabs.com",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
    ],
}
