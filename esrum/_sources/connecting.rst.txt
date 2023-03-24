###########################
 Connecting to the Cluster
###########################

************************************
 Applying for access to the cluster
************************************

An `official guide`_ is available here.

#. Visit identity.ku.dk_.

#. Click on the ``Manage My Access`` button or the ``Manage User
   Access`` button. Which of the two buttons you'll see depends on your
   existing roles.

   #. If you clicked on the ``Manage user Access`` button, first search
      for your KU username (e.g. ``abc123``) and then click on the check
      mark to the left of the search result *once*. Wait for the check
      mark to turn green and then click the ``Next`` button.

#. Search for ``SRV-esrumhead-users``.

#. Click *once* on the check mark to the left of ``SRV-esrumhead-users``
   in the resulting list. Wait for the check mark to turn green and then
   click the ``Next`` button.

#. Verify that you are applying for access to ``SRV-esrumhead-users``
   and then click the ``Submit`` button.

#. Wait for your request to be processed.

You will receive an email that ``Changes to your Identity were
processed`` once you have been granted access, but note that it may take
longer before your account is ready for use.

***************************
 Connecting to the cluster
***************************

The cluster is accessible via SSH at ``esrumhead01fl.unicph.domain``. To
connect to the cluster you will typically need to connect to the KU VPN.

For Windows users
=================

Windows users will need to install a SSH client in order to be able to
connect to the server. Options include MobaXterm_, Putty_, and Windows
Subsystem for Linux (WSL_), and many more. The following demonstrates
how to setup MobaXterm. Please refer to the `For Linux users`_ section
if using WSL_.

Configuration MobaXterm
-----------------------

For Linux users
===============

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

.. _identity.ku.dk: https://identity.ku.dk/

.. _mobaxterm: https://mobaxterm.mobatek.net/

.. _official guide: https://kunet.ku.dk/medarbejderguide/ITvejl/KU%20IdM%20-%20S%C3%A5dan%20anmodes%20om%20funktionsrolle.pdf

.. _putty: https://www.putty.org/

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about
