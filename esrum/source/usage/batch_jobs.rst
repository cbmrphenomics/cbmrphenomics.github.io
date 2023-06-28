.. _page_batch_jobs:

####################
 Running batch jobs
####################

Unlike the ``srun`` command, the ``sbatch`` command is designed to run
commands in batches and therefore does not wait for the queued command
to terminate. Furthermore, the ``sbatch`` command does not run commands
directly but instead executes a script in which options for ``sbatch``
may be specified using comments (see below).

In other words, ``sbatch`` is equivalent to the ``qsub`` command used on
the old cluster, but note that command-line options are not the same!

The following gives a brief overview of how to perform common tasks,
with additional resources and templates provided at the end of the page.

******************
 A simple example
******************

The following ``srun`` command compresses a file using 8 cores using the
parallel gzip alternative ``pigz``, with a maximum runtime of 60
minutes:

.. code:: shell

   $ srun --cpus-per-task 8 --time=60 pigz --processes 8 chr1.fasta

This may be converted to the following bash script (``my_script.sh``):

.. code:: bash

   #!/bin/bash
   #SBATCH --cpus-per-task=8
   #SBATCH --time=60

   pigz --processes 8 chr1.fasta

Note how options are supplied using ``#SBATCH`` comments at the top of
the file. The same options may alternatively be specified on the
command-line, just like with ``srun``, but it is often helpful to record
your parameters in your batch script.

This resulting script can in turn be run using the ``sbatch`` command
and it's status checked using the ``squeue`` command:

.. code:: shell

   $ ls
   chr1.fasta my_script.sh
   $ sbatch my_script.sh
   Submitted batch job 8503
   $ squeue --me
   JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    8503 standardq my_scrip   abc123  R       0:02      1 esrumcmpn01fl

The ST column indicating the status of the job (R for running, PD for
pending, `and so on
<https://slurm.schedmd.com/squeue.html#SECTION_JOB-STATE-CODES>`_).
Completed jobs are removed from the ``squeue`` list and can instead be
listed using ``sacct``:

.. code:: shell

   $ sacct
   JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
   ------------ ---------- ---------- ---------- ---------- ---------- --------
   8503         my_script+ standardq+                     8  COMPLETED      0:0
   8503.batch        batch                                8  COMPLETED      0:0
   $ ls
   chr1.fasta.gz my_script.sh slurm-8503.out

The ``slurm-8503.out`` file contains any console output produced by your
script/commands. In this case it is an empty file, but it is

***********************************************
 Command-line options and ``#SBATCH`` comments
***********************************************

As shown above it is possible to specify options for ``sbatch`` using
either command-line options or ``#SBATCH`` comments in your scripts.
There are, however, a few caveats:

-  The ``#SBATCH`` lines must be at the top of the file, before any
   other commands or the like. Moreover, there must be no spaces before
   or after the ``#`` in the ``#SBATCH`` comments. Other comments (lines
   starting with ``#``) are allowed.

-  It is also possible to embed ``#SBATCH`` comments in for example
   Python scripts, if you want to run a Python script directly, but note
   that formatting tools like ``black`` may attempt to re-format the
   ``#SBATCH`` comments and break the script.

-  Options specified on the command-line takes precedence: If you run
   ``sbatch --cpus-per-task=4 my_script.sh`` and ``my_script.sh``
   contains the line ``#SBATCH --cpus-per-task=8``, then your job will
   be assigned 4 CPUs instead of 8.

-  Finally, any command-line options meant for ``sbatch`` must be
   written *before* the filename of the batch script:

   .. code:: shell

      $ sbatch --option my_script.sh

   If the option is instead placed *after* ``my_script.sh``, then it is
   passed to that script.

Common options
==============

The following provides a brief overview of common options for ``sbatch``
not mentioned above. There is a significant overlap between ``sbatch``
and ``srun``, including for example how to request resources (see
:ref:`reserving_resources`), and this section will not cover those
options.

All of these options may be specified using ``#SBATCH`` comments.

-  The ``--name`` option allows you to give a name to your job. This
   shows up when using ``squeue``, ``sacct`` and more. If not specified,
   the name of your script is used instead.

-  The ``--output`` and ``--error`` options allow you to specify where
   Slurm writes your scripts STDOUT and STDERR. The filenames should
   always include the text ``%j``, which is replaced with the job ID.
   See the manual page for usage. Note also that the destination folder
   *must* exist or no output will be saved!

-  ``--time`` can be used to limit the maximum running time of your
   script. We do not require that ``--time`` is set, but it may be
   useful to automatically stop jobs that unexpectedly take too long to
   run. See the ``sbatch`` manual page for how to specify time limits.

-  ``--test-only`` can be used to test your batch scripts. Combine it
   with ``--verbose`` to verify that your options are correctly set
   before queuing your job:

   .. code:: shell

      $ sbatch --test-only --verbose my_script.sh
      sbatch: defined options
      sbatch: -------------------- --------------------
      sbatch: cpus-per-task       : 8
      sbatch: test-only           : set
      sbatch: time                : 01:00:00
      sbatch: verbose             : 1
      sbatch: -------------------- --------------------
      sbatch: end of defined options
      [...]
      sbatch: Job 8568 to start at 2023-06-28T12:15:32 using 8 processors on nodes esrumcmpn02fl in partition standardqueue

-  The ``--wait`` option can be used to make the ``sbatch`` block until
   the queued tasks have completed. This can be useful if you want to
   run sbatch from another script.

