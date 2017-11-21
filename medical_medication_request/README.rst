.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

==========================
Medical Medication Request
==========================

The resource **Medication Request** represents an order or request for both
supply of the medication and the instructions for administration of the
medication to a patient.

The resource **Medication Administration** describes the event of a patient
consuming or otherwise being administered a medication. This may be as simple
as swallowing a tablet or it may be a long running infusion. Related
resources tie this event to the authorizing prescription, and the specific
encounter between patient and health care practitioner.

For further information about FHIR Medication Request visit: https://www.hl7.org/fhir/medicationrequest.html
For further information about FHIR Medication Administration visit: https://www.hl7.org/fhir/medicationadministration.html

Installation
============

To install this module, go to 'Medical / Configuration / Settings' and inside
'Medication' activate 'Medication administration & Medication requests'.

Usage
=====

#. Go to 'Medical / Medications / Requests'
#. Click 'Create' and fill in all the required information.
#. Click 'Save'.
#. Go to 'Medical / Medications / Administration'
#. Click 'Create'.
#. Provide a patient, a product, a quantity and a medical location which must
   be already related to a stock location.
#. Click 'Save'.
#. Press the button 'Activate'.
#. Press the button 'Complete'.
#. Press the button 'Stock moves' to see the generated move.

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
