# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Prescription Threaded',
    'version': '10.0.1.0.0',
    'author': 'LasLabs, Odoo Medical Team, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'medical_prescription',
    ],
    'website': 'https://laslabs.com/',
    'license': 'AGPL-3',
    'data': [
        'views/medical_prescription_order_view.xml',
        'views/medical_prescription_order_line_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
