.. image:: https://img.shields.io/badge/license-GPL--3-blue.svg
    :target: http://www.gnu.org/licenses/GPL-3.0-standalone.html
    :alt: License: GPL-3

===============================
Medical Prescription Sale Stock
===============================

* This module adds dispense logic to prescription sale orders and integrates with the process of stock and inventory
  management found in the Odoo Inventory Management (stock) app. This also extends to OTC orders as well.

* Prescription order lines in the Medical panel will be highlighted red in the
  respective tree views if they cannot be dispensed due to lack of stock inventory available.

* The prescription order lines will also be red if there is a Date Stop Treatment defined and the current date is
  greater than the stop date.

Usage
=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/9.0

Known Issues / Roadmap
======================

* Implement determination for what drugs can be substituted (in _check_product)

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

Contributors
------------

* Dave Lasley <dave@laslabs.com>
* Brett Wood <bwood@laslabs.com>

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
