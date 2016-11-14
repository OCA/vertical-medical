.. image:: https://img.shields.io/badge/license-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Medical Prescription - Order Merge
==================================

This module provides support for merging multiple existing prescription orders 
into one. Merging is handled by a wizard that allows users to select a list of 
orders that will be merged and a destination order, whose values will take 
precedence if there are conflicts. Many2many and one2many fields (e.g. 
prescription order lines) are always combined additively and cannot cause a 
conflict.

Installation
============

To install this module, simply follow the standard install process.

Configuration
=============

No configuration is needed or possible.

Usage
=====

To use this module, navigate to the prescription order list view and select 
the orders that you'd like to merge. Then choose "Merge" from the "Action" 
menu, which will start the merge wizard.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/10.0

Known Issues / Roadmap
======================

* Company-dependent fields are currently not supported and will not be 
  processed. Any values already present in these fields on the destination 
  order will remain unchanged after the merge.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues 
<https://github.com/OCA/vertical-medical/issues>`_. In case of trouble, please 
check there to see if your issue has already been reported. If you spotted it 
first, help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: 
  `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Oleg Bulkin <obulkin@laslabs.com>

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
