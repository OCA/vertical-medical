.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

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

* ``Pathologies`` - Use this menu to add or view diseases in the system.
* ``Pathology Categories`` - Provides a hierarchical category structure for pathologies.
  These categories are typically standardized, such as ICD-10.

.. image:: static/description/screenshot_pathologies.png?raw=true
   :alt: Pathologies

.. image:: static/description/screenshot_pathology_categories.png?raw=true
   :alt: Pathology Categories

Usage
=====

This module does not provide functionality beyond data models as listed above.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/10.0

Known issues / Roadmap
======================

* The concepts here should be replaced with FHIR `Observation <https://www.hl7.org/fhir/observation.html>`_
  and `Condition <https://www.hl7.org/fhir/condition.html>`_ in v11. `More info
  <http://wiki.hl7.org/index.php?title=Observation,_Condition,_Diagnosis,_Concern>`_.
* A concept of pathology aliases should be introduced, which will allow for pathologies
  of different code types to be referenced back to each other - allowing for code type
  conversions.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/vertical-medical/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

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
