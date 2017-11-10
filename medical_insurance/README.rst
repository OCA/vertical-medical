.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

======================
Odoo Medical Insurance
======================

Extension of medical that provides Insurance concept.

Configuration
=============

To configure this module, you need to:

#. Go to 'Medical/Insurance/Insurance Providers' and create an Insurance
   Provider.
#. Go to 'Medical/Insurance/Insurance Plan Template' and create a Plan Template
   with an Insurance Provider and an Insurance Product.

Usage
=====

In order to create an Insurance Plan for a patient:

#. Go to 'Medical/Patient/Patient' and create a Patient.
#. Go to 'Medical/Insurance/Insurance Plans' and create a new Insurance Plan
   with the Patient and using the according Insurance Plan Template.
#. Go to the patient and in the page 'Medical' you can see the new Insurance
   Plan for that patient.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/11.0

For further information, please visit:

* https://www.odoo.com/forum/help-1

Known issues / Roadmap
======================

* Improve and provide a full description for this module into the README.rst

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

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Dave Lasley <dave@laslabs.com>
* Jonathan Nemry <jonathan.nemry@acsone.eu>
* Parthiv Patel <parthiv@techreceptives.com>
* Ruchir Shukla <ruchir@techreceptives.com>
* Parthiv Patel <parthiv@techreceptives.com>
* Nhomar Hernandéz <nhomar@vauxoo.com>
* Jordi Ballester <jordi.ballester@eficent.com>
* Roser Garcia <roser.garcia@eficent.com>
* Gisela Mora <gisela.mora@eficent.com>
* Enric Tobella <etobella@creublanca.es

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
