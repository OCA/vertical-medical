# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical SCT Codification',
    'summary': 'Medical codification base',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_terminology'
    ],
    'data': [
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'data/sct_data.xml',
        'views/medical_sct_concept_views.xml',
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