**********************
 Monitoring your jobs
**********************

Slurm offers a number of ways in which you may monitor your jobs:

The ``squeue`` command allows you to list jobs that have not yet
finished (or failed). The recommended use is either ``squeue --me`` to
show all your jobs or ``squeue --job ${JOB_ID}``, where ``${JOB_ID}`` is
the ID of the job whose status you want to inspect.

The ``sacct`` command allows you list jobs that have finished running
(or failed).

In addition to actively monitoring your jobs, it is possible to receive
email notifications when your jobs are started, finish, fail, are
requeued, or some combination. This is accomplished by using the
``--mail-user`` and ``--mail-type`` options:

.. code:: shell

   $ sbatch my_script.sh --mail-user=abc123@ku.dk --mail-type=END,FAIL
   Submitted batch job 8503

When run like this, you will receive notifications at ``abc123@ku.dk``
(remember to use your account KU email address!) when the job is
completed or fails. The possible options are ``NONE`` (the default),
``BEGIN``, ``END``, ``FAIL``, ``REQUEUE``, ``ALL``, or some combination
as shown above.

***************
 Managing jobs
***************

*************************************
 Running multiple tasks using arrays
*************************************

As noted above the ``sbatch`` command is meant to run jobs in batches.
This is accomplished using "job arrays", which allows you to
automatically queue and run the same command on multiple inputs.

For example, we could expand on the example above to gzip multiple
chromosomes using a job array. To do so, we first need to update the
script to make use of the ``SLURM_ARRAY_TASK_ID`` variable, which
specifies the numbered ID of a task:

.. code:: bash

   #!/bin/bash
   #SBATCH --cpus-per-task=8
   #SBATCH --time=60
   #SBATCH --array=1-3

   pigz --processes 8 chr${SLURM_ARRAY_TASK_ID}.fasta

Our script can then be run as before:

.. code:: shell

   $ $ ls
   chr1.fasta chr2.fasta chr3.fasta my_script.sh
   $ sbatch my_script.sh
   Submitted batch job 8504
   $ squeue --me
    JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
   8504_1 standardq my_scrip   zlc187  R       0:02      1 esrumcmpn01fl
   8504_2 standardq my_scrip   zlc187  R       0:02      1 esrumcmpn01fl
   8504_3 standardq my_scrip   zlc187  R       0:02      1 esrumcmpn01fl
   $ ls
   chr1.fasta.gz  chr3.fasta.gz  slurm-8507_1.out  slurm-8507_3.out
   chr2.fasta.gz  my_script.sh   slurm-8507_2.out

An `.out` file is automatically created for each task.

In this example there was a simple one-to-one mapping between the
``SLURM_ARRAY_TASK_ID`` and our data, but that is not always the case.
The `Mapping task ID to data`_ section below describes several ways you
might use to map the ``SLURM_ARRAY_TASK_ID`` variable to more complex
data/filenames.

Dependencies
============

Mapping task ID to data
=======================

Using ``sbatch`` arrays requires that you map a number (the array task
ID) to a file or similar. The above example assumed that filenames were
numbered for simplicity, but that is not always the case.

The following therefore describes a few ways in which you can map array
task ID to more complicated data in a bash script.

#. Using numbered filenames:

.. code:: bash

   # Simple numbering (sample1.vcf, sample2.vcf, etc.)
   FILENAME="/path/to/data/sample${SLURM_ARRAY_TASK_ID}.vcf"
   # Formatted numbering (sample01.vcf, sample02.vcf, etc.)
   FILENAME=$(printf "/path/to/data/sample%02i.vcf" ${SLURM_ARRAY_TASK_ID})

2. Using a table of filenames:

   Given a text file ``my_samples.txt`` containing one filename per
   line:

   +------------------------------------+
   | /path/to/fist_sample.vcf           |
   +------------------------------------+
   | /path/to/second_sample.vcf         |
   +------------------------------------+
   | /path/to/third_sample.vcf          |
   +------------------------------------+

.. code:: bash

   # Prints the Nth line
   FILENAME=$(sed "${SLURM_ARRAY_TASK_ID}q;d" my_samples.txt)

3. Using a table of numbered samples (``my_samples.tsv``):

   +----+--------+------------------------------+
   | ID | Name   | Path                         |
   +----+--------+------------------------------+
   | 1  | first  | /path/to/fist_sample.vcf     |
   +----+--------+------------------------------+
   | 2  | second | /path/to/second_sample.vcf   |
   +----+--------+------------------------------+
   | 3  | third  | /path/to/third_sample.vcf    |
   +----+--------+------------------------------+

.. code:: bash

   # Find row where 1. column matches SLURM_ARRAY_TASK_ID and print 3. column
   FILENAME=$(awk -v ID=${SLURM_ARRAY_TASK_ID} '$1 == ID {print $3; exit}')

****************************
 ``sbatch`` template script
****************************

The following is a simple template for use with the ``sbatch`` command.
This script can also be downloaded :download:`here <my_sbatch.sh>`.

.. literalinclude:: my_sbatch.sh
   :language: sh

**********************
 Additional resources
**********************

-  Slurm `documentation <https://slurm.schedmd.com/overview.html>`_
-  Slurm `summary <https://slurm.schedmd.com/pdfs/summary.pdf>`_ (PDF)
-  The `sbatch manual page <https://slurm.schedmd.com/sbatch.html>`_
-  The `squeue manual page <https://slurm.schedmd.com/squeue.html>`_
