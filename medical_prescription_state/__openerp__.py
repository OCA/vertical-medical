# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription Order States',
    'version': '9.0.1.0.0',
    'author': "LasLabs, Odoo Medical Team, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_prescription',
    ],
    'website': 'http://github.com/oca/vertical-medical',
    'license': 'AGPL-3',
    'data': [
        # Views
        'views/medical_prescription_order_state_view.xml',
        'views/medical_prescription_order_view.xml',

        # Menu & Access
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        "tests/medical_prescription_order.yml",
        'tests/medical_prescription_order_state.yml',
    ],
    'installable': True,
    'auto_install': False,
}
