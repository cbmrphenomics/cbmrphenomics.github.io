############
 Guidelines
############

The following describes the general guidelines for using the Esrum
cluster.

Failure to follow these guidelines may result in your tasks being
terminated and may even result in your access to the cluster being
revoked.

****************
 Basic security
****************

-  Never leave your PC/laptop unsecured while logged onto the cluster.
   In general, you should *never* leave your PC/laptop unsecured. Your
   PC/laptop *must* be locked or turned off whenever you leave it.

-  Your account is strictly personal and must not be shared.

**************
 Data storage
**************

-  GDPR protected data *must* be stored in audited folders. These can be
   recognized by the `-AUDIT` suffix, for example `/projects/name-AUDIT`
   or `/datasets/name-AUDIT`.

-  Directory names and file names *must not* contain GDPR protected data
   or other confidential information, even if placed in an audited
   folder. This is because common operations expose this information to
   *all* users of the cluster. For the same reason, *do not* include
   such information in command-line arguments.

-  Data *must not* be copied out of audited `/datasets` or `/projects`
   folders without permission from the relevant data controller. Instead
   use symbolic links if you need the data to be located in a more
   convenient location.

-  Data must not leave the cluster without permission from the relevant
   data controllers.

-  Do not place data or custom scripts in your home folder. Your home
   folder is accessible only to you, unless you provide a written
   permission to KU IT.

See :ref:`filesystem_page` for more information.

***************
 Running tasks
***************

-  Do not run big jobs on the head node (`esrumhead01fl`), as doing so
   may impact the ability of everyone to run jobs. However, we do permit
   small jobs on the head node, meaning a few cores *in total* and
   modest memory usage.

-  Do not use more resources than those you have reserved for your jobs:
   If you need N cores/threads, if you need more RAM than default, or if
   need to use GPUs, then you must reserve those resources via Slurm.

-  Remember to be considerate to other users. For example, limit the
   number of jobs you are running simultaneously,so that others users
   can also run their jobs

-  Please close interactive shells and the like that you are not
   actively using. Resources that you have reserved are not made
   available for other users until your tasks have finished.

See the :ref:`page_running` page for more information about how to run
your tasks on the cluster.
