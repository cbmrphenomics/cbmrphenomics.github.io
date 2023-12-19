:orphan:

.. _p_transfers:

#################################
 Transferring data to/from Esrum
#################################

This section describes how to bulk transfer data between Esrum, your PC,
and services such as SIF/Erda and Computerome.

.. _s_transferring_within_cbmr:

************************************
 Transferring data from within CBMR
************************************

Users on a wired connection within CBMR or using the VPN can transfer
files to/from their PCs using any of the standard tools that connect via
SSH, including but not limited to ``scp``, ``sftp``, and ``rsync``.
Windows users may also consider graphical tools such as FileZilla_ or
MobaXterm (see the :ref:`p_usage_connecting` page).

.. _s_transferring_outside_cbmr:

*************************************
 Transferring data from outside CBMR
*************************************

If using the VPN is an option, then see the
:ref:`s_transferring_within_cbmr` section above.

When outside CBMR and using the VPN is not feasible, one may instead use
the SSH/SFTP server at ``sftp.ku.dk``. Official documentation provided
is provided on the `UCPH computing/HPC Systems`_ pages on KUNet.

Briefly

.. code-block:: shell

   $ sftp sftp://abc123@sftp.ku.dk
   (abc123@sftp.ku.dk) Enter password
   Password: ******
   (abc123@sftp.ku.dk) Enter one-time password
   Enter one-time password: ******
   Connected to sftp.ku.dk.
   sftp> ls
   ucph
   sftp> cd ucph/
   sftp> ls
   datasets  hdir      ndir      projects

.. _p_tranfers_sifanderda:

.. _p_transfers_computerome:

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
available on the cluster (Lynx_):

.. code:: shell

   lynx -accept_all_cookies "https://sif.ku.dk"

#. Use the up/down arrow keys to select the ``log in`` link under ``I'm
   already signed up to SIF`` and press Enter:
#. Press enter to confirm that you wish to try login:
#. Enter your KU username and password. Use ``Tab`` to jump to the next
   field and ``Shift+Tab`` to jump to the next field:
#. Use ``Tab`` to select the TODO button and press Enter
#. Enter the SIF two-factor code, press tab to select the ``Submit``
   button, and press enter

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

***************************************
 Transferring data to/from Computerome
***************************************

*****************
 Troubleshooting
*****************

.. _filezilla: https://filezilla-project.org/

.. _ucph computing/hpc systems: https://kunet.ku.dk/work-areas/research/Research%20Infrastructure/research-it/ucph-computing-hpc-systems/Pages/default.aspx
