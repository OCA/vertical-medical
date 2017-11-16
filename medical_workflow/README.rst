.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

================
Medical Workflow
================

The Workflow Module focuses on the coordination of activities within and
across systems.

In addition to the Task resource, this specification defines three logical
models - Definition, `Request <https://www.hl7.org/fhir/request.html>`_ and
`Event <https://www.hl7.org/fhir/event.html>`_ that define the patterns for
resources that are typically involved in workflow. These patterns include
elements defining common attributes of each type of resource as well as
relationships between them.

Finally the `Plan definition <https://www.hl7.org/fhir/plandefinition.html>`_
and `Activity definition <https://www.hl7.org/fhir/activitydefinition.html>`_
resources combine to support the creation of protocols, orders sets,
guidelines and other workflow definitions by describing the types of
activities that can occur and setting rules about their composition,
sequencing, interdependencies and flow.

For more information about the FHIR Workflow model visit: https://www.hl7.org/fhir/workflow-module.html

Installation
============

#. To install this module, go to 'Medical / Configuration / Settings' and inside
   'Workflow' activate 'Workflow'.

Usage
=====

#. Go to 'Medical / Workflow / Workflow Types'
#. Click 'Create' and fill in all the required information.
#. Click 'Save'.
#. Go to 'Medical / Workflow / Activity definitions'
#. Click 'Create' and fill in all the required information.
#. Click 'Save'.
#. Go to 'Medical / Workflow / Plan definitions'
#. Click 'Create'.
#. Provide a name and create actions by providing a name and an Activity
   Definition or a Plan Definition.
#. Click 'Save'.

Plan definition on patients
---------------------------
#. Go to 'Medical / Configuration / Settings' and inside
   'Workflow' activate 'Plan definition on patients'.
#. Go to 'Medical / Administration / Patients'
#. Select a patient and press the button 'Add Plan definition'. Automatically
   the requests are generated.

Main activity on plan definitions
---------------------------------
#. Go to 'Medical / Configuration / Settings' and inside
   'Workflow' activate 'Main activity on plan definition'.
#. Go to 'Medical / Workflow / Plan definitions'
#. Add an activity definition to the plan.

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
