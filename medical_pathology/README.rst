.. image:: https://img.shields.io/badge/license-GPL--3-blue.svg
    :target: http://www.gnu.org/licenses/gpl-3.0-standalone.html
    :alt: License: GPL-3

======================
Odoo Medical Pathology
======================

This module extends Odoo Medical with functionality for pathologies (diseases).

Definitions
===========

* ``Pathology`` - The branch of medicine concerned with the study of the nature of
  disease and its causes, processes, development, and consequences.

Configuration
=============

The ``Disease`` configuration menu is in the ``Configuration`` section of the
``Medical`` app.

* ``Pathologies`` - Use ths menu to add or view diseases in the system.
* ``Pathology Categories`` - Provides a hierarchal category structure for pathologies.
  These categories are typically standardized, such as ICD-10.
* ``Pathology Groups`` - Allows for internal pathology classification while providing
  isolation from the standardized categories.

.. image:: static/description/screenshot_pathologies.png?raw=true
   :alt: Pathologies

.. image:: static/description/screenshot_pathology_categories.png?raw=true
   :alt: Pathology Categories

Usage
=====

This module does not provide functionality beyond data models as listed above.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/9.0

Known issues / Roadmap
======================

Upgrade Note: This module replaces pathology logic from v8 ``medical_disease``. The
remaining logic related to the application of pathologies to the context of a patient
(aka ``pathosis``) is in ``medical_patient_disease``.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/vertical-medical/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* James Foster <jfoster@laslabs.com>
* Brett Wood <bwood@laslabs.com>
* Dave Lasley <dave@laslabs.com>

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
