.. image:: https://img.shields.io/badge/license-AGPL--3-blue.svg
    :alt: License: AGPL-3

======================
Medical Base -  Kanban
======================

This module provides abstract KanBan logic for use in Medical Resources.


Usage
=====

The ``medical.base.kanban`` model should be inherited in order to add KanBan
and Stage functionality to any record

.. code-block:: python

    class MyModel(models.Model):
        _name = 'my.model'
        _inherit = 'medical.base.kanban'
        
A Base KanBan view is also provided, which can be integrated into child views

.. code-block:: xml

    <record id="my_model_kanban_view" model="ir.ui.view">
        <field name="name">My Record</field>
        <field name="model">my.model</field>
        <field name="inherit_id" ref="medical_base_state.medical_base_kanban_view" />
        <field name="arch" type="xml">
            <!-- Add your contextual changes here w/ XPath -->
        </field>
    </record>

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/9.0

For further information, please visit:

* https://www.odoo.com/forum/help-1

Known issues / Roadmap
======================


Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/vertical-medical/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/vertical-medical/issues/new?body=module:%20medical_prescription_state%0Aversion:%209.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors
------------

* Dave Lasley <dave@laslabs.com>

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
