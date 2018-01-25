# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

{
    'name': 'Odoo Medical',
    'version': '10.0.1.1.0',
    'category': 'Medical',
    'depends': [
        'product',
        'base_locale_uom_default',
    ],
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'website': 'https://odoo-community.org/',
    'license': 'GPL-3',
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
