# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Condition',
    'summary': 'Medical condition',
    'version': '11.0.1.0.0',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'depends': [
        'medical_administration',
        'medical_terminology_sct',
    ],
    'data': [
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/medical_clinical_finding.xml',
        'views/medical_patient_views.xml',
        'views/medical_condition_views.xml',
        'views/medical_clinical_finding_views.xml',
    ],
    'demo': [
        'demo/medical_demo.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
