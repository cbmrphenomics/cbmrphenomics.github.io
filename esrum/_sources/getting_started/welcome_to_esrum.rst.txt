##################
 Welcome to Esrum
##################

The Esrum cluster runs `Red Hat Enterprise Linux`_ 8.7 (Ootpa) and uses
the Slurm_ job management system for running tasks on the available
nodes.

For a description of software available on Esrum, as well as
instructions for adding your own software, see TODO. For an introduction

******************
 Your home folder
******************

When you login to Esrum for the first time, your home folder should
contain a single folder named `ucph`. This folder in turn contains your
KU network drives (formerly `H:` and `N:`).

The primary use of your home folder is to store programs, your own
scripts, configuration files, and similar files that are not related to
a specific project. However, if possible it is recommended to keep your
scripts in your group project folder, to ensure that your group has
access as well:

.. warning::

   Do **not** put project related files in your home folder! Only you
   have access to your home folder and it requires written permission
   from you if other users need to access files in your home after
   you've left CBMR.

   Your home should therefore be limited to your personal configuration
   files, installed programs, and whatever/tools scripts that are not
   required to reproduce your work in the projects you are working on.

**********************
 Your project folders
**********************

The majority of your work on Esrum should take place in the folder
corresponding either to your group or a specific project. Folders for
both are located in the `/projects` folder:

.. code::

   $ ls -1 /projects
   phenomics
   genotyping-AUDIT
   ...

To apply for access to a specific project follow the instructions in
:ref:`applying_for_access`, using the name of the project in the
following form `COMP-PRJ-genotyping`, replacing `genotyping` with the
name of your project.

.. warning::

   Projects configured for GDPR data are marked with the `AUDIT`. NEVER
   work on GDPR data in your home folder or in non-AUDIT projects!

.. _red hat enterprise linux: https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux

.. _slurm: https://slurm.schedmd.com/overview.html
