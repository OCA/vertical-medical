# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Medical Practitioner',
    'version': '1',
    'summary': 'Defines practioners',
    'author': "Creu Blanca",
    'maintainer': 'Creu Blanca',
    'sequence': 30,
    'category': 'Project',
    'website': 'http://www.creublanca.es',
    'depends': ['medical'],
    'data': [
        'data/medical_role.xml',
        'views/medical_role.xml',
        'wizard/medical_practitioner_user.xml',
        'views/medical_practitioner.xml',
        'views/medical_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
