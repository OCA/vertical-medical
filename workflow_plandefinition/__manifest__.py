# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Plan Definition',
    'summary': 'Add Plan definition concept',
    'version': '10.0.1.0.0',
    'author': 'Eficent, Odoo Community Association (OCA)',
    'depends': [
        'mail',
        'medical',
        'stock',
    ],
    'data': [
        'views/workflow_plan_definition_action.xml',
        'security/workflow_security.xml',
        'security/ir.model.access.csv',
        'views/workflow_type.xml',
        'views/workflow_plan_definition.xml',
        'views/workflow_activity_definition.xml',
        'views/workflow_menu.xml',
    ],
    'website': 'https://github.com/OCA/vertical-medical',
    'licence': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
