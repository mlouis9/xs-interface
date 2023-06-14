Read and Write Cross Sections
=============================

This Notebook demonestrates how to read cross sections from a serpent
``_res.m`` file, and write these cross sections using a template file.

Case Description
----------------

The ``.\inputs`` directory includes: - ``bwr_rho1_2gr`` a serpent input
file. This is a 3D BWR assembly divided into 36 layers (i.e., universes
1,2,…,36) of fuel surrounded by a bottom (universe 54) and upper layers
(universe 55) of reflectors. - ``bwr_rho1_2gr_res.m`` a serpent results
file with all the cross sections. - ``univs`` a file that describes how
to read ``bwr_rho1_2gr_res.m`` - ``template_dyn3d_2g`` is a template
file that specifies how cross sections should be printed out. -
``controlDict`` the main files that is required by the ``xsInterface``.

The ``.\outputs`` directory will include all the files with printed
cross sections.

Required imports
~~~~~~~~~~~~~~~~

.. code:: ipython3

    from xsInterface.functions.main import Main

.. code:: ipython3

    inputFile = ".\\inputs\\controlDict"

Read the cross sections
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    # Reset the main object
    xs = Main(inputFile)


.. parsed-literal::

    ... Reading control dict ...
    <.\inputs\controlDict>
    
    

Read xs data without populating the templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    # readTemplate allows to read and populate data using the templates
    xs.Read(readUniverses=True, readTemplate=True)


.. parsed-literal::

    SERPENT Serpent 2.1.32 found in .\inputs\bwr_rho1_2gr_res.m, but version 2.1.31 is defined in settings
      Attemping to read anyway. Please report strange behaviors/failures to developers.
    

.. parsed-literal::

    ... Reading universe <u> ...
    ... Reading coe/_res.m file for hisotry <nom> ...
    

Write to output files
~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    xs.Write()


.. parsed-literal::

    
    
    ... Writing cross sections ...
    
    
    

All the files should be written to the ``.\outputs`` directory

