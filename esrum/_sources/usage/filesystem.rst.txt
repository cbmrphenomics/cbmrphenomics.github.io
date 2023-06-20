.. _filesystem_page:

################
 The filesystem
################

This section describes the layout of your home folder on Esrum, as well
as the location and layout of projects and data-shares.

.. _section_home:

******************
 Your home folder
******************

When you login to Esrum for the first time, your home folder should
contain a single folder named ``ucph``. This folder in turn contains
your KU network drives (formerly ``H:`` and ``N:``).

.. note::

   The shared drives are only accessible from the head node. If you need
   to analyze data located on either of these shared drives, then you
   will need to copy it an appropriate projects folder.

The primary use of your home folder is to store your programs and
scripts, configuration files, and similar files that are not related to
a specific project. For this reason, your home cannot exceed 100 GB in
size.

However, if possible it is recommended to keep your scripts in your
group project folder, to ensure that your group will have access to
these now and in the future:

.. warning::

   Do **not** put project related files in your home folder! Only you
   have access to your home folder and it requires written permission
   from you if other users need to access files in your home after
   you've left CBMR.

   Your home should therefore be limited to your personal configuration
   files, installed programs, and whatever/tools scripts that are not
   required to reproduce your work in the projects you are working on.

.. _section_projects:

**********************
 Your project folders
**********************

The majority of your work on Esrum should take place in the project
folder corresponding either to your research group or an actual project.
This ensures that people you are working with (group members or project
members) can access your results and that nobody else can! See the
:ref:`applying_for_projects` section for information about applying for
access to projects on Esrum.

Project folders are both are located in the ``/projects`` folder:

.. code::

   $ ls -1 /projects
   phenomics
   genotyping-AUDIT
   ...

To apply for access to a specific project follow the instructions in
:ref:`applying_for_access`, using the name of the project in the
following form ``COMP-PRJ-genotyping``, replacing ``genotyping`` with
the name of your project.

.. warning::

   Projects configured for GDPR data are marked with the ``-AUDIT``
   suffix. NEVER work on GDPR data in your home folder or in non-AUDIT
   projects!

Projects folder always contain the following four sub-folders:

-  ``/projects/<project-name>/people``

   Every member of a project has their own people folder. It is
   suggested that you keep your scripts, configuration files,
   documentation, and the like in this folder. The ``people`` folder is
   automatically backed up every day.

-  ``/projects/<project-name>/apps``

   The apps folder is intended for storing software shared between
   project members. See for example the :ref:`modules_page` for how to
   setup a shared repository of software that can be used with the
   module system. The ``apps`` folder is automatically backed up every
   day.

-  ``/projects/<project-name>/data``

   The ``data`` folder is intended for datasets shared between project
   members. This could be your raw data or your results files from
   processing your raw data. The ``data`` folder is automatically backed
   up every day.

-  ``/projects/<project-name>/scratch``

   The ``scratch`` folder is intended for temporary files. It is also
   suitable for files that do not need to be backed up, for example
   public databases or datasets used for a specific project.

Unlike your ``/home`` folder, there are no limits on how much you store
in these folders.

.. _red hat enterprise linux: https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux

.. _slurm: https://slurm.schedmd.com/overview.html
