# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Terminology',
    'summary': 'Medical terminology base',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_base'
    ],
    'data': [
        'views/medical_menu.xml',
        'views/medical_abstract_concept_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
