.. _page_overview:

##########
 Overview
##########

The Esrum cluster is a cluster managed by the `Phenomics Platform`_ at
CBMR_. Technical support and administration is handled by KU-IT.

**************
 Architecture
**************

The cluster consists of a head node, 8 compute nodes, and 1 GPU node:

+---+---------+------+-------------------------+---------------------+
|   | Node    | RAM  | CPUs                    | GPUs                |
+===+=========+======+=========================+=====================+
| 1 | Head    | 2 TB | 2x24 core AMD EPYC 7413 |                     |
+---+---------+------+-------------------------+---------------------+
| 8 | Compute | 2 TB | 2x32 core AMD EPYC 7543 |                     |
+---+---------+------+-------------------------+---------------------+
| 1 | GPU     | 4 TB | 2x32 core AMD EPYC 75F3 | 2x NVIDIA A100 80GB |
+---+---------+------+-------------------------+---------------------+

Users connect to the "head" node, from which jobs can be submitted to
the individual nodes. In addition, a server for running container
instances, an RStudio_ web server, and a Shiny_ server are available.

The nodes runs Red Hat Enterprise Linux 8, use the Slurm_ management
system for running tasks, and use `environment modules`_ for managing
software.

**************************
 Projects and data-shares
**************************

Access is managed on a per-project level, and is administrated by
individual project owners, with each project folder containing a
standard set of sub-folders (``apps``, ``data``, ``people``,
``scratch``).

Datasets used by several projects may made available via read-only
network shares. As with projects, access is administered by the data
owner.

****************************
 Backup policies and quotas
****************************

Your ``/home`` and the ``apps``. ``data``, and ``people`` folders in
each projects are automatically backed up. The ``scratch`` folders are
NOT backed up. The specific frequency and duration of backups differ for
each type of folder and may also differ for individual projects.

As a rule folders for projects involving GDPR protected data (indicated
by the project name ending with ``-AUDIT``) is subject to more frequent
backups. However, on-site backups are kept for a shorter time to prevent
the unauthorized recovery of intentionally deleted data.

**********************
 Additional resources
**********************

   -  Official `UPCH computing/HPC Systems`_ documentation on KUNet.

.. _cbmr: https://cbmr.ku.dk/

.. _environment modules: https://modules.readthedocs.io/en/latest/

.. _phenomics platform: https://cbmr.ku.dk/research-facilities/phenomics/

.. _rstudio: https://posit.co/products/open-source/rstudio/

.. _shiny: https://shiny.rstudio.com/

.. _slurm: https://slurm.schedmd.com/

.. _upch computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/upch-computing-hpc-systems/Pages/default.aspx
