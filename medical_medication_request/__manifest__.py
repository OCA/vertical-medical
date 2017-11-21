# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Medication Request',
    'summary': 'Medical medication request and administration',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'category': 'Medical',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_workflow',
        'medical_medication',
        'medical_administration_location_stock',
    ],
    'data': [
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/stock_location.xml',
        'views/medical_request_views.xml',
        'views/medical_medication_administration_view.xml',
        'views/medical_medication_request.xml',
    ],
    'demo': [
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
