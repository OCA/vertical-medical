# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Medicament',
    'version': '9.0.1.0.2',
    "author": "ACSONE SA/NV, LasLabs, Odoo Community Association (OCA)",
    "maintainer": "ACSONE SA/NV, LasLabs, Odoo Community Association (OCA)",
    "website": "http://www.acsone.eu",
    'category': 'Medical',
    'depends': [
        'medical',
        'product',
    ],
    'summary': 'Introduce Medicament notion into the medical product',
    'data': [
        'security/ir.model.access.csv',
        'data/medical_drug_form.xml',
        'data/medical_drug_route.xml',
        'views/product_product_view.xml',
        'views/medical_medicament_view.xml',
        'views/medical_drug_form_view.xml',
        'views/medical_drug_route_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
