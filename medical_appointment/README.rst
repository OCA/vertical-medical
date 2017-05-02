.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================
Odoo Medical Appointment
========================

Extension of medical_physician that provides appointment concepts

Installation
============

To install this module, simply follow the standard install process.

Configuration
=============

No configuration is needed or possible.

Usage
=====

#. Go to Medical -> Appointments -> Appointments
#. Click "Create"
#. Enter appointment information and click "Save"

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/10.0

Known Issues / Roadmap
======================

* Improve and provide a full description for this module into the README.rst
* Due to a bug in the ``auditlog`` module that should be fixed soon, duplicate 
  appointment audit log entries will be produced after this module is first 
  installed. Restarting the server after installing should fix this.

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
