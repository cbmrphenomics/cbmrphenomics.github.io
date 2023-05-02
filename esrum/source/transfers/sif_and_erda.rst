########################################
 Transferring data to/from SIF and ERDA
########################################

The following describes how to bulk transfer data from the Esrum cluster
to SIF_ (Sensitive Information Facility) or ERDA_ (Electronic Research
Data Archive) and vice versa. For small amounts of data, it may be
easier to use the web interfaces provided by the SIF_ and ERDA_
websites.

***************************
 Two Factor Authentication
***************************

Connecting to the SIF_ or ERDA_ servers requires that the user has
successfully authenticated using Two Factor Authentication. Futhermore,
this must be done using the same IP from which the user intends to
connect, in this case from the Esrum IP.

This poses some challenges, as running a full-fledged browser over SSH
performs extremely poorly. This section therefore describes how to
authenticate to SIF_ or ERDA_ using a purely text-based browser
available on the cluster (Lynx_).

******************************
 Transferring data using lftp
******************************

*******************************
 Transferring data using sshfs
*******************************

.. note::

   The following assumes that you have successfully authenticated as
   described in `Two Factor Authentication`_.

.. warning::

   Note that sshfs *cannot* be used in project folders. See below for
   more information.

SSHFS makes it possible to mount folders over SSH and access those as
were normal filesystems (with some limitations). This is useful if you
wish to explore the content of a SIF_ or ERDA_ project,

.. warning::

   Note that sshfs *cannot* be used in project folders. Attempting to
   mount a folder under ``/projects`` using sshfs will result in a
   broken mount-point that cannot be removed. You must therefore only
   create mount-points in your home folder!

.. _erda: https://erda.ku.dk/

.. _lynx: https://en.wikipedia.org/wiki/Lynx_(web_browser)

.. _sif: https://sif.ku.dk/
