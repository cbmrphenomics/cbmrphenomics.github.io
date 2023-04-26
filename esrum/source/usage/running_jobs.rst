.. _page_running:

##########################
 Running jobs using Slurm
##########################

The Esrum cluster makes use of the Slurm_ job management system in order
to queue and distribute jobs on the compute and GPU nodes. This section
describes how to how to run basic jobs, how to start an interactive
shell on a compute node, and how to reserve the needed resources for
your tasks.

It is strongly recommended that you run tmux_ or a similar tool before
starting tasks using ``srun``, in order to ensure that your work is not
interrupted if you lose connection to the server or need to turn off
your PC. See the :ref:`tmux_page` page for a short tutorial.

.. warning::

   Resource intensive jobs *must* be run using Slurm. Your tasks *will*
   be terminated without prior warning if you fail to do so, in order to
   prevent any impact on other users of the cluster.

.. warning::

   Show consideration towards other users of the cluster. If you need to
   run very intensive jobs then please :ref:`page_contact` Phenomics
   first so that we can ensure that the cluster will still be usable by
   other users while your jobs are running. Failure to do so may result
   in your jobs being terminated without prior warning.

******************************
 Running commands using Slurm
******************************

The ``srun`` command is used to queue and execute commands on the
compute nodes, and for most part it should feel no different than
running a command on the head node. Simply prefix your command with
``srun`` and the queuing system takes care of running it on the first
available compute node:

.. code::

   srun gzip chr20.fasta

.. image:: images/srun_minimal.gif
   :class: gif

Except for the ``srun`` prefix, this is exactly as if you ran the
``gzip`` command on the head node. However, if you need to pipe output
to a file or to another command, then you *must* wrap your commands in a
bash (or similar) script. The script can then be run using ``srun``:

.. code::

   srun bash my_script.sh

.. image:: images/srun_wrapped.gif
   :class: gif

For tips to make your bash scripts more robust, see the :ref:`page_bash`
page.

By default task are allocated one CPU and 15 GB of RAM. If you need to
use additional resources, then see `Reserving resources for your jobs`_
and `Reserving GPUs`_ below.

******************************
 Running an interactive shell
******************************

If you need to run an interactive process, for example if you need to
use an interactive R shell to process a large dataset, or if you just
need to experiment with running an computationally heavy process, then
you can start a shell on one of the compute nodes as follows:

.. code::

   [abc123@esrumhead01fl ~] $ srun --pty -- /bin/bash
   [abc123@esrumcmpn07fl ~] $

Note that the hostname displayed changes from ``esrumhead01fl`` to
``esrumcmpn07fl``, where ``esrumcmpn07fl`` is one of the eight Esrum
compute nodes.

You can now run interactive jobs, for example running an R shell, or
test computationally expensive tools or scripts. Once you are done, exit
the interactive shell by using the ``exit`` command or pressing
``Ctrl+D``.

Be sure to exit the interactive session once you are done working, so
that the resources reserved for your shell is made available to other
users!

***********************************
 Reserving resources for your jobs
***********************************

By default a ``srun`` will reserve 1 CPU (2 threads) and 8 GB of ram per
CPU. Should your job require more CPUs or RAM, then you can request CPUs
using the ``-c`` or ``--cpus-per-task`` options, and request RAM using
the ``--mem`` or ``--mem-per-cpu`` options. Values given to ``--mem``
are assumed to be in megabytes by default, but this may be overridden by
using an explicit unit (M for megabyte, G for gigabyte, T for terabyte):

.. code::

   # Run a task with 8 CPUs and 64 gigabytes of memory
   srun -c 8 --mem 64G -- my-command

.. warning::

   If you

****************
 Reserving GPUs
****************

To reserve GPU resources, you need to select the GPU queue and
(optionally) specify the number of Nvidia A100 GPUs (1 or 2) needed. The
following command queues command ``${COMMAND}`` and requests a single
A100 GPU:

.. code::

   srun --partition=gpuqueue --gres=gpu:a100:1 -- ${COMMAND}

.. _slurm: https://slurm.schedmd.com/overview.html

.. _tmux: https://github.com/tmux/tmux/wiki
