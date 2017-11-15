.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

====================
Medical Practitioner
====================

This module adds medical practitioners.

Practitioner covers all individuals who are engaged in the healthcare process
and healthcare-related services as part of their formal responsibilities.

The PractitionerRole resource provides the details of roles that the
practitioner is approved to perform for which organizations.

Practitioners include (but are not limited to):

* Physicians, dentists, pharmacists
* Physician assistants, nurses, scribes
* Midwives, dietitians, therapists, optometrists, paramedics
* Medical technicians, laboratory scientists, prosthetic technicians,
  radiographers
* Social workers, professional home carers, official volunteers
* Receptionists handling patient registration
* IT personnel merging or unmerging patient records
* Service animal (e.g., ward assigned dog capable of detecting cancer in
  patients)

For further information about FHIR Practitioner visit: http://hl7.org/fhir/practitioner.html.
For more information about FHIR Practitioner Role visit: http://hl7.org/fhir/practitionerrole.html

Installation
============

To install this module, go to 'Medical / Configuration / Settings' and inside
'Administration' activate 'Practitioner'.

Usage
=====

#. Go to 'Medical / Configuration / Roles'
#. Create a new role by providing a name and a description.
#. Click 'Save'.
#. Go to 'Medical / Administration / Practitioners'
#. Click 'Create' by providing a name. Choose whether if the practitioner is
   an internal employee (Internal Entity) or external employee (External
   Entity). Below this, you can choose the roles this practitioner has.
#. Click 'Save'

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

* Ken Mak <kmak@laslabs.com>
* Brett Wood <bwood@laslabs.com>
* Dave Lasley <dave@laslabs.com>
* Enric Tobella <etobella@creublanca.es>
* Roser Garcia <roser.garcia@eficent.com>

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
