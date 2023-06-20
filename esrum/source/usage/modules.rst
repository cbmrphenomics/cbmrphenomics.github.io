.. _modules_page:

###################
 The module system
###################

`Environment modules`_ provides a method by which users of the cluster
can access a wide range of software, including different versions of the
same software.

Modules on Esrum are primarily provided by KU-IT (see below), but users
may also set up their own private or shared environment modules. See the
:ref:`creating_modules_page`

*************
 Basic usage
*************

This section briefly describe how to carry out common tasks using the
module system: Finding what modules are available, loading a module, and
unloading them again. For more information see the `official
documentation`_.

Finding available modules
=========================

The first step is to determine what modules are available on the server.
This is accomplished with the `module avail` command:

.. code:: shell

   $ module avail
   -------------------------- /opt/software/modules --------------------------
   anaconda2/4.0.0            libpng/1.6.39               texlive/2023
   anaconda3/4.0.0            libtool/2.4.7               tiff/4.5.0
   anaconda3/5.3.1            libuv/1.44.2                topspin/4.1.4
   anaconda3/2020.11          libxkbcommon/1.3.0          trimgalore/0.6.6
   anaconda3/2021.05          libxscrnsaver/1.0.0         trnascan-se/2.0.11
   [...]

The command can also be used to search for specific modules by
specifying one or more keywords:

.. code:: shell

   $ module avail sam
   -------------------------- /opt/software/modules --------------------------
   samtools/1.12  samtools/1.17

The modules are loaded using the `module load` command: This adds the
executable to your PATH and performs any other setup required to run the
software.

Loading a module
================

.. code:: shell

   $ samtools
   -bash: samtools: command not found
   $ module load samtools
   $ samtools
   Program: samtools (Tools for alignments in the SAM format)
   Version: 1.17 (using htslib 1.17)
   [...]

Multiple modules may be specified per `module load` command and it i
also possible to specify the exact version that you need, provided that
a module is available:

.. code:: shell

   $ module load samtools/1.12
   $ samtools
   Program: samtools (Tools for alignments in the SAM format)
   Version: 1.12 (using htslib 1.12)
   [...]

In some cases one module will require another module:

.. code:: shell

   $ module load bcftools
   Loading bcftools/1.16
   ERROR: bcftools/1.16 cannot be loaded due to missing prereq.
      HINT: the following module must be loaded first: perl

In that case you simply need to load the required module first. This can
be done in done manually:

.. code:: shell

   $ module load perl
   $ module load bcftools

Or automatically:

.. code:: shell

   $ module load --auto bcftools
   Loading bcftools/1.16
     Loading requirement: perl/5.26.3

Listing and unloading loaded modules
====================================

The modules you have loaded can be listed using the `module list`
command:

.. code:: shell

   $ modules list
   Currently Loaded Modulefiles:
    1) perl/5.26.3   2) bcftools/1.16   3) samtools/1.12

To remove a module that you no longer need, use the `module unload`
command to unload a single module or the `module purge` command to
unload all modules:

.. code:: shell

   # Unload the samtools module
   $ module unload samtools
   # Unload the remaining modules
   $ module purge
   $ modules list
   No Modulefiles Currently Loaded.

***********************************
 Making your analyses reproducible
***********************************

As described above you can load modules with or without specific
versions. For a lot of software it is not very important that a specific
version used, but even so it is highly recommended that you keep using
the same versions of modules throughout a project.

-  It documents what software you used to run your analyses.
-  It ensures that your results do not change (subtly or greatly) when
   new versions of software are installed.

There are two ways to ensure that you are using the same versions of
modules: Either using the built-in `save/restore` functionality or using
a script containing `module load` commands.

Managing modules with `module save/restore`
===========================================

To use the built-in functionality, run the following commands:

.. code:: shell

   $ module config collection_pin_version 1
   $ module save ./modules.txt

There are two important points here: Firstly, the `module config
collection_pin_version 1` command *must* be run first. If this is not
done, then the specific versions of modules are not recorded!

Secondly, the filename used in the second command (`./modules.txt`)
*must* contain a directory component (e.g. `./`). If this is not done,
then the list is saved in a database and won't be accessible to other
users!

If used correctly, the `./modules.txt` file will contain the currently
loaded modules, e.g:

.. code:: shell

   $ module list
   Currently Loaded Modulefiles:
   1) gcc/11.2.0   2) samtools/1.17   3) perl/5.26.3   4) bcftools/1.16
   $ module config collection_pin_version 1
   $ module save ./modules.txt
   $ cat modules.txt
   module use --append /opt/software/modules
   module load gcc/11.2.0
   module load samtools/1.17
   module load perl/5.26.3
   module load bcftools/1.16

To load the saved modules, simply run `module restore` with the same
filename (and a directory component):

.. code:: shell

   $ module list
   No Modulefiles Currently Loaded.
   $ module save ./modules.txt
   $ module list
   Currently Loaded Modulefiles:
   1) gcc/11.2.0   2) samtools/1.17   3) perl/5.26.3   4) bcftools/1.16

Managing modules with a script
==============================

The other solution is to write a script containing one or more `module
load` commands:

.. code:: shell

   $ cat modules.txt
   module load gcc/11.2.0
   module load samtools/1.17
   module load perl/5.26.3
   module load bcftools/1.16

To load these modules use the command `. modules.sh` (dot space
filename) or `source modules.sh`:

.. code:: shell

   $ module list
   No Modulefiles Currently Loaded.
   $ . modules.sh
   $ module list
   Currently Loaded Modulefiles:
   1) gcc/11.2.0   2) samtools/1.17   3) perl/5.26.3   4) bcftools/1.16

Simply running the script with `bash modules.sh` will not work, as the
`.` / `source` commands inject the `module` or other commands into your
current shell.

.. _requesting_missing_modules:

****************************
 Requesting missing modules
****************************

If software you are missing is not available as a module, you may
request this software through KU-IT as described below. You are welcome
to :ref:`page_contact` if you need help determining which exact software
and/or versions you need to request.

To request software,

#. Login to the KU `IT Serviceportal`_.
#. Click the ``Create Ticket`` button.
#. Select the ``Research IT`` category.
#. Then select the ``Research Applications and Services`` subcategory.
#. Finally, select ``Consultancy and Support``.
#. List what software you wish to have installed in the "Please
   describe" text-box (see below).
#. Write "esrumhead01fl.unicph.domain" in the System name text-box.
#. Click the ``Add to cart`` button.
#. Click the ``SUBMIT ORDER`` button.

Your request should include the following information:

#. The name of the software.
#. The specific version requested (if any).
#. The homepage of the software.

A request may look like the following:

.. code::

   Requesting the addition of environment modules for the following software:

   1. seqtk v1.4 (https://github.com/lh3/seqtk)
   2. jq v1.5 (https://stedolan.github.io/jq/)
   3. igzip v2.30.0 (https://github.com/intel/isa-l)

.. _environment modules: https://modules.sourceforge.net/

.. _it serviceportal: https://serviceportal.ku.dk/

.. _official documentation: https://modules.readthedocs.io/en/v4.5.2/
