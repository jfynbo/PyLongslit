Identify
========

In this step, we manually identify the lines in the arc spectrum. 
This is done by in an interactive plotting window/GUI. 

**This step is by far the most time-consuming for the user, as 
a fair amount of user work is needed.**

To run this script, you will need the `arcsub.fits` file from the 
:ref:`pre-processing <pre_processing>` step. You will also need a 
list with the arc lines for your specific setup. This list should
be called `mylines_vac.dat` or `ThAr_linelist.dat` and should be 
located in the `database` directory. For this tutorial, we provide the
list for the HeNe lamp used. As one will need a referrence spectrum 
to manually identify the lines, these also need to be aquired. 
For this tutorial, we provide the such reference spectra for the
HeNe lamp used with the g04 grating for ALFOSC in 4 PDF files in the 
`database` directory.

Therefore, the relevant files and directories for this step are:

.. code-block:: bash

    ├── arcsub.fits
    ├── database
    │   ├── map-g04-he-1.pdf
    │   ├── map-g04-he-2.pdf
    │   ├── map-g04-ne-1.pdf
    │   ├── map-g04-ne-2.pdf
    │   └── mylines_vac.dat
    ├── identify.py

In the following, we provide a step-by-step guide on how to execute
the line identification:

1. **Run the script**: 
   In the same directory as the `identify.py` script, run:

    .. code-block:: bash
    
        python3 identify.py

    When the script is excecuted, a GUI/interactive plot window will open.
    You have to manually load the arc spectrum by clicking on the `Load Spectrum`
    button, and finding the `arcsub.fits` file. This will also load the 
    pre-existing line list `mylines_vac.dat` into the GUI. Your window should
    look something like this:

    .. image:: pictures/id_post_loading.png
       :width: 600
       :align: center

2. **Identifying the lines**: 
   In this step, you have to use the reference spectra provided in the `databse`
   directory (or downloaded elswhere for your own setup) to identify the
   wavelentghs of the lines in the arc spectrum. This is done by clicking on the
   `Add Line` button, and then clicking on the arc spectrum where you think a line
   is, and then manually typing in the wavelength of the line. Example for a small
   Helium portion of the spectrum, with a zoom in of the corresponding reference 
   spectrum (here there is a small offset between the reference spectrum and the
   line list - we have used the linelist, since it is in vacuum):

    .. image:: pictures/id_post_first.png
       :width: 600
       :align: center

    .. image:: pictures/id_post_first_ref.png
       :width: 600
       :align: center

   ..............................
