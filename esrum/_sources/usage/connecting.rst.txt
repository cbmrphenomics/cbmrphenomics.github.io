.. _connecting:

###########################
 Connecting to the cluster
###########################

If you have not already applied for and been granted access to the
cluster, then please see the :ref:`page_applying_for_access` page before
continuing.

The cluster's is accessible via SSH at ``esrumhead01fl.unicph.domain``.
This is the Esrum "head" node, which serves as the entry-point for the
cluster and which gives you access to the job management system used for
running software (see :ref:`page_running`)

To connect to the cluster you will typically need to be connected to the
KU VPN. For information about connecting to the VPN, see the support
pages on KUNet in Danish_ and English_.

***********************
 Connecting on Windows
***********************

Windows users will need to install a SSH client in order to be able to
connect to the server. Options include MobaXterm_, Putty_, and Windows
Subsystem for Linux (WSL_), and much more. The following demonstrates
how to setup MobaXterm. Please refer to the `Connecting On Linux or
OSX`_ section if using WSL_.

.. _configure_mobaxterm:

Configuring MobaXterm
=====================

#. Install and open MobaXterm.

#. Click left-most ``Session`` button on the toolbar.

   .. image:: images/mobaxterm_01.png
      :align: center

#. Click on the left-most ``SSH`` button on the resulting ``Session
   settings`` dialog

   .. image:: images/mobaxterm_02.png
      :align: center

#. Under ``Basic SSH settings``

   #. Write ``esrumhead01fl.unicph.domain`` under ``Remote Host``
   #. Click the checkbox next to ``Specify username`` and enter your KU
      username (in the form ``abc123``)

   .. image:: images/mobaxterm_03.png
      :align: center

#. Click on the ``Bookmark settings`` tab and

   #. Write ``Esrum`` or a name you prefer under ``Session Name``

   #. Optionally click the ``Create a desktop shortcut to this session``
      button. This will create a shortcut on your desktop that connects
      to Esrum.

   .. image:: images/mobaxterm_04.png
      :align: center

#. Click OK and you should connect to the server. The first time you
   connect a new server you if you want to proceed. As this is the first
   time we are connecting to Esrum, simply press Accept:

   .. image:: images/mobaxterm_05.png
      :align: center

   .. warning::

      If you receive this question again later, then stop and
      double-check that you are connected via the KU VPN, as the message
      could indicate that you are not actually connecting to Esrum!

#. You should now be able to login to the server:

   .. image:: images/mobaxterm_06.png
      :align: center

#. For security reasons we recommend that you decline if asked if you
   want to save your password.

To connect again another time, either use the desktop shortcut (if you
created it), double click on ``Esrum`` in the list of sessions on the
left side of MobaXterm, or select ``Esrum`` from the list that appears
when clicking on the middle ``Sessions`` button on the main menu.

   .. image:: images/mobaxterm_07.png
      :align: center

.. _connecting_linux:

****************************
 Connecting on Linux or OSX
****************************

Linux and OSX users can connect to the cluster using the following
terminal command, replacing ``abc123`` with your KU username:

.. code::

   $ ssh abc123@esrumhead01fl.unicph.domain

.. image:: images/connecting_ssh.gif
   :class: gif

It is recommended to add an entry for the cluster to your
``.ssh/config`` file, replacing ``abc123`` with your KU username:

.. code::

   $ cat ~/.ssh/config
   Host esrum esrumhead01fl esrumhead01fl.unicph.domain
       HostName esrumhead01fl.unicph.domain
       User abc123

This allows you connect to the server using the names ``esrum``,
``esrumhead01fl``, or ``esrumhead01fl.unicph.domain``, and without
having to specify your username:

.. code::

   $ ssh esrum
   abc123@esrumhead01fl.unicph.domain's password:
        __
       /  \
      _\__/  Welcome to esrumhead01fl
     (_)     University of Copenhagen
   _____O______________________________________
   Supported by UNICPH IT  it.ku.dk/english


   Last login: Fri Oct 13 01:35:00 1980 from 127.0.0.1
   $

.. note::

   Note that the cluster *does not* support authentication through a
   public SSH key and that you therefore have to enter your password
   when connecting to the server.

*****************
 Troubleshooting
*****************

If have not already been granted access to the server, then please see
the :ref:`page_applying_for_access` page before continuing!

Timeout while connecting to the cluster
=======================================

You may experience timeout errors when you attempt to connect to the
server:

.. image:: images/connecting_ssh_timeout.gif
   :class: gif

#. Firstly verify that you are correctly connected to the KU network:

   #. You must either use a wired connection while physically at CBMR.
   #. Or you must connect via the KU VPN.

   It is not possible to connect to using WIFI at CBMR nor is it
   possible to from outside of CBMR without the use of the VPN. See the
   official VPN documentation in Danish_ or English_ for more
   information.

#. If neither using a wired connection nor connecting the the KU VPN
   fixes the problem, you may need to create a support ticket to have KU
   IT permit you to connect to the server.

   #. Login to the KU `IT Serviceportal`_.

   #. Click the ``Create Ticket`` button.

   #. Select the ``Research IT`` category.

   #. Then select the ``Research Applications and Services``
      subcategory.

   #. Finally, select ``Consultancy and Support``.

   #. Write something like "SSH connection times out when attempting to
      connect to esrumhead01fl.unicph.domain" in the "Please describe"
      text-box and describe the steps you have taken to try to fix this
      problem: Tried wired connection at CBMR, tried VPN, etc.

   #. Write "esrumhead01fl.unicph.domain" in the System name text-box.

   #. Click the ``Add to cart`` button.

   #. Click the ``SUBMIT ORDER`` button.

.. _danish: https://kunet.ku.dk/medarbejderguide/Sider/It/Fjernadgang-vpn.aspx

.. _english: https://kunet.ku.dk/employee-guide/Pages/IT/Remote-access.aspx

.. _it serviceportal: https://serviceportal.ku.dk/

.. _mobaxterm: https://mobaxterm.mobatek.net/

.. _putty: https://www.putty.org/

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
