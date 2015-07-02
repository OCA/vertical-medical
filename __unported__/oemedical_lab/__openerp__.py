##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    OeMedical, HMS Opensource Solution
##############################################################################
#    Collaborators of this module:
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#    Coded by: Parthiv Patel <parthiv@techreceptives.com>
#    Coded by: Ruchir Shukla <ruchir@techreceptives.com>
#    Planifyied by: Parthiv Patel <parthiv@techreceptives.com>
#    Planifyied by: Nhomar Hernandéz <nhomar@vauxoo.com>
#
##############################################################################
#    This project is mantained by OeMEdical Team:
#    https://launchpad.net/oemedical
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

    'name': 'OeMedical : Free Health and Hospital Information System',
    'version': '1.0',
    'author': "OeMEdical Team,Odoo Community Association (OCA)",
    'category': 'Generic Modules/Others',
    'depends': ['oemedical_emr'],
    'application': True,
    'description': """

About OeMedical
---------------

OeMedical is a multi-user, highly scalable, centralized Electronic
Medical Record (EMR) and Hospital Information System for openERP.

OeMedical provides a free universal Health and Hospital Information System,
so doctors and institutions all over the world,
specially in developing countries will benefit from a centralized,
high quality, secure and scalable system.

OeMedical at a glance:

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
    "website": "http://launchpad.net/oemedical",
    "licence": "AGPL v3",
    "data": [
        #'views/oemedical_lab_view.xml',  # view has errors, please correct before enabling....
        #'views/oemedical_lab_report.xml',  # not checked yet....
        'security/oemedical_security.xml',
        'security/ir.model.access.csv',
        'oemedical_menu.xml',
    ],
    "demo": [

    ],
    'test': [
        'test/physician.yml',
        'test/patient.yml',
        'test/partners.yml',
        'test/insurance_plan.yml',
        'test/insurance.yml',
        'test/physician_speciality.yml'
    ],
    'css': [

    ],
    'js': [

    ],
    'qweb': [

    ],
    "active": False,
    "installable": False,
}