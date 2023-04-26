#################
 Do's and don'ts
#################

In general

-  GDPR protected data *must* be stored in audited project folders.
   These can be recognized by the `AUDIT` suffix, for example
   `/projects/denmark-AUDIT`.

-  Do not place data or custom scripts in your home folder. Your home
   folder is accessible only to you, unless you provide a written
   permission to KU IT. See :ref:`section_home` for more information.

-  Do not run big jobs on the head node (`esrumhead01fl`). Small jobs
   are allowed (a couple of cores at most and modest memory usage), but
   larger jobs *will* be terminated without warning. See the
   :ref:`page_batch_jobs` page for how to run your tasks on the cluster.

-  Be considerate of other users who also need to run their analyses and
   please talk to us if you have a lot of jobs to run, need to use a lot
   of computational resources, and so on. See also the
   :ref:`page_running` page.

The following may make your use of the Esrum cluster easier:

-  Use tmux_ for running persistent shells on the cluster. See the
   :ref:`tmux_page` page for more information.
-  If using `ssh` directly, then setup an alias for connecting to Esrum.
   See TODO page for more information.

.. _tmux: https://github.com/tmux/tmux/wiki
