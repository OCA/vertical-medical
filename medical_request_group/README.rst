.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============
Request Group
=============

The Request Group resource is used to represent a group of optional
activities that may be performed for a specific patient or context. This
resource is often, but not always, the result of applying a specific
Plan Definition to a particular patient.

Request Groups can contain hierarchical groups of actions, where each specific
action references the action to be performed (in terms of a Request resource),
and each group describes additional behavior, relationships, and applicable
conditions between the actions in the overall group.


Installation
============

To install this module, simply follow the standard install process.


Usage
=====

#. Go to Medical -> Request Group -> Request Groups
#. Click "Create"
#. Enter the information and click "Save"

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/10.0


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
