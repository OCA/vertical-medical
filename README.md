[![Build Status](https://travis-ci.org/OCA/vertical-medical.svg?branch=8.0)](https://travis-ci.org/OCA/vertical-medical)
[![Coverage Status](https://coveralls.io/repos/OCA/vertical-medical/badge.png?branch=8.0)](https://coveralls.io/r/OCA/vertical-medical?branch=8.0)

*Important note*: in order to facilitate the review process, work to migrate to 8.0 is currently done on the 8.0-incubator branch because it implies several PR's depending on each others and is currently in unstable state. As soon as this stabilizes, it will be merged back in the 8.0 branch and the normal OCA process will resume.

What is Odoo Medical
---

**Odoo Medical** is a multi-user, highly scalable, centralized Electronic Medical
Record (EMR) and Hospital Information System for odoo.

**Odoo Medical** provides a free universal Health and Hospital Information System,
so doctors and institutions all over the world, specially in developing
countries will benefit from a centralized, high quality, secure and scalable
system.

Odoo Medical at a glance:
---

- Strong focus in family medicine and Primary Health Care

- Major interest in Socio-economics (housing conditions, substance abuse,
education...)

- Diseases and Medical procedures standards (like ICD-10 / ICD-10-PCS ...)

- Patient Genetic and Hereditary risks : Over 4200 genes related to
diseases (NCBI / Genecards)

- Epidemiological and other statistical reports

- 100% paperless patient examination and history taking

- Patient Administration
(creation, evaluations / consultations, history ... )

- Doctor Administration

- Lab Administration

- Medicine / Drugs information (vademécum)

- Medical stock and supply chain management

- Hospital Financial Administration

- Designed with industry standards in mind

- Open Source : Licensed under AGPL


Contributing
---

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
---

*Report Bugs*

Report bugs at https://github.com/oca/vertical-medical/issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

*Fix Bugs*

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

*Implement Features*

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

*Write Documentation*

Try to comment your code using PEP guidelines, and don’t repeat yourself.
TODO: Link the oca standars here.

*Submit Feedback*

The best way to send feedback is to file an issue at https://github.com/oca/vertical-medical/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Hacking Odoo Medical
---

1. Clone this repository:

    ```bash
    $ git clone git@github.com:oca/vertical-medical.git
    $ cd medical && checkout 8.0
    ```

2. Create your own branch locally.

    ```bash
    $ git checkout -b 8.0-your_new_feature_theme
    ```

3. Push your first change branch to know you start to work on.

    ```bash
    $ git push -u origin 8.0-your_new_feature_theme
    ```

4. Prepare your enviroment to work with this repository and the mandatory ones to have all the enviroment ready.

    ```bash
    $ git clone https://github.com/odoo/odoo.git
    $ git clone https://github.com/oca/vertical-medical.git
    $ cd odoo && checkout 8.0
    $ cd vertical-medical && checkout 8.0
    ```

5. Create a postgres user (only for this work to avoid problems not related to this enviroment).

    ```bash
    $ sudo su postgres
    $ createuser medicaluser -P
    #put your password just (1) for example.
    $ createdb medical -U medicaluser -O medicaluser -T remplate0 -E UTF8
    ```

6. Run the development enviroment.

    ```bash
    $ cd path/to/odoo/odoo
    $ ./openerp-server --addons-path=addons/,../medical -r \
    medicaluser -w 1 --db-filter=medical \
    -i medical -d medical
    ```

7. Do your code, and update it passing -u module -d medical (replacing this paramenter above).

8. Before be sure all is ok, we can delete and create db again with -i
   paramenter to ensure all install correctly.

    ```bash
    $ sudo su postgres
    $ dropbd medical
    $ createdb medical -U medicaluser -O medicaluser -T remplate0 -E UTF8
    $ ./openerp-server --addons-path=addons/,../medical -r \
    medicaluser -w 1 --db-filter=medical \
    -i medical -d medical
    ```

9. If all is ok installing, please test your enviroment running your code with ‘test-enabled’.

    ```bash
    $ ./openerp-server --addons-path=addons/,../medical -r \
    medicaluser -w 1 --db-filter=medical \
    -i medical -d medical --test-enable
    ```

**Note:**

    This will take a time, just do it before commit your change and make push.

10. Add your changes to have them versioned.

    ```bash
    $ git add .
    ```

11. Commit your changes.

    ```bash
    $ git commit -m "[TAG] module: what you did"
    ```

12. Push your first change branch to know you start to work on.

    ```bash
    $ git push -u origin 8.0-your_new_feature_theme
    ```


[//]: # (addons)
Available addons
----------------
addon | version | summary
--- | --- | ---
[medical](medical/) | 8.0.1.0.0 | Odoo Medical

Unported addons
---------------
addon | version | summary
--- | --- | ---
[oemedical_emr](__unported__/oemedical_emr/) | 1.0 (unported) | OeMedical EMR : Electronic Medical Record management for OeMedical
[oemedical_emr_data](__unported__/oemedical_emr_data/) | 1.0 (unported) | OeMedical EMR: Module Data
[oemedical_genetics](__unported__/oemedical_genetics/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_gynecology_and_obstetrics](__unported__/oemedical_gynecology_and_obstetrics/) | 1.0.1 (unported) | OeMedical : gynecology and obstetrics
[oemedical_his](__unported__/oemedical_his/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_icu](__unported__/oemedical_icu/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_insurance](__unported__/oemedical_insurance/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_invoice](__unported__/oemedical_invoice/) | 0.1 (unported) | Medical Invoice
[oemedical_lab](__unported__/oemedical_lab/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_lifestyle](__unported__/oemedical_lifestyle/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_pediatrics](__unported__/oemedical_pediatrics/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_socioeconomics](__unported__/oemedical_socioeconomics/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[oemedical_surgery](__unported__/oemedical_surgery/) | 1.0 (unported) | OeMedical : Free Health and Hospital Information System
[web_doc_oemedical](__unported__/web_doc_oemedical/) | 0.1 (unported) | OeMedical CMS

[//]: # (end addons)
