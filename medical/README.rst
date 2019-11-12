.. image:: https://img.shields.io/badge/license-GPL--3-blue.svg
    :target: http://www.gnu.org/licenses/gpl-3.0-standalone.html
    :alt: License: GPL-3

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
* Jordi Ballester Alomar <jordi.ballester@eficent.com>

The current project as it is today represents an evolution of the original work
started by Luis Falcon. See https://sourceforge.net/projects/medical/files/Oldfiles/1.0.1,
that later became GNU Health (see
http://health.gnu.org/). The original code was licensed under GPL.

On Nov 27, 2012 derivative code was published in https://github.com/OCA/vertical-medical,
by Tech-Receptives Solutions Pvt. Ltd., licensed
under AGPL.  The license change was unauthorized by the original
author. See https://github.com/OCA/vertical-medical/commit/f0a664749edaea36f6749c34bfb04f1fc4cc9ea4

On Feb 17, 2017 the branch 9.0 of the project was relicensed to LGPL.
https://github.com/OCA/vertical-medical/pull/166. Various prior contributors
approved the relicense, but not all.

On Jan 25, 2018, GNU Health claimed that the original code and attribution
should be respected, and after further investigation the Odoo Community
Association Board agreed to switch the license back to GPL v3 to respect the
rights of the original author.

Although no trace of relationship was found between the code at the date
and the original code from 2012, through the commit history of the project one
can see that the current status of the project is the end result of an
evolutionary process. The Odoo Community Association Board concluded that
the original license should be respected for ethical reasons.

More information can be read here - https://odoo-community.org/blog/our-blog-1/post/vertical-medical-75.

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
