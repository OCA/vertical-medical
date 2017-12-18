.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

=================
Medical Condition
=================

This resource is used to record detailed information about a condition,
problem, diagnosis, or other event, situation, issue, or clinical concept
that has risen to a level of concern.

It can be used to record information about a disease/illness identified from
application of clinical reasoning over the pathologic and pathophysiologic
findings (diagnosis), or identification of health issues/situations that a
practitioner considers harmful, potentially harmful and may be investigated
and managed (problem), or other health issue/situation that may require
ongoing monitoring and/or management (health issue/concern).

The condition resource may be used to record a certain health state of a
patient which does not normally present a negative outcome, e.g. pregnancy.
The condition resource may be used to record a condition following a
procedure, such as the condition of Amputee-BKA following an amputation
procedure.

While conditions are frequently a result of a clinician's assessment and
assertion of a particular aspect of a patient's state of health, conditions
can also be expressed by the patient, related person, or any care team member.
A clinician may have a concern about a patient condition (e.g. anorexia) that
the patient is not concerned about. Likewise, the patient may have a
condition (e.g. hair loss) that does not rise to the level of importance such
that it belongs on a practitioner’s Problem List.

For example, each of the following conditions could rise to the level of
importance such that it belongs on a problem or concern list due to its
direct or indirect impact on the patient’s health:

* Unemployed
* Without transportation (or other barriers)
* Susceptibility to falls
* Exposure to communicable disease
* Family History of cardiovascular disease
* Fear of cancer
* Cardiac pacemaker
* Amputee-BKA
* Risk of Zika virus following travel to a country
* Former smoker
* Travel to a country planned (that warrants immunizations)
* Motor Vehicle Accident
* Patient has had coronary bypass graft

For further information about FHIR Condition visit: https://www.hl7.org/fhir/condition.html

Installation
============

To install this module, go to 'Medical / Configuration / Settings' and inside
'Clinical' activate 'Medical condition'.

Usage
=====

#. Go to 'Medical / Terminologies / Clinical Finding Codes'
#. Click 'Create'.
#. Provide a name and (if desired) a description and a Sct Code.
#. Click 'Save'.
#. Go to 'Medical / Administration / Patients'
#. Select a patient and press the button 'Conditions'
#. Create a new clinical condition by providing a Clinical Finding and
   specifying whether it is a problem or a diagnosis.
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
