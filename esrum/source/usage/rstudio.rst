.. _page_rstudio:

###############################
 RStudio and Jupyter Notebooks
###############################

Users of the Esrum cluster have the option of using RStudio or Jupyter
Notebooks to run their analyses. This section describes steps required
to use these tools.

*********
 RStudio
*********

An RStudio_ server is made available at http://esrumweb01fl:8787. To use
this server, you must

#. Be a member of the ``SRV-esrumweb-users`` group. Simply follow the
   steps in the :ref:`applying_for_access` section, and enter the above
   group name.

#. Be connected via the KU VPN or using a wired connection at CBMR. See
   :ref:`connecting` for more information.

Once you have been been made a member of the ``SRV-esrumweb-users`` and
connected using the VPN or a wired connection at CBMR, simply visit
http://esrumweb01fl:8787 and login using your KU credentials.

For your username you should use the short form:

.. image:: images/rstudio_login.png
   :align: center

******************
 Jupyter notebook
******************

`Jupyter Notebooks`_ are available via the module system on Esrum and
may be started as follows:

.. code:: shell

   $ module load jupyter-notebook
   $ jupyter notebook --no-browser --port=XXXXX

.. raw:: html

   <script>
    document.write("The number used in the argument <code class=\"docutils literal notranslate\"><span class=\"pre\">--port=XXXXX</span></code> must be a value in the range 49152 to 65535, and must not be a number used by another user on Esrum. The number shown here was randomly selected for you and you can refresh this page for a different suggestion.")
   </script>
   <noscript>
   The XXXXX in the above command must be replaced with a valid port number. To avoid trouble you should pick a number in the range 49152 to 65535, and you must not pick a number used by another user on Esrum.
   </noscript>

It is also recommended that you run your notebook in a tmux session or
similar, to avoid the notebook shutting down if you lose connection to
the server. See :ref:`tmux_page` for more information.

To actually connect to the notebook server, you will need to setup port
forwarding using the port-number from your command.

Port forwarding in Windows (MobaXterm)
======================================

The following instructions assume that you are using MobaXterm. If not,
then please refer to the documentation for your tool of choice.

#. Install and configure MobaXterm as described in
   :ref:`configure_mobaxterm`.

#. Click the middle ``Tunneling`` button on the toolbar.

   .. image:: images/mobaxterm_tunnel_01.png
      :align: center

#. Click the bottom-left ``New SSH Tunnel`` button.

   .. image:: images/mobaxterm_tunnel_02.png
      :align: center

#. Fill out the tunnel dialogue as indicated, replacing ``12356`` with
   your chosen port number (e.g. XXXXX) and replacing ``abc123`` with
   your KU username. Finally click ``Save``:

   .. image:: images/mobaxterm_tunnel_03.png
      :align: center

#. If the tunnel does not start automatically, press either the "Play"
   button or the ``Start all tunnels`` button:

   .. image:: images/mobaxterm_tunnel_04.png
      :align: center

#. Enter your password and your SSH tunnel should now be active.

Once you have configured MobaXterm and enabled port forwarding, you can
open your notebook via the
``http://localhost:XXXXX/?token=${long_text_here}`` URL that Jupyter
Notebook printed in your terminal.

Port forwarding on Linux/OSX
============================

It is recommended to enable port forwarding using your ``~/.ssh/config``
file. This is accomplished by adding a ``LocalForward`` line to your
entry for Esrum as shown below (see also the section about
:ref:`connecting_linux`):

.. code:: text

   Host esrum esrumhead01fl esrumhead01fl.unicph.domain
       HostName esrumhead01fl.unicph.domain
       User abc123

       LocalForward XXXXX localhost:XXXXX

The command costs of two parts: The port used by the notebook on Esrum
(XXXXX), and the address via which the notebook on Esrum should be
accessible on your PC (localhost:XXXXX).

Alternatively, you can start start/stop port forwarding on demand by
using an explicit SSH command. The ``-N`` option is optional and stops
ssh from starting a shell once it has connected to Esrum:

.. code:: shell

   $ ssh -N -L XXXXX:localhost:XXXXX abc123@esrumhead01fl.unicph.domain

Once you have port forwarding is enabled, you can open your notebook via
the ``http://localhost:XXXXX/?token=${long_text_here}`` URL that Jupyter
Notebook printed in your terminal.

*****************
 Troubleshooting
*****************

RStudio: Incorrect or invalid username/password
===============================================

Please make sure that you are entering your username in the short form
and that you have been added as a member of the ``SRV-esrumweb-users``
group (see above). If the problem persists, please :ref:`page_contact`
us for assistance.

Jupyter Notebooks: Browser error when opening URL
=================================================

Depending on your browser you may receive one of the following errors.
The typical causes are listed, but the exact error message will depend
on your browser. It is therefore helpful to review all possible causes
listed here.

When using Chrome, the cause is typically listed below the line that
says "This site can't be reached".

-  "The connection was reset"

   This typically indicates that Jupyter Notebook isn't running on the
   server, or that it is running on a different port than the one you've
   forwarded. Check that Jupyter Notebook is running and make sure that
   your forwarded ports match those used by Jupyter Notebook on Esrum.

-  "localhost refused to connect" or "Unable to connect"

   This typically indicates that port forwarding isn't active, or that
   you have entered the wrong port number in your browser. Verify that
   port forwarding is active and that you are using the correct port
   number in the ``localhost`` URL.

-  "Check if there is a typo in esrumweb01fl" or "We’re having trouble
   finding that site"

   You are must likely connecting from a network outside of KU. Make
   sure that you are using a wired connection at CBMR and/or that the
   VPN is activated and try again.

Browser: Timeout
================

..
   TODO: messages from chrome/firefox

.. raw:: html

   <script defer>
    var random_port = getEphemeralPort();

    function updatePort(elem) {
      if (elem.childNodes.length) {
        elem.childNodes.forEach(updatePort);
      } else if (elem.textContent) {
        elem.textContent = elem.textContent.replaceAll("XXXXX", random_port);
      }

      if (elem.href && elem.href.includes("XXXXX")) {
        elem.href = elem.href.replaceAll("XXXXX", random_port);
        // open in new page
        elem.target = "_blank";
      }
    };

    document.addEventListener('DOMContentLoaded', function() {
      updatePort(document.body);
    });
   </script>

.. _jupyter notebooks: https://jupyter.org/

.. _rstudio: https://posit.co/products/open-source/rstudio/
