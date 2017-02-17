.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

============
Medical Labs
============

This module allows for the workflows necessary for storing Medical Lab test
data.

Definitions
===========

* ``Lab`` - A Lab is an order for a set of tests, and an encapsulation of the results
  from those tests. This record contains no personally identifying data regarding who
  the Lab was performed on. A Lab is defined by its Lab Test Type.
* ``Patient Lab`` - A Patient Lab is a Lab, but also contains the information regarding
  the Patient that the Lab was performed on.
* ``Test Type`` - A Lab Test Type defines the Testing Criteria that should be applied
  to a Lab. An example of a Test Type is an STD Screening.
* ``Test Criterion`` - A Test Criterion defines the expected range, units, and description
  for Test Types. An example of a Test Criterion is an HIV Test, as part of an STD
  Screening Test Type.
* ``Test Result`` - A Test Result represents the results from a Test Criterion.

Usage
=====

Labs can be ordered and processed in the ``Patient Labs`` section of the ``Medical`` app.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/159/9.0

Known issues / Roadmap
======================

* Add a lesser privileged user that can only see anonymized data.
* Add a menu for the anonymized data once safe to do so.
* Lab Reports in Patient More menu should be a smart button.

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
* Parthiv Patel <parthiv@techreceptives.com>
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
