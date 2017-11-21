.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl.html
   :alt: License: LGPL-3

====================================
Medical Pathology - ICD-10-CM Import
====================================

This module provides support for the import of ICD-10-CM pathology data. If it
is installed with demo data enabled, the import will happen automatically
during the install process. Otherwise, it will need to be triggered manually.

Usage
=====

If necessary, you can manually trigger the import as follows:

1. Go to ``Medical > Configuration > Pathology > Import Data`` to access the
   import wizard
2. Select the ``ICD-10-CM`` importer type
3. Click ``Save``

This is a large dataset and can easily take a few minutes to import. If your
Odoo instance times out during this process, you may need to increase the
``limit_time_cpu`` and ``limit_time_real`` values in your config file.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/10.0

Known Issues / Roadmap
======================

* Add translation support for imported data
  (https://github.com/OCA/vertical-medical/issues/136)
* Add support for importing additional ICD-10-CM sections that do not map
  directly to the main pathology hierarchy

Bug Tracker
===========

Bugs are tracked on 
`GitHub Issues <https://github.com/OCA/vertical-medical/issues>`_. In case of
trouble, please check there if your issue has already been reported. If you
spotted it first, help us smash it by providing detailed and welcome feedback.

Credits
=======

Images
------

* Odoo Community Association:
  `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Dave Lasley <dave@laslabs.com>
* Oleg Bulkin <obulkin@laslabs.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
