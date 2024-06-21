Installation
~~~~~~~~~~~~~~

The software is run by executing a series of 
Python scripts. Therefore, the installation consists of these steps:


.. _Download the source code:

1. :ref:`Download the source code <download>`.
2. :ref:`Create a clean Python environment <venv>` (**optional - but strongly recommended**).
3. :ref:`Install the required Python packages <packages>`.

.. _download:

1. Download the source code
===========================

The software can be downloaded from the `GitHub repository website <https://github.com/jfynbo/PyLongslit/>`_ or 
cloned by using git.

**Direct link to download from the repository website:**

`Download Source Code (ZIP) <https://github.com/jfynbo/PyLongslit/archive/refs/heads/main.zip>`_

**Using git:** 

SSH (recommended if you plan on developing)...

.. code-block:: bash

    git clone git@github.com:jfynbo/PyLongslit.git

... or HTTPS (works too, but you will need to enter your username and password on every pull/push):

.. code-block:: bash

    git clone https://github.com/jfynbo/PyLongslit.git


.. _venv:

2. Create a clean Python environment
====================================

To ensure best possible stability of the software and to avoid version conflicts with other Python packages on your system,  
it is **strongly recommended** to create a clean Python environment for running the software.
If you are unfamiliar with Python environments, see :ref:`our quick introduction to
Python environments <envs_quick_into>`. You can skip directly to :ref:`installing the required Python packages <packages>`
if you prefer to not use a clean environment - in that case you might experience
software bugs due to version conflicts that are not accounted for in this documentation.

**Using Anaconda (conda) (recommeded):**

To create a new virtual environment using conda (Anaconda), run the following commands in your terminal:

.. code-block:: bash

    conda create --name PyLongslit python=3.9

You can replace ``PyLongslit`` with any name you like. This will create a new environment with Python 3.9 installed.

To activate the environment, run:

.. code-block:: bash

    conda activate PyLongslit

**Using venv (standard Python):**

To create a new virtual environment using venv (standard Python), run the following commands in your terminal:

.. code-block:: bash

    python3.9 -m venv PyLongslit

You can replace ``PyLongslit`` with any name you like. This will create a new environment with the Python version 3.9 installed.

To activate the environment, run:

.. code-block:: bash

    source PyLongslit/bin/activate
.. _envs_quick_into:

Quick introduction to Python environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python applications often depend on a specific version of Python and a specific set of Python packages.
These packages can have dependencies on other packages, and these dependencies can have dependencies on other packages, and so on.
This can lead to a situation where two applications require different versions of the same package, which can cause conflicts.
By using Python environments, you can create isolated environments where you can install the specific versions of Python and Python 
packages that you need for a specific application. This helps ensure that only the needed packages are installed, and that they do not
conflict with other applications on your system.

Python environments as created with the commands shown above will be empty, and you will need to install the required packages,
as described in :ref:`installing the required Python packages <packages>`.

**Note:** The envirornment will need to be activated every time you open a new terminal.
You can configure your terminal to automatically activate the environment - 
this will not be covered in this documentation - see documentation for your terminal for more information.

In `bash` (Linux/MacOS), prior to activating a specific environment, 
your terminal will start in the `base` environment:

.. code-block:: bash

    (base) user@computer:~$

After activating the environment, the name of the environment will be shown in the terminal prompt:

.. code-block:: bash

    (PyLongslit) user@computer:~$

.. _packages:

1. Install the required Python packages
====================================