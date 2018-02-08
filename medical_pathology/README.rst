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
