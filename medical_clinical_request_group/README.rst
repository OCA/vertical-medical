.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

=====================
Medical Request Group
=====================

The Request Group resource is used to represent a group of optional activities
that may be performed for a specific patient or context. This resource is
often, but not always, the result of applying a specific PlanDefinition to a
particular patient.

Request Groups can contain hierarchical groups of actions, where each
specific action references the action to be performed (in terms of a Request
resource), and each group describes additional behavior, relationships, and
applicable conditions between the actions in the overall group.

For more information about the FHIR Request Group visit: https://www.hl7.org/fhir/requestgroup.html

Installation
============

To install this module, go to 'Medical / Configuration / Settings' and inside
'Clinical' activate 'Request groups'.

Usage
=====

#. Go to 'Medical / Clinical / Requests / Request groups'
#. Click 'Create'.
#. Fill in the information.
#. Click 'Save'.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/11.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/{project_repo}/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Clker-Free-Vector-Images: `Medical Icon <https://pixabay.com/es/de-salud-medicina-serpiente-alas-304919/>`_
* Odoo Community Association: `Odoo Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Enric Tobella <etobella@creublanca.es>
* Roser Garcia <roser.garcia@eficent.com>
* Jordi Ballester <jordi.ballester@eficent.com>

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
