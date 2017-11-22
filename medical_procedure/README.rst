.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Medical Procedure
=================

This module adds medical procedure request and medical procedure.

A Procedure represents an action that is or was performed on a patient. This
can be a physical intervention like an operation, or less invasive like
counseling or hypnotherapy.

**This resource is used to record the details of procedures performed on a
patient.** A procedure is an activity that is performed with or on a patient as
part of the provision of care. Examples include surgical procedures, diagnostic
procedures, endoscopic procedures, biopsies, counseling, physiotherapy,
exercise, etc. Procedures may be performed by a healthcare professional, a
friend or relative or in some cases by the patient themselves.

This resource provides **summary information about the occurrence of the
procedure** and is not intended to provide real-time snapshots of a procedure
as it unfolds, though for long-running procedures such as psychotherapy, it
could represent summary level information about overall progress. The creation
of a resource to support detailed real-time procedure information awaits the
identification of a specific implementation use-case to share such information.

Some diagnostic procedures may not have a Procedure record. The Procedure record is
only necessary when there is a need to capture information about the physical
intervention that was performed to capture the diagnostic information (e.g.
anesthetic, incision, scope size, etc.).


=========================
Medical Procedure Request
=========================

**A Procedure Request is a record of a request for a procedure to be planned,
proposed, or performed with or on a patient.** Examples of procedures include
diagnostic tests/studies, endoscopic procedures, counseling, biopsies, therapies
(e.g., physio-, social-, psychological-), (exploratory) surgeries or procedures,
exercises, and other clinical interventions. Procedures may be performed by a
healthcare professional, a friend or relative or in some cases by the patient
themselves.

The general work flow that this resource facilitates is that a clinical system
creates a procedure request. The procedure request is then accessed by or
exchanged with a system, perhaps via intermediaries, that represents an
organization (e.g., diagnostic or imaging service, surgical team, physical
therapy department) that can perform the procedure. The organization receiving
the procedure request will, after it accepts the request, update the request as
the work is performed, and then finally issue a report that references the
requests that it fulfilled.

The Procedure Request resource allows requesting only a single procedure. If a
workflow requires requesting multiple procedures simultaneously, this is done
using multiple instances of this resource. These instances can be linked in
different ways, depending on the needs of the workflow.


Installation
============

To install this module, simply follow the standard install process.


Usage
=====
To create a Procedure Request or a Procedure:

#. Go to Medical -> Procedures -> Procedure or Procedure Request
#. Click "Create"
#. Enter the procedure request information and click "Save"

To create a Procedure from a Procedure Request:

#. Go to Medical -> Procedure -> Procedure Requests
#. Select a Procedure Request
#. Click "Action" -> Create Procedure

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
