.. sectnum::
    :start: 1

All the coding guidelines of OeMEdical is based on 
`OpenERP guidelines for coding.`_

Some exceptions in Styles are in this code that you must to follow to approve 
`merge proposals`_ and ensure the quality of the system.

Coding Styles
+++++++++++++

What will be considered good or bad code to merge in core.

Your code should be pep8 compliant.
-----------------------------------

In order to be sure our code is of high wuality, is important use some 
conventions in the python world the most accepted is the `pep8 convention`_, 
we will use it in this project.

If you develop in a linux enviroment you can install ``pep8`` program:

.. code-block:: guess

  sudo apt-get install pep8
  
With this program you will be able to test your code before the `merge proposals`_
or even test the code of other person to help us to answer with Q&A reasons 
before commit or merge changes.

i.e:

.. code-block:: guess
  
  pep8 yourpythonfile.py
  
It will return a set of results about the quality of your code see 
``pep8 --help`` for more information.

About new objects
-----------------

A new object is this one that for functional or design reasons is not included 
on the core of OpenERP.

New classes signature.
"""""""""""""""""""""'

All new classes must start with ``OeMedicalName`` see it in `CamelCase`.

i.e.:

.. literalinclude:: snnipets/snnipets.py
  :lines: 2

New Object name.
"""""""""""""""'

All new objects will complay with OpenERP standard it means separated by one dot
between words.

i.e.

.. literalinclude:: snnipets/snnipets.py
  :lines: 15

New method signature.
"""""""""""""""""""""

All new methods will be named with `snake_case`.

File management for new objects
""""""""""""""""""""""""""""""'

All new objects will be in a new folder, with both xml and py files, see 
``oemedical`` modules for some example.

About Openerp Version.
----------------------

In version 1.0 of OeMedical we decide work with version 7.0 of OpenERP, for 
this reason some specific conventions must be verified.

Views 7.0 compatibles.
"""""""""""""""""""""'

All views that use OeMedical will comply with version 7.0 of OpenERP.

About Data for Standards.
-------------------------

Data loaded should be in an extra module called oemedical_yourstandard_data, 
to separate data errors from model errors, frequently data dont change too much, 
because it is based on Standards.

.. warning::

  If the data is necesary for the correct work of your module this rule 
  do not apply

About Complementary Modules.
----------------------------

Modules that improve functionality working with the core of openerp, should be 
in an extra module, it means.

i.e:

* Creation of Automated invoices and commercial management: oemedical_account
* Relation with sale orders: oemedical_sale
* Relation with purchase: oemedical_purchase

Avoid use names not self descriptive, as `oemedical_purchase_ext`, the correct 
sufix should say what it is improving.

Useability Guidelines.
----------------------

If a model is inherited, we should create them own view with them own action, 
to be sure the user is able to use this model in its functional context without 
unnecesary information in this function.

Technical requirements.
-----------------------

If a model impact some kind of a more than 3 steps flow, the object ``MUST`` have 
Workflow.

Documentation Guidelines
++++++++++++++++++++++++

In order to be sure the useabilty and to avoid not re-use the job of others 
members of community will not be merged any module or improvement that is not 
correct documented.

How Documentation will be included.
-----------------------------------

All documentation will be in a web_doc_yourmodule module to be able to embed documentation compiled with sphinx in the same server.

.. note::

  TODO: Put some example or link to a branch with a basic template for this 
  kind of module.

Guidelines to document your improvement.
----------------------------------------

We must try to document following `pep-0257 convention`_.

As the standard is a little extense we share some useful snnipets, with some 
examples.

.. literalinclude:: snnipets/snnipets.py
  :lines: 48-66

It is important understand that the documentation with pep standards just 
propose some good practices from the technical point of view, to be sure all 
is correct and all community involved has the correct approach about what 
document and how, some premises are listed below, and the community can propose 
another ones to follow, in the middle this methodology can be reviewed and 
improved.

About comments in code:
-----------------------

At least the model is still on development, we must avoid code commented, 
all commentaries must be usuables by sphinx to use `autodoc`_ embebed.

Try to commit with a really `explicit`_ message to avoid unecessary comments

.. footer::

 All discussion regading this guidelines is in Launchpad on this topic, you can 
 collaborate in this `discussion`_

.. _pep-0257 convention: http://www.python.org/dev/peps/pep-0257/
.. _OpenERP guidelines for coding.: http://doc.openerp.com/v6.1/contribute/15_guidelines/coding_guidelines.html
.. _merge proposals: https://help.launchpad.net/Code/Review?action=show&redirect=BranchMergeProposals
.. _explicit: http://doc.openerp.com/v6.1/contribute/15_guidelines/coding_guidelines_framework.html#bazaar-is-your-historian
.. _pep8 convention: http://www.python.org/dev/peps/pep-0008/
.. _autodoc: http://sphinx-doc.org/ext/autodoc.html#directive-autoattribute
.. _discussion: https://blueprints.launchpad.net/oemedical/+spec/coding-guidelines