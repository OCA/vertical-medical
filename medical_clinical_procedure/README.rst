.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

=================
Medical Procedure
=================

A **Procedure Request** is a record of a request for a procedure to be
planned, proposed, or performed with or on a patient.

The **Procedure** represents an action that is or was performed on a patient.
This can be a physical intervention like an operation, or less invasive like
counseling or hypnotherapy.

This resource is used to record the details of procedures performed on a
patient. A procedure is an activity that is performed with or on a patient as
part of the provision of care. Examples include surgical procedures,
diagnostic procedures, endoscopic procedures, biopsies, counseling,
physiotherapy, exercise, etc.

This resource provides summary information about the occurrence of the
procedure and is not intended to provide real-time snapshots of a procedure
as it unfolds, though for long-running procedures such as psychotherapy, it
could represent summary level information about overall progress. The
creation of a resource to support detailed real-time procedure information
awaits the identification of a specific implementation use-case to share such
information.

For more information about the FHIR Procedure Request visit: https://www.hl7.org/fhir/procedurerequest.html
For further information about the FHIR Procedure visit: https://www.hl7.org/fhir/procedure.html

Installation
============

To install this module, go to 'Medical / Configuration / Settings' and inside
'Clinical' activate 'Procedures & Procedure requests'.

Usage
=====

#. Go to 'Medical / Clinical / Requests / Procedure Requests'
#. Click 'Create'.
#. Fill in the information.
#. Click 'Save' and press the button 'Activate'.
#. Go to 'Action / Create Procedure' to generate the according Procedure.

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
