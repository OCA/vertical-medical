.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

===============
Plan definition
===============

A plan definition is a pre-defined group of actions to be taken in particular
circumstances, often including conditional elements, options, and other
decision points. The resource is flexible enough to be used to represent a
variety of workflows, as well as clinical decision support and quality
improvement assets, including order sets, protocols, and decision support rules.

Plan Definitions can contain hierarchical groups of action definitions, where
each specific action definition describes an activity to be performed (in terms
of an Activity Definition resource), and each group defines additional
behavior, relationships, and applicable conditions between the actions in the
overall definition.

The process of applying a Plan Definition to a particular context typically
produces request resources representing the actions that should be performed,
typically grouped within a Care Plan and a Request Group to capture
relationships between the resulting request resources.

Each Activity Definition is used to construct a specific resource, based on
the definition of the activity and combined with contextual information for the
particular patient that the plan definition is being applied to.

As with the ActivityDefinition, a Plan Definition may provide information about
how to transform the activity to a specific intent resource by specifying values
for specific elements of the resulting resource using elements in the action.

Note that these mechanisms are provided on both the Activity Definition and
the Plan Definition to allow both reusable transformation descriptions, as
well as customization of those descriptions within specific contexts.

Installation
============

To install this module, simply follow the standard install process.

Configuration
=============

Define Workflow Types
---------------------
#. Go to Workflow / Configuration / Workflow Types
#. Create a new Workflow Type.

Usage of main activity definition on plans
------------------------------------------

It is possible to add a main activity definition on plans in order to create
a parent activity.
You can configure it on Medical / Configuration / Settings

Add plan definitions directly on patients
-----------------------------------------

It is possible to add a plan configuration on patients.
You can configure this option on Medical / Configuration / Settings.

Once it is allowed, you can add it on a patient through a button on the header
of patient

Usage
=====
#. Go to Workflow / Activity definition
#. Create an activity definition for each activity you want to have
#. Go to Workflow / Plan definition
#. Create a new Plan Definition, choose a workflow type and add as many actions
   as this plan needs. For every action, you can associate an activity
   definition to it.
   Every action can contain a list of actions.

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

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

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
