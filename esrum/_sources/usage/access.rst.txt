.. _applying_for_access:

#####################
 Applying for access
#####################

The following describes how to apply for access to the Esrum cluster and
related related services, projects, and datasets. An official guide to
the identity system used is available here_.

************************************
 Applying for access to the servers
************************************

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

Once you have been granted access you will receive an email that
``Changes to your Identity were processed``.

.. warning::

   Please note that your account may not be ready by the time you
   receive the email described above. In that case, logging in will
   result in a warning that your home folder does not exist. If so, then
   simply wait a few hours before trying again.

Once you have been granted access and your account is ready, you may
refer to the :ref:`connecting` page for instructions on how to connect
to the cluster.

.. _applying_for_projects:

*************************************
 Applying for access to the projects
*************************************

You can apply for access to projects using the same method as described
in `Applying for access to the servers`_. Alternatively, the project
owner(s) can add you to projects directly. However, the Phenomics group
cannot add you to projects owned by a third party.

See :ref:`section_projects` for a description of the location and
file-structure of projects on Esrum.

*********************************************
 Applying for access to the datasets/cohorts
*********************************************

.. warning::

   Transfer of data to the new servers has not yet been completed. You
   can still apply for access to cohorts, but you may not be granted
   access until everything is ready.

You can find an up-to-date of datasets and cohorts in the N-drive at

.. code::

   N:/path/to/TODO.xlsx

In order to apply for access to a dataset, simply follow the steps
described in the `Applying for access to the servers`_ section and
substitute ``SRV-esrumhead-users`` with the name of your project.

.. note::

   Access to datasets managed by the Phenomics group requires permission
   from the data-manager responsible for that data. The Phenomics group
   will verify that you are permitted to access the data. You may speed
   up this process by having the data manager :ref:`page_contact` us in
   advance.

.. _here: https://kunet.ku.dk/medarbejderguide/ITvejl/KU%20IdM%20-%20S%C3%A5dan%20anmodes%20om%20funktionsrolle.pdf

.. _identity.ku.dk: https://identity.ku.dk/

.. _wsl: https://learn.microsoft.com/en-us/windows/wsl/about

