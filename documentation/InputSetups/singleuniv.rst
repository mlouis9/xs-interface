.. _singleuniv:

Single Universe
================

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   singleuniv_files//u0.rst
   singleuniv_files//controlDict.rst
   singleuniv_files//template0.rst
   singleuniv_files//template1.rst
   singleuniv_files//template2.rst
   singleuniv_files//output0_u0.rst
   singleuniv_files//output1_u0.rst
   singleuniv_files//output2_u0.rst


Description
-----------

To execute the problem, the user is required to prepare the following files:

1. A single control deck (:ref:`single_controldeck`) file - defining universe and template files to be read.
2. Universe file/s (:ref:`single_u0`) - a single universe file is defined here.
3. Template file/s (:ref:`single_template0`, :ref:`single_template1`, :ref:`single_template2`) - three template files are defined here to demonestrate multiple ways to write the same information.

Each file referenced above provides description of the states, data, and the template used for outputting data.



Application of ``xsInterface``:
-------------------------------


.. code::

    # ---------------------------------------------------------------------
    # Import xsInterface
    # ---------------------------------------------------------------------
    from xsInterface.functions.main import Main

    # ---------------------------------------------------------------------
    # Define the Input Control File
    # ---------------------------------------------------------------------
    inpFile = '.\\controlDict'
    
    # ---------------------------------------------------------------------
    # Read Input File
    # ---------------------------------------------------------------------
    xs = Main(inputFile)  # Read the control dict
    xs.Read()   # Read xs data and templates and populate data
    
    # ---------------------------------------------------------------------
    # Write to output files
    # ---------------------------------------------------------------------
    xs.Write()
    
    # ---------------------------------------------------------------------
    # Basic capablity to obtain results
    # ---------------------------------------------------------------------
    xs.Table("u0", ['inf_nsf'], time=0.0, history='nom', fuel=900, mod=650)
    xs.Values("u0", 'inf_nsf', fuel=900, mod=650, cool=600,time=0.0, history='nom')
    

Outputs generated by ``xsInterface``:
-------------------------------------
    
After executing the ``xs.Write()`` command in the code snippet provided above, the following files are created.

1. :ref:`single_output0` corresponding the template provided in :ref:`single_template0`.
2. :ref:`single_output1` corresponding the template provided in :ref:`single_template1`.
3. :ref:`single_output2` corresponding the template provided in :ref:`single_template2`.
