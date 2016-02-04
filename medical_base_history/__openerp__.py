# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Base - History',
    'summary': 'Add concept of abstract history object for change auditing',
    'version': '9.0.1.0.0',
    'author': 'LasLabs, Odoo Medical Team, Odoo Community Association (OCA)',
    'category': 'Medical',
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
    'test': [
        'tests/medical_history.yml',
    ],
    'website': 'https://laslabs.com',
    'licence': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
