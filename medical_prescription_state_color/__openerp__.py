# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription Order State Color',
    'version': '9.0.1.0.0',
    'author': "LasLabs, Odoo Medical Team, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_prescription_state',
    ],
    'website': 'http://github.com/oca/vertical-medical',
    'license': 'AGPL-3',
    'data': [
        'views/medical_prescription_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
