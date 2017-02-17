# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Medicament Components',
    'version': '9.0.1.0.0',
    'author': "LasLabs, Odoo Community Association (OCA)",
    'category': 'Medical',
    'depends': [
        'medical_medicament',
    ],
    'website': 'https://laslabs.com',
    'license': 'LGPL-3',
    'data': [
        'views/medical_medicament_component_view.xml',
        'views/medical_medicament_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'tests': [
        'tests/medical_medicament_component.yml',
    ],
    'installable': True,
    'auto_install': False,
}
