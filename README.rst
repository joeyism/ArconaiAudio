
ArconaiAudio
============

Allows you to listen to Arconai through your terminal

Installation
------------

.. code-block:: bash

   pip3 install --user ArconaiAudio

Dependencies
------------

You need to install `mpv <https://mpv.io/installation/>`_ as well

Ubuntu
^^^^^^

.. code-block:: bash

   sudo add-apt-repository ppa:mc3man/mpv-tests
   sudo apt-get install mpv

OS X
^^^^

.. code-block:: bash

   brew install mpv --with-bundle

Usage
-----

In your terminal, run

.. code-block:: bash

   ArconaiAudio

and you will see a selection


.. image:: docs/images/Screenshot_2019-03-16_18-04-54.png
   :target: docs/images/Screenshot_2019-03-16_18-04-54.png
   :alt: selecting show type


After selection a show type, the relevant show names will be displayed. In the input menu, you can type in the show you want to listen to. Word completion is automatically enabled, so pressing ``TAB`` will help selection. Selection through ``UP`` or ``DOWN`` arrow keys also works.


.. image:: docs/images/Screenshot_2019-03-16_18-04-04.png
   :target: docs/images/Screenshot_2019-03-16_18-04-04.png
   :alt: selecting show name


**NOTE**\ : Show names are case sensitive

Options
^^^^^^^

.. code-block:: bash

   ArconaiAudio [show type] [show name]

Show Type
~~~~~~~~~


* shows
* cable
* movies

Show Name
~~~~~~~~~

The name of the show under the specific **Show Type**. The name is case sensitive, and for names with spaces in the title, you should put quotes around it.

Example
^^^^^^^

Running

.. code-block:: bash

   ArconaiAudio shows Scrubs

will play the **Scrubs** audio

.. code-block:: bash

   ArconaiAudio shows "Always Sunny in Philadelphia"

will play the **Always Sunny in Philadelphia** audio
