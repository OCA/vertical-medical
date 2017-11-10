# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Plan Definition',
    'summary': 'Adds Plan Definition concept',
    'version': '11.0.1.0.0',
    'author': 'Eficent, Odoo Community Association (OCA)',
    'depends': [
        'mail',
        'medical_request_group',
        'product',
    ],
    'data': [
        'data/medical_workflow.xml',
        'security/workflow_security.xml',
        'security/ir.model.access.csv',
        'views/workflow_plan_definition_action.xml',
        'views/workflow_type.xml',
        'views/workflow_plan_definition.xml',
        'views/workflow_activity_definition.xml',
        'views/workflow_menu.xml',
        'wizard/medical_add_plan_definition_views.xml',
        'views/medical_patient.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'demo/medical_demo.xml'
    ],
    'website': 'https://github.com/OCA/vertical-medical',
    'licence': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
