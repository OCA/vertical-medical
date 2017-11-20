# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Administration Encounter',
    'summary': 'Add Encounter concept',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_administration',
        'medical_administration_location',
    ],
    'data': [
        'views/medical_encounter_view.xml',
        'views/medical_menu.xml',
        'security/ir.model.access.csv',
        'data/medical_encounter_sequence.xml',
    ],
    'installable': True,
    'auto_install': False,
}
