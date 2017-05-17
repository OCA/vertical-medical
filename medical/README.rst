.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

============
Odoo Medical
============

This module extends Odoo with the base functionality of medical patients.

Installation
============

This module depends on modules located in the following repos:
* https://github.com/OCA/partner-contact

Check the ``__manifest__.py`` for the specific dependencies.

Usage
=====

Patients
--------

Patients are available in the ``Medical`` App, in the ``Patients`` submenu.

Medical Abstract Entity
-----------------------

The Medical Abstract Entity (``medical.abstract.entity``) is an AbstractModel
that provides for a central base that all medical entities should inherit from.

A Medical Entity is any partner that also requires a medical context. Examples:

* MedicalCenter
* MedicalPatient
* MedicalPhysician
* MedicalPharmacy

Some base views are also provided in order to make it easy to create new medical
entities & maintain uniformity between them:

* Kanban - ``medical_asbsract_entity_view_kanban``
* Tree - ``medical_asbsract_entity_view_tree``
* Form - ``medical_asbsract_entity_view_form``
* Search - ``medical_asbsract_entity_view_search``

When inheriting these views, you must define the inheritance mode as ``primary``,
such as in the following example:

    .. code-block:: xml
    <record id="medical_patient_view_tree" model="ir.ui.view">
        <field name="name">medical.patient.tree</field>
        <field name="model">medical.patient</field>
        <field name="inherit_id" ref="medical_abstract_entity_view_tree" />
        <field name="mode">primary</field>
        <field name="arch" type="xml">
            <xpath expr="//tree" position="attributes">
                <attribute name="string">Patients</attribute>
            </xpath>
            <xpath expr="//field[@name='email']" position="after">
                <field name="identification_code" />
                <field name="age" />
                <field name="gender" />
            </xpath>
        </field>
    </record>

Take a look at ``medical/views/medical_patient.xml``, or any of the other medical
entity views for more examples.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/10.0

Known issues / Roadmap
======================

* There is a singleton issue with the ID numbers pass-thru & crossing could
  occur.
* v11 - Move Marital status into a new module in OCA/partner-contact

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/vertical-medical/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.
* DevCom: `Patient Avatar <http://www.devcom.com/>`_.

Contributors
------------

* Dave Lasley <dave@laslabs.com>
* Jonathan Nemry <jonathan.nemry@acsone.eu>
* Brett Wood <bwood@laslabs.com>
* Ruchir Shukla <ruchir@techreceptives.com>
* Parthiv Patel <parthiv@techreceptives.com>
* Nhomar Hernandéz <nhomar@vauxoo.com>

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
