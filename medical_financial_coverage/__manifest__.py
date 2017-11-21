# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Financial Coverage',
    'summary': 'Add Coverage concept',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_financial',
    ],
    'data': [
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'data/medical_payor_sequence.xml',
        'data/medical_coverage_sequence.xml',
        'views/medical_patient_views.xml',
        'views/res_partner_views.xml',
        'views/medical_coverage_template_view.xml',
        'views/medical_coverage_view.xml',
        'views/medical_menu.xml',
    ],
    "demo": [
        "demo/medical_coverage.xml",
    ],
    'installable': True,
    'auto_install': False,
}
