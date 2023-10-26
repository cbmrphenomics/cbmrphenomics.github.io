.. _page_running:

##########################
 Running jobs using Slurm
##########################

In order to run jobs on the Esrum cluster, you must connect to the head
node and queue them using the Slurm_ job management system. Slurm_ takes
care of automatically queuing and distribute jobs on the compute and GPU
nodes when the required resources are available.

This section describes how to run basic jobs using the ``srun`` command,
how to start an interactive shell on a compute node, and how to reserve
the resources needed for your tasks.

If you need to run a number of similar jobs in parallel, for example
genotyping a set of samples or mapping FASTQ files to a reference
genome, then the ``sbatch`` command can be used to automatically queue
multiple jobs. See the :ref:`page_batch_jobs` for more information.

.. warning::

   Resource intensive jobs *must* be run using Slurm_. Tasks running on
   the head node *will* be terminated without prior warning, in order to
   prevent any impact on other users of the cluster.

******************************
 Running commands using Slurm
******************************

The ``srun`` command is used to queue and execute commands on the
compute nodes, and for most part it should feel no different than
running a command without Slurm_. Simply prefix your command with
``srun`` and the queuing system takes care of running it on the first
available compute node:

.. code::

   $ srun gzip chr20.fasta

.. image:: images/srun_minimal.gif
   :class: gif

Except for the ``srun`` prefix, this is exactly as if you ran the
``gzip`` command on the head node. However, if you need to pipe output
to a file or to another command, then you *must* wrap your commands in a
bash (or similar) script. The script can then be run using ``srun``:

.. code::

   $ srun bash my_script.sh

.. image:: images/srun_wrapped.gif
   :class: gif

By default task are allocated one CPU and 15 GB of RAM. If you need to
use additional resources, then see `Reserving resources for your jobs`_
and `Reserving the GPU node`_ below.

*****************
 Cancelling jobs
*****************

To cancel a job running with srun, simply press `Ctrl + c` twice:

.. code:: shell

   $ srun gzip chr20.fasta
   <ctrl+c> srun: interrupt (one more within 1 sec to abort)
   srun: StepId=8717.0 task 0: running
   <ctrl+c> srun: sending Ctrl-C to StepId=8717.0
   srun: Job step aborted: Waiting up to 32 seconds for job step to finish.

See also the :ref:`managing_jobs` section on the :ref:`page_batch_jobs`
page.

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
test computationally expensive tools or scripts. However, note that you
*cannot* start jobs using Slurm in an interactive shell; jobs can only
be started from the head node.

Once you are done, be sure to exit the interactive shell by using the
``exit`` command or pressing ``Ctrl+D``, so that the resources reserved
for your shell is made available to other users!

.. _reserving_resources:

***********************************
 Reserving resources for your jobs
***********************************

By default a ``srun`` will reserve 1 CPU and just under 15 GB of ram per
CPU. Should your job require more CPUs, then you can request them using
the ``-c`` or ``--cpus-per-task`` options. The following runs a task
with 8 CPUs, and is automatically assigned 8 * 15 ~= 120 gigabytes of
RAM:

.. code::

   $ srun -c 8 -- my-command --threads 8

The amount of RAM allocated by default should be sufficient for most
tasks, but when needed you can request additional RAM using the
``--mem`` or ``--mem-per-cpu`` options. The following runs a task with 8
CPUs and 512 gigabytes of RAM:

.. code::

   $ srun -c 8 --mem 512G -- my-command --threads 8

As described in the :ref:`page_overview`, each node has 128 CPUs
available and 2 TB of RAM, of which 1993 GB can be reserved by Slurm.

The GPU node has 4 TB of RAM available, of which 3920 GB can be reserved
by Slurm, and may be used for jobs that have very high memory
requirements. However, since we only have one GPU node we ask that you
use the regular nodes unless your jobs actually require that much RAM.
See the next section for how to use the GPU node with or without
reserving a GPU.

