.. _connecting:

###########################
 Connecting to the cluster
###########################

If you have not already applied for and been granted access to the
cluster, then please see the :ref:`applying_for_access` page.

The cluster is accessible via SSH at ``esrumhead01fl.unicph.domain``. To
connect to the cluster you will typically need to be connected to the KU
VPN.

For information about connecting to the VPN, see the support pages on
KUNet in `Danish
<https://kunet.ku.dk/medarbejderguide/Sider/It/Fjernadgang-vpn.aspx>`_
and `English
<https://kunet.ku.dk/employee-guide/Pages/IT/Remote-access.aspx>`_.

*******************
 For Windows users
*******************

Windows users will need to install a SSH client in order to be able to
connect to the server. Options include MobaXterm_, Putty_, and Windows
Subsystem for Linux (WSL_), and many more. The following demonstrates
how to setup MobaXterm. Please refer to the `For Linux and OSX users`_
section if using WSL_.

Configuring MobaXterm
=====================

#. Install and open MobaXterm.

#. Click left-most ``Session`` button on the toolbar.

#. Click on the left-most ``SSH`` button on the resulting ``Session
   settings`` dialog

#. Under ``Basic SSH settings``

   #. Write ``esrumhead01fl.unicph.domain`` under ``Remote Host``
   #. Click the checkbox next to ``Specify username`` and enter your KU
      username (in the form ``abc123``)

#. Click on the ``Bookmark settings`` tab and

#. Write ``Esrum`` or a name you prefer under ``Session Name``

#. Optionally click the ``Create a desktop shortcut to this session``
   button. This will create a shortcut on your desktop that connects to
   Esrum.

#. Click OK and you should connect to the server. Note that this will
   likely fail if you are not connected to the KU VPN.

To connect again another time, either use the desktop shortcut (if you
created it), double click on ``Esrum`` in the list of sessions on the
left side of MobaXterm, or select ``Esrum`` from the list that appears
when clicking on the middle ``Sessions`` button on the main menu.

*************************
 For Linux and OSX users
*************************

Linux and OSX users can connect to the cluster using the following
terminal command, replacing ``abc123`` with your KU username:

.. code::

   $ ssh abc123@esrumhead01fl.unicph.domain

It is recommended to add an entry for the cluster to your
``.ssh/config`` file, replacing ``abc123`` with your KU username:

.. code::

   $ cat ~/.ssh/config
   Host esrum esrumhead01fl.unicph.domain
       HostName esrumhead01fl.unicph.domain
       User abc123

This allows you connect to the server using the abbreviated name
``esrum`` and without having to specify your username:

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

.. _mobaxterm: https://mobaxterm.mobatek.net/

.. _putty: https://www.putty.org/

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
