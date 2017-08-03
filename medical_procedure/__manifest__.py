# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Procedure',
    'summary': 'Add Procedure and Procedure Request concept',
    'version': '10.0.1.0.0',
    'author': 'Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'mail',
        'medical',
        'medical_request_group',
        'medical_practitioner',
        'medical_center',
        'workflow_plandefinition',
    ],
    'data': [
        'wizard/medical_procedure_request_make_procedure_view.xml',
        'views/medical_procedure_view.xml',
        'views/medical_procedure_request_view.xml',
        'views/medical_request_group_view.xml',
        'views/medical_menu.xml',
        'data/medical_procedure_sequence.xml',
        'data/medical_procedure_request_sequence.xml'
    ],
    'website': 'https://github.com/OCA/vertical-medical',
    'licence': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
