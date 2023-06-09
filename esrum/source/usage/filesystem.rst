.. _filesystem_page:

###################
 Files and folders
###################

This section describes the layout of your home folder on Esrum, as well
as the location and layout of projects and data-shares.

.. _section_home:

******************
 Your home folder
******************

The primary use of your home folder is to store your programs and
scripts, configuration files, and similar files that are not related to
specific projects. For this reason, your home cannot exceed 100 GB in
size.

However, we recommended to keep your scripts and similar files in your
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

KU network drives
=================

When you login to Esrum for the first time, your home folder should
contain a single folder named ``ucph``. This folder in turn contains
your KU network drives (formerly ``H:`` and ``N:``).

Note that these drives are only accessible from the head node. If you
need to analyze data located on either of these shared drives, then you
will need to copy it an appropriate projects folder.

.. _section_projects:

**********************
 Your project folders
**********************

The majority of your work on Esrum should take place in project folder
corresponding either to your research group or to actual projects. This
ensures that your collaborators can access your results and that nobody
else can!

Project folders are located in the ``/projects`` folder:

.. code::

   $ ls -1 /projects
   phenomics-AUDIT
   genotyping
   ...

The ``-AUDIT`` suffix indicates that the phenomics project has been
configured for work on GDPR data. All work on GDPR data should take
place in project or data-shares (see below) marked with ``-AUDIT`` and
*nowhere else*!

To apply for access to a specific project follow the instructions in the
:ref:`applying_for_access` section, using the name of the project in the
form ``COMP-PRJ-genotyping``, replacing ``genotyping`` with the name of
your project.

Projects folder always contain the following four sub-folders:

-  ``/projects/<project-name>/people``

   Every member of a project has their own folder in ``people``. It is
   suggested that you keep your scripts, configuration files,
   documentation, and the like in this folder. The ``people`` folder is
   automatically backed up every day.

-  ``/projects/<project-name>/apps``

   The apps folder is intended for storing software shared between
   project members. See :ref:`modules_page` for how to setup a shared
   repository of software that can be used with the module system. The
   ``apps`` folder is automatically backed up every day.

-  ``/projects/<project-name>/data``

   The ``data`` folder is intended for datasets shared between project
   members. This could be your raw data or your results files from
   processing your raw data. The ``data`` folder is automatically backed
   up every day.

-  ``/projects/<project-name>/scratch``

   The ``scratch`` folder is intended for temporary files, as it is
   *not* backed up. It is also suitable for other files that do not need
   to be backed up, including for example publicly available datasets,
   large index files, and such.

Unlike your ``/home`` folder, there are no limits on how much you store
in these folders.

*****************
 Backup policies
*****************

..
   TODO: Briefly describe backup policies

.. _red hat enterprise linux: https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux

.. _slurm: https://slurm.schedmd.com/overview.html
