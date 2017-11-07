# Copyright 2004-2009 Tiny SPRL
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Odoo Medical',
    'version': '11.0.1.0.0',
    'category': 'Medical',
    'depends': [
        'product',
    ],
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'website': 'https://odoo-community.org/',
    'license': 'LGPL-3',
    'data': [
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'templates/assets.xml',
        'views/medical_abstract_entity.xml',
        'views/medical_patient.xml',
        'views/res_partner.xml',
        'views/medical_menu.xml',
    ],
    'demo': [
        'demo/medical_patient_demo.xml',
    ],
    'installable': True,
    'application': True,
}
