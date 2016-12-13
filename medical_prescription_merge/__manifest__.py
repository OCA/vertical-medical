# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Prescription - Order Merge',
    'summary': 'Provides support for merging existing prescription orders',
    'version': '10.0.1.0.0',
    'category': 'Medical',
    'website': 'https://laslabs.com/',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': False,
    'depends': [
        'medical_prescription',
    ],
    'data': [
        'wizards/medical_prescription_order_merge.xml',
    ],
}
