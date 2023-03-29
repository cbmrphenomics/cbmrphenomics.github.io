###########################
 Connecting to the cluster
###########################

The cluster is accessible via SSH at ``esrumhead01fl.unicph.domain``. To
connect to the cluster you will typically need to be connected to the KU
VPN.

.. warning::

   TODO: Link to KU VPN documentation and/or add tips section

*******************
 For Windows users
*******************

Windows users will need to install a SSH client in order to be able to
connect to the server. Options include MobaXterm_, Putty_, and Windows
Subsystem for Linux (WSL_), and many more. The following demonstrates
how to setup MobaXterm. Please refer to the `For Linux users`_ section
if using WSL_.

.. warning::

   TODO: Write instructions for MobaXterm
      #. Where to get it
      #. Setting up a server profile
      #. Add downloadable session file?
      #. Basic usage

Configuring MobaXterm
=====================

*****************
 For Linux users
*****************

Linux users can connect to the cluster using the following command,
replacing ``abc123`` with your KU username:

.. code::

   $ ssh abc123@esrumhead01fl.unicph.domain

It is recommended to add an entry for the cluster to your
``.ssh/config`` file:

.. code::

   $ cat ~/.ssh/config
   Host esrum esrumhead01fl.unicph.domain
       HostName esrumhead01fl.unicph.domain
       User abc123

This allows you connect to the server using the abbreviated name
``esrum`` and without having to specify your username:

.. code::

   $ ssh esrum

.. note::

   Note that the cluster *does not* support authentication through a
   public SSH key and that you have to enter your password when
   connecting to the server.

.. _mobaxterm: https://mobaxterm.mobatek.net/

.. _putty: https://www.putty.org/

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