.. note::

   Remember that reserving CPUs only makes them available to your jobs,
   it does not automatically make use of them! Check the documentation
   for the software you are using to determine how to tell the software
   to use additional threads (corresponding to the ``--threads 8``
   arguments in the above example).

Best practice for reserving resources
=====================================

Determining how many CPUs and how much memory you need to reserve for
your jobs can be difficult.

Few programs benefit from using a lot of threads (CPUs) used due to
added overhead and due to limits to how much of a given process can be
parallelized. Maximum throughput is also often limited by how fast the
software can read/write data. In some cases too many threads can even
increase the amount of time it takes to run the software, sometimes
drastically so!

We therefore recommended that you

   -  Always refer to the documentation and recommendations for the
      specific software you are using!

   -  Test the effect of the number of threads you are using before
      starting a lot of jobs.

   -  Start with fewer CPUs and increase it only when there is a benefit
      to doing so. You can for example start with 2, 4, or 8 CPUs per
      task, and only increasing the number after it has been determined
      that the software benefits from it.

The ``/usr/bin/time -f "CPU = %P, MEM = %MKB"`` command can be used to
estimate the efficiency from using multiple threads and to show how much
memory a program used:

.. code:: console

   $ /usr/bin/time -f "CPU = %P, MEM = %M" my-command --threads 1 ...
   CPU = 99%, MEM = 840563KB
   $ /usr/bin/time -f "CPU = %P, MEM = %M" my-command --threads 4 ...
   CPU = 345%, MEM = 892341KB

In this example increasing the number of threads/CPUs to 4 did not
result in a 4x increase in CPU usage, but only a 3.5x increase. And this
difference tends to increase the more threads are used.

Because performance does not grow linearly with the number of threads it
is often more efficient to split your job into multiple sub-jobs (for
example one job per chromosome) rather than increasing the number of
threads used for the individual jobs. See the :ref:`page_batch_jobs`
page for more information.

Increasing the number of threads only increased slightly the amount of
memory used (820MB to 871MB) in this example. In other words this
software probably did not load additional data per thread, however that
may be the case for other software.

Reserving the GPU node
======================

This section describes how to schedule a task on the GPU node. The GPU
node is intended for tasks that need to use GPUs and for tasks that have
very high memory requirements (more than 2 TB).

To schedule a task on the GPU node you need to select the GPU queue and
(optionally) specify the number of Nvidia A100 GPUs needed (1 or 2). For
example, the following command queues the command ``my-gpu-command`` and
requests a single A100 GPU:

.. code::

   $ srun --partition=gpuqueue --gres=gpu:a100:1 -- my-gpu-command

Alternatively you may reserve both GPUs:

.. code::

   $ srun --partition=gpuqueue --gres=gpu:a100:2 -- my-gpu-command

If you on not need to use a GPU, then you can omit the ``--gres``
option:

.. code::

   $ srun --partition=gpuqueue -- my-command

As above you must also specify your CPU and RAM requirements using
``--cpus-per-task`` and ``--mem``.

Monitoring GPU utilization
==========================

   .. warning::

      Due to changes to SLURM settings, to ensure that jobs cannot
      access resources that were not reserved for them, it is currently
      not possible to monitor GPUs usage from a different job using the
      instructions below. The documentation will be updates shortly.

Slurm does not provide any means of monitoring the actual GPU
utilization, but tools such as ``nvidia-smi`` can be used to monitor
performance metrics. And since we are not going to actually *use* the
GPU, we can simply omit the ``--gres`` option.

.. warning::

   If you need to make use of GPU resources (passive monitoring
   excluded), then you *must* also specify the appropriate ``--gres``
   option. Failure to do so will result in your jobs being terminated!

This allows slurm to run the monitoring task even when the GPUs are
reserved:

