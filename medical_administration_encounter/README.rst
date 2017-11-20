.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Medical Encounter
=================

Represents an interaction between a patient and healthcare provider(s) for
the purpose of providing healthcare service(s) or assessing the health
status of a patient.

A patient encounter is further characterized by the setting in which it
takes place. Amongst them are ambulatory, emergency, home health, inpatient
and virtual encounters. An Encounter encompasses the lifecycle from
pre-admission, the actual encounter (for ambulatory encounters), and
admission, stay and discharge (for inpatient encounters). During the
encounter the patient may move from practitioner to practitioner and
location to location.

Installation
============

To install this module, simply follow the standard install process.

Usage
=====

#. Go to Medical -> Encounter -> Encounters
#. Click "Create"
#. Enter the encounter information and click "Save"

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/11.0

Known Issues / Roadmap
======================

* Improve and provide a full description for this module into the README.rst
* The fields 'Insurance' and 'Medical center' from Encounter are still missing but
  since they depend on other entities that haven't been implemented they aren't available yet.

Bug Tracker
===========

Bugs are tracked on 
`GitHub Issues <https://github.com/OCA/vertical-medical/issues>`_. In case of 
trouble, please check there if your issue has already been reported. If you 
spotted it first, help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association:
  `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Jordi Ballester <jordi.ballester@eficent.com>
* Roser Garcia <roser.garcia@eficent.com>
* Gisela Mora <gisela.mora@eficent.com>
* Enric Tobella <etobella@creublanca.es>


Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
