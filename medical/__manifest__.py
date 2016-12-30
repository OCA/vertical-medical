# -*- coding: utf-8 -*-
# Copyright 2004-2009 Tiny SPRL
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Odoo Medical',
    'version': '10.0.1.0.0',
    'category': 'Medical',
    'depends': [
        'product',
        'partner_contact_birthdate',
        'partner_firstname',
        'partner_identification',
        'partner_contact_gender',
    ],
    'author': 'LasLabs, Odoo Community Association (OCA)',
    'website': 'https://odoo-community.org/',
    'license': 'AGPL-3',
    'data': [
        'templates/assets.xml',
        'views/medical_abstract_entity.xml',
        'views/medical_patient.xml',
        'views/res_partner.xml',
        'views/medical_menu.xml',
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
    ],
    'demo': [
        'demo/medical_patient_demo.xml',
    ],
    'installable': True,
    'application': True,
}
