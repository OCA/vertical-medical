# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Location with stock',
    'summary': 'Medical administration location with stock',
    'version': '11.0.1.0.0',
    "category": "Medical",
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_administration_location',
        'stock',
    ],
    'data': [
        'security/medical_security.xml',
        'views/res_partner_views.xml',
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
