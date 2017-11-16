# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Administration Practitioner',
    'version': '11.0.1.0.0',
    'author': 'Eficent, Creu Blanca, LasLabs, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_administration',
    ],
    'data': [
        'data/ir_sequence_data.xml',
        'data/medical_role.xml',
        'views/medical_role.xml',
        'views/medical_administration_practitioner.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/medical_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
