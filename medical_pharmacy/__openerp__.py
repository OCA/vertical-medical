# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Pharmacy',
    'version': '9.0.1.1.0',
    'author': "LasLabs, Odoo Medical Team, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical',
    ],
    'website': 'https://laslabs.com',
    'license': 'AGPL-3',
    'data': [
        'views/medical_pharmacy_view.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        'tests/medical_pharmacy.yml',
    ],
    'installable': True,
    'auto_install': False,
}
