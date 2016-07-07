# -*- coding: utf-8 -*-
# © 2004 Tiny SPRL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Odoo Medical',
    'version': '9.0.1.0.0',
    'category': 'Medical',
    'depends': [
        'base',
        'product',
    ],
    'author': 'LasLabs, Odoo Medical Team, Odoo Community Association (OCA)',
    'website': 'http://github.com/oca/vertical-medical',
    'license': 'AGPL-3',
    'data': [
        'data/ir_sequence_data.xml',
        'views/res_partner_view.xml',
        'views/medical_patient_view.xml',
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/medical_menu.xml',
    ],
    'test': [
        'tests/patient.yml',
        'tests/partners.yml',
    ],
    'demo': [
        'demo/medical_patient_demo.xml',
    ],
    'installable': True,
    'application': True,
}
