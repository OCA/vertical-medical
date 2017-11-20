# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Medication',
    'summary': 'Medical medication base',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_administration',
        'medical_terminology_sct',
        'medical_terminology_atc',
        'product',
        'stock',
    ],
    'data': [
        'security/medical_security.xml',
        'data/sct_data.xml',
        'views/medical_menu.xml',
        'views/product_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'demo/sct_data.xml',
        'demo/medication.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
