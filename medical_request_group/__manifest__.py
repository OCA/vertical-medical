# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Request Group',
    'summary': 'Request Group',
    'version': '10.0.1.0.0',
    'author': 'Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'mail',
        'medical',
        'workflow_plandefinition',
        'medical_center',
    ],
    'data': [
        'security/request_group_security.xml',
        'security/ir.model.access.csv',
        'views/medical_request_group_view.xml',
        'views/medical_menu.xml',
    ],
    'website': 'https://github.com/OCA/vertical-medical',
    'licence': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
