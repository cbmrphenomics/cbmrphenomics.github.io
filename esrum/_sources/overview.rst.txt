.. _overview_page:

##########
 Overview
##########

The Esrum cluster is a cluster managed by the Phenomics group at CBMR.
The server runs Red Hat Enterprise Linux 8, uses the SLURM_ management
system for running tasks, and `environment modules`_ for managing
software.

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

In addition, a server for running container instances, an RStudio_ web
server, and a Shiny_ server are available.

.. _environment modules: https://modules.readthedocs.io/en/latest/

.. _rstudio: https://posit.co/products/open-source/rstudio/

.. _shiny: https://shiny.rstudio.com/

.. _slurm: https://slurm.schedmd.com/
