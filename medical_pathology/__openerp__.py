# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Medical Pathology',
    'version': '9.0.1.0.0',
    'author': 'LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)',
    'maintainer': 'LasLabs, ACSONE SA/NV, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'medical',
    ],
    'website': 'https://laslabs.com/',
    'licence': 'AGPL-3',
    'data': [
        'views/medical_pathology_category_view.xml',
        'views/medical_pathology_group_view.xml',
        'views/medical_pathology_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        'tests/medical_pathology_category.yml',
        'tests/medical_pathology_group.yml',
        'tests/medical_pathology.yml',
    ],
    'installable': True,
    'auto_install': False,
}
