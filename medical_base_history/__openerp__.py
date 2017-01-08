# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Medical Base - History',
    'summary': 'Add concept of abstract history object for change auditing',
    'version': '9.0.1.0.0',
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://laslabs.com',
    'license': 'AGPL-3',
    'depends': [
        'medical',
    ],
    'data': [
        'views/medical_history_entry_view.xml',
        'views/medical_history_type_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
        'data/medical_history_type_data.xml',
    ],
    'installable': True,
}
