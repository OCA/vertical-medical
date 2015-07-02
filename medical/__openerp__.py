##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    Odoo Medical, HMS Opensource Solution
##############################################################################
#    Collaborators of this module:
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Coded by: Parthiv Patel <parthiv@techreceptives.com>
#    Coded by: Ruchir Shukla <ruchir@techreceptives.com>
#    Coded by: Mario Arias   <support@cysfuturo.com>
#    Planifyied by: Parthiv Patel <parthiv@techreceptives.com>
#    Planifyied by: Nhomar Hernandéz <nhomar@vauxoo.com>
#
##############################################################################
#    This project is mantained by Odoo Medical Team:
#    http://github.com/oca/vertical-medical
#
##############################################################################
#    It is a collaborative effort between several companies that want to join
#    efforts in have a proposal solid and strong in the Health Care environment
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{

    'name': 'Odoo Medical',
    'version': '1.0',
    'category': 'Medical',
    'depends': [
        'base',
        'product'
    ],
    'author': "Odoo Medical Team,Odoo Community Association (OCA)",
    'category': 'Generic Modules/Others',
    'application': True,
    'description': """

About Odoo Medical
------------------

Odoo Medical is a multi-user, highly scalable, centralized Electronic
Medical Record (EMR) and Hospital Information System for openERP.

Odoo Medical provides a free universal Health and Hospital Information System,
so doctors and institutions all over the world,
specially in developing countries will benefit from a centralized,
high quality, secure and scalable system.

Odoo Medical at a glance:

    * Strong focus in family medicine and Primary Health Care

    * Major interest in Socio-economics (housing conditions, substance abuse,
    education...)

    * Diseases and Medical procedures standards (like ICD-10 / ICD-10-PCS ...)

    * Patient Genetic and Hereditary risks : Over 4200 genes related to
    diseases (NCBI / Genecards)

    * Epidemiological and other statistical reports

    * 100% paperless patient examination and history taking

    * Patient Administration
    (creation, evaluations / consultations, history ... )

    * Doctor Administration

    * Lab Administration

    * Medicine / Drugs information (vademécum)

    * Medical stock and supply chain management

    * Hospital Financial Administration

    * Designed with industry standards in mind

    * Open Source : Licensed under AGPL

""",
    "website": "http://github.com/oca/vertical-medical",
    "licence": "AGPL v3",
    "data": [
        'views/medical_sequence.xml',
        'views/product_product_view.xml',
        'views/res_partner_view.xml',
        'wizard/medical_physician_unavailable_view.xml',
        'views/medical_physician_view.xml',
        'views/medical_patient_view.xml',
        'views/medical_appointment_view.xml',
        'data/medical_appointment_data.xml',
        'views/medical_specialty_view.xml',
        'security/medical_security.xml',
        'security/ir.model.access.csv',
        'views/medical_menu.xml',
    ],
    "demo": [

    ],
    'test': [
        'tests/physician.yml',
        'tests/patient.yml',
        'tests/partners.yml',
        'tests/physician_speciality.yml'
    ],
    'css': [

    ],
    'js': [

    ],
    'qweb': [

    ],
    "active": False
}
