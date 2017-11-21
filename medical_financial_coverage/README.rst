.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

================
Medical Coverage
================

The **Coverage** Resource represents a Financial instrument which may be used
to reimburse or pay for health care products and services.

The Coverage resource is intended to provide the high level identifiers and
potentially descriptors of an insurance plan which may used to pay for, in
part or in whole, the provision of health care products and services.

This resource may also be used to register 'SelfPay' where an individual or
organization other than an insurer is taking responsibility for payment for a
portion of the health care costs.

The **Payor** Resorce represents the identity of the insurer or party paying
for services.

For more information about the FHIR Coverage visit: https://www.hl7.org/fhir/coverage.html
For more information about the FHIR Payor visit: https://www.hl7.org/fhir/coverage-definitions.html#Coverage.payor

Installation
============

To install this module, go to 'Medical / Configuration / Settings' and inside
'Financial' activate 'Covarages'.

Usage
=====

#. Go to 'Medical / Financial / Payors'
#. Click 'Create'.
#. Fill in the information.
#. Click 'Save'.
#. Go to 'Medical / Financial / Coverage Template'
#. Click 'Create'.
#. Provide a name for that template and a payor.
#. Click 'Save'.
#. Go to 'Medical / Financial / Coverage'
#. Click 'Create'.
#. Provide a patient, a subscriber id and a coverage template.
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

* Clker-Free-Vector-Images: `Icon <https://pixabay.com/es/de-salud-medicina-serpiente-alas-304919/>`_
* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

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
