.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

=================================
Website Sale Medical Prescription
=================================

Extension providing prescription workflows in website_sale checkout process.


Usage
=====

* Create a product that is Prescription Only ``medical.medicament.is_prescription``
* Add it to cart in website
* Note, prescriptions with medicaments that are not in the current pricelist cannot be added to the cart.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/8.0

For further information, please visit:

* https://www.odoo.com/forum/help-1

Known issues / Roadmap
======================

Medicaments that are not in any pricelist cannot be added to the cart.
Make sure to select at least 'Different prices per customer segment' in
Sales -> Settings -> Sale Price. Then add that medicament to a pricelist
so it can be added to the cart when that pricelist is currently active.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/vertical-medical/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/vertical-medical/issues/new?body=module:%20website_sale_medical_prescription%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

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
