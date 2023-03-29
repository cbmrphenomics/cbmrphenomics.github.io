##########################
 Running jobs using Slurm
##########################

The Esrum cluster makes use of the Slurm_ job management system in order
to queue and distribute jobs on the available nodes. This section
describes how to start an interactive shell on a compute node, how run
basic jobs, and how to reserve the needed resources for your work.

It is strongly recommended that you make use of tmux_ or a similar tool
when running tasks, in order to ensure that your work is not interrupted
if you lose connection to the server or need to turn off your PC. See
the :ref:`tmux` page for a short tutorial.

.. warning::

   Resource intensive jobs *must* be run using the queuing system. Your
   tasks *will* be terminated without prior warning if you fail to do
   so, in order to prevent any impact on other users of the cluster.

.. warning::

   Show consideration towards other users of the cluster. If you need to
   run very intensive jobs then please contact Phenomics first so that
   we can ensure that the cluster will still be usable by other users
   while your jobs are running. Failure to do so will result in your
   jobs being terminated without prior warning.

******************************
 Running an interactive shell
******************************

If you need to run analyses in using an interactive process, for example
an R shell, then you can start a remote shell

.. code::

   [abc123@esrumhead01fl ~] $ srun --pty
   [abc123@esrumcmpn07fl ~] $

Note that the hostname displayed changes from `esrumhead01fl` to
`esrumcmpn07fl`, where `esrumcmpn07fl` is one of the eight Esrum compute
nodes.

You can now run interactive jobs, for example running an R shell or
testing computationally expensive tools or scripts. Once you are done,
exit the interactive shell by using the `exit` command or pressing
`Ctrl+D`.

Be sure to exit the interactive session once you are done working, so
that the resources reserved for your shell is made available to other
users.

***********************************
 Reserving resources for your jobs
***********************************

By default a `srun` will reserve 1 CPU (2 threads) and TODO GB of ram
per CPU. Should your job require more resources, you may request those
using the `-c` or `--cpus-per-task` options, and the

.. warning::

   If you

****************
 Reserving GPUs
****************

.. _slurm: https://slurm.schedmd.com/overview.html
