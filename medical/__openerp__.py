# -*- coding: utf-8 -*-
# © 2015 LasLabs Inc.
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
        'wizard/medical_physician_unavailable_view.xml',
        'views/medical_physician_view.xml',
        'views/medical_patient_view.xml',
        'views/medical_specialty_view.xml',
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'views/medical_menu.xml',
    ],
    'test': [
        'tests/physician.yml',
        'tests/patient.yml',
        'tests/partners.yml',
        'tests/physician_speciality.yml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
