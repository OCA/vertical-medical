[![Runbot Status](https://runbot.odoo-community.org/runbot/badge/flat/159/9.0.svg)](https://runbot.odoo-community.org/runbot/repo/github-com-oca-vertical-medical-159)
[![Build Status](https://travis-ci.org/OCA/vertical-medical.svg?branch=9.0)](https://travis-ci.org/OCA/vertical-medical)
[![codecov](https://codecov.io/gh/OCA/vertical-medical/branch/9.0/graph/badge.svg)](https://codecov.io/gh/OCA/vertical-medical)

# Vertical Medical

Vertical Medical provides a Free and Open Source solution for storing and processing medical
records in Odoo.

Many of the workflows were built in alignment with existing Odoo processes to allow for
seamless operation with other record types.

# Licensing history
The current project as it is today represents an evolution of the original work
from from started from Luis Falcon. See https://sourceforge
.net/projects/medical/files/Oldfiles/1.0.1, that later became GNU Health (see
http://health.gnu.org/). The original code was licensed under GPL.

On Nov 27, 2012 derivative code was published in https://github
.com/OCA/vertical-medical, by Tech-Receptives Solutions Pvt. Ltd., licensed
under AGPL.  The license change was unauthorized by the original
author. See https://github.com/OCA/vertical-medical/commit
/f0a664749edaea36f6749c34bfb04f1fc4cc9ea4

On Feb 17, 2017 the branch 9.0 of the project was relicensed to GPL.
https://github.com/OCA/vertical-medical/pull/166. Various prior contributors
approved the relicense, but not all.

On Jan 25, 2017, GNU Health claimed that the original code and attribution
should be respected, and after further investigation the Odoo Community
Association Board agreed to switch the license back to GPL v3 to respect the
rights of the original author.

Although no trace of relationship was found between the code at the date
and the original code from 2012, through the commit history of the project one
can see that the current status of the project is the end result of an
evolutionary process. The Odoo Community Association Board concluded that
the original license should be respected for ethical reasons.

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[mail_thread_medical_prescription](mail_thread_medical_prescription/) | 9.0.1.0.0 | Adds message threads to rx orders and rx order lines.
[medical](medical/) | 9.0.1.0.0 | Extends Odoo with medical patients and centers.
[medical_base_us](medical_base_us/) | 9.0.1.0.0 | Provides some helper mixins for US locale.
[medical_lab](medical_lab/) | 9.0.1.0.0 | Medical Lab
[medical_manufacturer](medical_manufacturer/) | 9.0.1.0.0 | Extension of medical with concept of medical manufacturers.
[medical_medicament](medical_medicament/) | 9.0.1.0.0 | Introduce Medicament notion into the medical product.
[medical_medicament_component](medical_medicament_component/) | 9.0.1.0.0 | Medical Medicament Components
[medical_medicament_us](medical_medicament_us/) | 9.0.1.0.0 | Extension of medical_medicament that provides US locale.
[medical_medication](medical_medication/) | 9.0.1.0.1 | Introduce medication notion into the medical addons.
[medical_pathology](medical_pathology/) | 9.0.1.0.1 | Extends Odoo Medical with pathologies (diseases).
[medical_patient_disease](medical_patient_disease/) | 9.0.1.0.0 | Extend medical patients with the concept of diseases.
[medical_patient_disease_allergy](medical_patient_disease_allergy/) | 9.0.1.0.0 | Isolates allergies from diseases.
[medical_patient_dob](medical_patient_dob/) | 9.0.1.0.0 | Show date of birth when searching patients.
[medical_pharmacy](medical_pharmacy/) | 9.0.1.0.0 | Adds pharmacy namespace on partners.
[medical_pharmacy_us](medical_pharmacy_us/) | 9.0.1.0.0 | Medical Pharmacy - US Locale
[medical_physician](medical_physician/) | 9.0.1.0.0 | Adds physicians to Odoo Medical.
[medical_prescription](medical_prescription/) | 9.0.2.0.0 | Introduces prescription orders and prescription order lines.
[medical_prescription_state](medical_prescription_state/) | 9.0.1.0.0 | Medical Prescription Order States
[medical_prescription_us](medical_prescription_us/) | 9.0.1.0.0 | Extension of medical_prescription that provides US Locale
[sale_crm_medical_prescription](sale_crm_medical_prescription/) | 9.0.1.0.0 | Create opportunities from prescriptions.
[sale_medical_prescription](sale_medical_prescription/) | 9.0.2.0.0 | Create sale orders from prescriptions.
[sale_stock_medical_prescription](sale_stock_medical_prescription/) | 9.0.1.0.0 | Provides dispense logic for prescriptions.


Unported addons
---------------
addon | version | summary
--- | --- | ---
[medical_insurance](medical_insurance/) | 8.0.1.1.0 (unported) | Medical Insurance
[medical_insurance_us](medical_insurance_us/) | 8.0.1.1.0 (unported) | Medical Insurance - US
[medical_medicament_attributes](medical_medicament_attributes/) | 8.0.1.0.0 (unported) | Medical Medicament Physical Attributes

[//]: # (end addons)

Translation Status
------------------
[![Transifex Status](https://www.transifex.com/projects/p/OCA-vertical-medical-9.0/chart/image_png)](https://www.transifex.com/projects/p/OCA-vertical-medical-9.0)

----

OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.
