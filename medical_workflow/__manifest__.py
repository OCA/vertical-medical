# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Workflow',
    'summary': 'Medical workflow base',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_administration_practitioner',
        'product'
    ],
    'data': [
        'data/medical_workflow.xml',
        'data/ir_sequence.xml',
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'wizard/medical_add_plan_definition_views.xml',
        'views/medical_menu.xml',
        'views/workflow_activity_definition.xml',
        'views/workflow_plan_definition.xml',
        'views/workflow_plan_definition_action.xml',
        'views/workflow_type.xml',
        'views/res_config_settings_views.xml',
        'views/medical_patient.xml',
        'views/medical_request_view.xml',
        'views/medical_event_view.xml',
    ],
    'demo': [
        'demo/medical_demo.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
