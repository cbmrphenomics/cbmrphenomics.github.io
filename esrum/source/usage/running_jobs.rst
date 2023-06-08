.. _page_running:

##########################
 Running jobs using Slurm
##########################

In order to run jobs on the Esrum cluster, you must connect to the head
node and queue them using the Slurm_ job management system. Slurm_ takes
care of automatically queuing and distribute jobs on the compute and GPU
nodes when the required resources are available.

This section describes how to run basic jobs, how to start an
interactive shell on a compute node, and how to reserve the resources
needed for your tasks.

If you need to run a number of similar jobs in parallel, for example
genotyping a set of samples or mapping FASTQ files to a reference
genome, then the ``sbatch`` can be used to automatically queue multiple
jobs. See the :ref:`page_batch_jobs` for more information.

.. warning::

   Resource intensive jobs *must* be run using Slurm_. Tasks running on
   the head node *will* be terminated without prior warning, in order to
   prevent any impact on other users of the cluster.

.. warning::

   Show consideration towards other users of the cluster. If you need to
   run very intensive jobs then please :ref:`page_contact` Phenomics
   first so that we can help ensure that the cluster will still be
   usable by other users while your jobs are running. Failure to do so
   may result in your jobs being terminated without prior warning.

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

For tips to make your bash scripts more robust, see the :ref:`page_bash`
page.

By default task are allocated one CPU and 15 GB of RAM. If you need to
use additional resources, then see `Reserving resources for your jobs`_
and `Reserving the GPU node`_ below.

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

***********************************
 Reserving resources for your jobs
***********************************

By default a ``srun`` will reserve 1 CPU and just under 15 GB of ram per
CPU. Should your job require more CPUs, then you can request them using
the ``-c`` or ``--cpus-per-task`` options. The following runs a task
with 8 CPUs and 8 * 15 = 120 gigabytes of RAM:

.. code::

   $ srun -c 8 -- my-command

The amount of RAM allocated by default should be sufficient for most
tasks, but when needed you can request additional RAM using the
``--mem`` or ``--mem-per-cpu`` options. The following runs a task with 8
CPUs and 512 gigabytes of RAM:

.. code::

   $ srun -c 8 --mem 512G -- my-command

As described in the :ref:`page_overview`, each node has 128 CPUs
available and 2048 GB of RAM, of which about 1993 GB can be reserved in
total.

The GPU node has 4096 GB of RAM, of which 3920 is reservable, but since
we only have one GPU node we ask that you use the regular nodes unless
your analyses actually requires that much RAM at once. See the next
section for how to use the GPU node with or without reserving a GPU.

Reserving the GPU node
======================

This section describes how to schedule a task on the GPU node. The GPU
node is intended for tasks that need to use GPUs and for tasks that have
very high memory requirements (more than 2 TB).

To schedule a task on the GPU node you need to select the GPU queue and
(optionally) specify the number of Nvidia A100 GPUs (1 or 2) needed. The
following command queues command ``my-gpu-command`` and requests a
single A100 GPU:

.. code::

   $ srun --partition=gpuqueue --gres=gpu:a100:1 -- my-gpu-command

Alternatively you may reserve both CPUs:

.. code::

   $ srun --partition=gpuqueue --gres=gpu:a100:2 -- my-gpu-command

If you on not need to use a GPU, then you can omit the `--gres` option:

.. code::

   $ srun --partition=gpuqueue -- my-command

As above you must also specify your CPU and RAM requirements using

.. warning::

   If you need to make use of GPU resources (monitoring excluded), then
   you *must* also specify the appropriate `--gres` option. Failure to
   do so will result in your jobs being terminated!

Slurm does not provide any means of monitoring the actual GPU usage, but
tool such as `nvidia-smi` can be used to monitor performance metrics.
Since we are not going to actually *use* the GPU, we can simply omit the
`--gres` option. This allows slurm to run the task even when the GPUs
are reserved.

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

The `gpustat` tool provides a more convenient overview but must be
installed via `pip`:

.. code::

   $ pip install gpustat
   $ srun --partition=gpuqueue --pty -- gpustat -i 5
   esrumgpun01fl.unicph.domain  Thu Jun  8 12:20:24 2023  525.60.13
   [0] NVIDIA A100 80GB PCIe | 43°C,   0 % |     0 / 81920 MB |
   [1] NVIDIA A100 80GB PCIe | 43°C,   0 % |     0 / 81920 MB |

The `--pty` option is used in order to support colored, full-screen
output despite not running an interactive actual shell.

As an alternative, you can also start an interactive shell on the GPU
node:

   $ srun --partition=gpuqueue --pty -- /bin/bash

**********************
 Additional resources
**********************

-  The ``srun`` `manual page <https://slurm.schedmd.com/srun.html>`_

.. _slurm: https://slurm.schedmd.com/overview.html

.. _tmux: https://github.com/tmux/tmux/wiki