.. code::

   $ srun --partition=gpuqueue -- nvidia-smi -l 5
   Thu Jun  8 12:18:15 2023
   +-----------------------------------------------------------------------------+
   | NVIDIA-SMI 525.60.13    Driver Version: 525.60.13    CUDA Version: 12.0     |
   |-------------------------------+----------------------+----------------------+
   | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
   | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
   |                               |                      |               MIG M. |
   |===============================+======================+======================|
   |   0  NVIDIA A100 80G...  On   | 00000000:27:00.0 Off |                    0 |
   | N/A   43C    P0    47W / 300W |      0MiB / 81920MiB |      0%      Default |
   |                               |                      |             Disabled |
   +-------------------------------+----------------------+----------------------+
   |   1  NVIDIA A100 80G...  On   | 00000000:A3:00.0 Off |                    0 |
   | N/A   43C    P0    45W / 300W |      0MiB / 81920MiB |      0%      Default |
   |                               |                      |             Disabled |
   +-------------------------------+----------------------+----------------------+

   +-----------------------------------------------------------------------------+
   | Processes:                                                                  |
   |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
   |        ID   ID                                                   Usage      |
   |=============================================================================|
   |  No running processes found                                                 |
   +-----------------------------------------------------------------------------+

The ``gpustat`` tool provides a more convenient overview but must be
installed via ``pip``:

..
   TODO: Update when gpustats has been added as a module

.. code::

   $ pip install gpustat
   $ srun --partition=gpuqueue --pty -- gpustat -i 5
   esrumgpun01fl.unicph.domain  Thu Jun  8 12:20:24 2023  525.60.13
   [0] NVIDIA A100 80GB PCIe | 43°C,   0 % |     0 / 81920 MB |
   [1] NVIDIA A100 80GB PCIe | 43°C,   0 % |     0 / 81920 MB |

The ``--pty`` option is used in order to support colored, full-screen
output despite not running an interactive actual shell. As an
alternative, you can also start an interactive shell on the GPU node and
run ``gpustats`` or ``nvidia-smi`` that way:

.. code::

   $ srun --partition=gpuqueue --pty -- /bin/bash
   $ gpustat -i 5

*****************
 Troubleshooting
*****************

Error: Requested node configuration is not available
====================================================

If you request too many CPUs (more than 128), or too much RAM (more than
1993 GB for compute nodes and more than 3920 GB for the GPU node), then
Slurm will report that the request cannot be satisfied:

.. code:: shell

   # More than 128 CPUs requested
   $ srun --cpus-per-task 200 -- echo "Hello world!"
   srun: error: CPU count per node can not be satisfied
   srun: error: Unable to allocate resources: Requested node configuration is not available

   # More than 1993 GB RAM requested on compute node
   $ srun --mem 2000G -- echo "Hello world!"
   srun: error: Memory specification can not be satisfied
   srun: error: Unable to allocate resources: Requested node configuration is not available

To solve this, simply reduce the number of CPUs and/or the amount of RAM
requested to fit within the limits described above. If your task does
require more than 1993 GB of RAM, then you also need to add the
``--partition=gpuqueue``, so that your task gets scheduled on the GPU
node.

Additionally, you may receive this message if you request GPUs without
specifying the correct queue or if you request too many GPUs:

.. code:: shell

   # --partition=gpuqueue not specified
   $ srun --gres=gpu:a100:2 -- echo "Hello world!"
   srun: error: Unable to allocate resources: Requested node configuration is not available

   # More than 2 GPUs requested
   $ srun --partition=gpuqueue --gres=gpu:a100:3 -- echo "Hello world!"
   srun: error: Unable to allocate resources: Requested node configuration is not available

To solve this error, simply avoid requesting more than 2 GPUs, and
remember to include the ``--partition=gpuqueue`` option.

**********************
 Additional resources
**********************

-  Slurm `documentation <https://slurm.schedmd.com/overview.html>`_
-  Slurm `summary <https://slurm.schedmd.com/pdfs/summary.pdf>`_ (PDF)
-  The ``srun`` `manual page <https://slurm.schedmd.com/srun.html>`_

.. _slurm: https://slurm.schedmd.com/overview.html

.. _tmux: https://github.com/tmux/tmux/wiki
