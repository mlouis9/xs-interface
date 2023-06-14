Iterative procedure with DYN3D
==============================

This Notebook demonestrates how to calculate correction factors (i.e.,
axial ADFs in this case) using the built-in JFNK procedure within the
``xsInterface`` package.

First, cross sections are read from a serpent ``_res.m`` file. This
notebook shows how to execute DYN3D iteratively using the ``Iterate``
method.

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

The ``.\dyn3d`` includes a pre-generated DYN3D case. The ``.\dyn3d\xs``
directory will include all the files with printed cross sections
required by DYN3D.

Required imports
~~~~~~~~~~~~~~~~

.. code:: ipython3

    from xsInterface.functions.main import Main

.. code:: ipython3

    # a class required to execute DYN3D
    from xsInterface.functions.dyn3d import DYN3D

.. code:: ipython3

    # plotting capability
    from xsInterface.functions.plotters import Plot1d

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
    xs.Read(readUniverses=True)


.. parsed-literal::

    SERPENT Serpent 2.1.32 found in .\inputs\bwr_rho1_2gr_res.m, but version 2.1.31 is defined in settings
      Attemping to read anyway. Please report strange behaviors/failures to developers.
    

.. parsed-literal::

    ... Reading universe <u> ...
    ... Reading coe/_res.m file for hisotry <nom> ...
    

Populate cross sections
~~~~~~~~~~~~~~~~~~~~~~~

In the ``".\\inputs\\controlDict"`` the user defined the core map used
to populate the cross sections according to their channels and layers
positions.

In our problem we have 1 channel and 38 axial layers.

**Define states** These states must exist and be used to obtain the
cross sections for different channels and layers.

.. code:: ipython3

    nchs, nlayers = 1, 38
    states = {
    'history':[['nom']*nlayers]*nchs, 'time': [[0.0]*nlayers]*nchs, 'dens': [[700.]*nlayers]*nchs,}

**Populate core data** built-in capability to populate the data
according to the defined map including defining new variables not listed
in the original ``univs`` file. This is a **mandaory** step if the
intent is to execute DYN3D.

.. code:: ipython3

    volmanip = {'infflx': 'divide'}
    xs.PopulateCoreData(
                        states=states, 
                        attributes=None,  # specify only if specific attrs needed
                        volManip=volmanip,
                        adf=None, topadf=None, bottomadf=None)

Iteratively execute DYN3D
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    casedir = ".\\dyn3d"   # dyn3d dir
    casefile = "bwr"  # name of dyn3d file
    exefile = "RUN_DYN3D" # dyn3d executuin file
    
    # Reset the object
    reslt = DYN3D(xs, casedir, casefile, exefile)

**Set the refernce flux**

.. code:: ipython3

    refFlx, chIds = xs.CoreValues('infflx', volManip=['divide'])
    refFlx = refFlx['infflx']

**Execute**

The files will be written to the specified directories and then
automatically executed.

.. code:: ipython3

    reslt.Iterate(
        corrattrs=['topadf'], refFlx=refFlx, newtonIters=8, krylovSpan=10, 
        dampingF=1.0)


.. parsed-literal::

    ... Iterative JFNK ...
    

Compare results against Serpent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    import numpy as np

The layers are defined as they were used in the actual problem

.. code:: ipython3

    layers = np.linspace(0, 365.76, 37)  #active core
    layers = np.hstack((-20.0, layers, 385.76))  # with reflectors
    zmid = 0.5*(layers[0:-1] + layers[1:])

Built-in plotting capability to plot the reference and DYN3D fluxes

.. code:: ipython3

    reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
                   chId="S1", layers=np.linspace(1, 30, 30, dtype=int), egroup=0, ylabel='Norm. Fast flux')



.. image:: jfnk_dyn3d_files%5Cjfnk_dyn3d_31_0.png



.. image:: jfnk_dyn3d_files%5Cjfnk_dyn3d_31_1.png



.. image:: jfnk_dyn3d_files%5Cjfnk_dyn3d_31_2.png


There is an option to continue the iterations on other parameters.

.. code:: ipython3

    reslt.Iterate(
        corrattrs=['inftranspxs'], refFlx=refFlx, newtonIters=12, krylovSpan=15, 
        dampingF=1.0)


.. parsed-literal::

    ... Iterative JFNK ...
    

.. code:: ipython3

    reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
                   chId="S1", layers=np.linspace(1, 30, 30, dtype=int), egroup=0, ylabel='Norm. Fast flux')



.. image:: jfnk_dyn3d_files%5Cjfnk_dyn3d_34_0.png



.. image:: jfnk_dyn3d_files%5Cjfnk_dyn3d_34_1.png



.. image:: jfnk_dyn3d_files%5Cjfnk_dyn3d_34_2.png


