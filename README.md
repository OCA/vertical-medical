[![Runbot Status](https://runbot.odoo-community.org/runbot/badge/flat/159/10.0.svg)](https://runbot.odoo-community.org/runbot/repo/github-com-oca-vertical-medical-159)
[![Build Status](https://travis-ci.org/OCA/vertical-medical.svg?branch=10.0)](https://travis-ci.org/OCA/vertical-medical)
[![codecov](https://codecov.io/gh/OCA/vertical-medical/branch/10.0/graph/badge.svg)](https://codecov.io/gh/OCA/vertical-medical)

# Vertical Medical

Vertical Medical provides a Free and Open Source solution for storing and processing medical
records in Odoo.

Many of the workflows were built in alignment with existing Odoo processes to allow for
seamless operation with other record types.

# Licensing history
The current project as it is today represents an evolution of the original work
started by Luis Falcon. See https://sourceforge.net/projects/medical/files/Oldfiles/1.0.1,
that later became GNU Health (see
http://health.gnu.org/). The original code was licensed under GPL.

On Nov 27, 2012 derivative code was published in https://github.com/OCA/vertical-medical,
by Tech-Receptives Solutions Pvt. Ltd., licensed
under AGPL.  The license change was unauthorized by the original
author. See https://github.com/OCA/vertical-medical/commit/f0a664749edaea36f6749c34bfb04f1fc4cc9ea4

On Feb 17, 2017 the branch 9.0 of the project was relicensed to LGPL.
https://github.com/OCA/vertical-medical/pull/166. Various prior contributors
approved the relicense, but not all.

On Jan 25, 2018, GNU Health claimed that the original code and attribution
should be respected, and after further investigation the Odoo Community
Association Board agreed to switch the license back to GPL v3 to respect the
rights of the original author.

Although no trace of relationship was found between the code at the date
and the original code from 2012, through the commit history of the project one
can see that the current status of the project is the end result of an
evolutionary process. The Odoo Community Association Board concluded that
the original license should be respected for ethical reasons.

More information can be read here - https://odoo-community.org/blog/our-blog-1/post/vertical-medical-75.



[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[medical](medical/) | 10.0.1.1.0 |  | Odoo Medical
[medical_agpl](medical_agpl/) | 10.0.1.0.0 |  | Odoo Medical - GPL
[medical_base_us](medical_base_us/) | 10.0.1.0.0 |  | Provides some helper mixins for US locale
[medical_center](medical_center/) | 10.0.1.0.0 |  | Adds a concept of Medical Centers to Patients.
[medical_insurance](medical_insurance/) | 10.0.1.0.0 |  | Medical Insurance
[medical_pathology](medical_pathology/) | 10.0.1.0.0 |  | Extends Odoo Medical with pathologies (diseases).
[medical_pathology_icd10](medical_pathology_icd10/) | 10.0.1.0.0 |  | Supports the import of ICD-10-CM pathology data
[medical_pathology_import](medical_pathology_import/) | 10.0.1.0.0 |  | Provides an interface for medical pathology data imports
[medical_practitioner](medical_practitioner/) | 10.0.1.2.0 |  | Defines medical practioners
[medical_practitioner_us](medical_practitioner_us/) | 10.0.1.0.0 |  | Adds several US IDs to medical practitioners
[medical_procedure](medical_procedure/) | 10.0.1.0.0 |  | Adds notion of medical procedure used elsewhere in medical


Unported addons
---------------
addon | version | maintainers | summary
--- | --- | --- | ---
[medical_disease](medical_disease/) | 8.0.1.1.0 (unported) |  | Introduce disease notion into the medical category
[medical_insurance_us](medical_insurance_us/) | 8.0.1.1.0 (unported) |  | Medical Insurance - US
[medical_medicament](medical_medicament/) | 8.0.1.0.0 (unported) |  | Introduce Medicament notion into the medical product
[medical_medicament_attributes](medical_medicament_attributes/) | 8.0.1.0.0 (unported) |  | Medical Medicament Physical Attributes
[medical_medication](medical_medication/) | 8.0.1.0.0 (unported) |  | Introduce medication notion into the medical addons
[medical_medication_us](medical_medication_us/) | 8.0.1.0.0 (unported) |  | Medical Medication - US Locale
[medical_pharmacy](medical_pharmacy/) | 8.0.1.1.0 (unported) |  | Medical Pharmacy
[medical_pharmacy_us](medical_pharmacy_us/) | 8.0.1.1.0 (unported) |  | Medical Pharmacy - US Locale
[medical_prescription](medical_prescription/) | 8.0.1.1.0 (unported) |  | This module introduce the prescription/prescription line into the medical addons.
[medical_prescription_sale](medical_prescription_sale/) | 8.0.1.0.0 (unported) |  | Medical Prescription Sales Processes
[medical_prescription_state](medical_prescription_state/) | 8.0.1.1.0 (unported) |  | Medical Prescription Order States
[medical_prescription_thread](medical_prescription_thread/) | 8.0.1.0.0 (unported) |  | Medical Prescription Threaded

[//]: # (end addons)

Translation Status
------------------
[![Transifex Status](https://www.transifex.com/projects/p/OCA-vertical-medical-10.0/chart/image_png)](https://www.transifex.com/projects/p/OCA-vertical-medical-10.0)

----

OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.
