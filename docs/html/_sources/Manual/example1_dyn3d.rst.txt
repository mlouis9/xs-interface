.. _dyn3d_example1:


Example 1: A single 3D fuel assembly
-------------------------------------

The files for this case can be found on:

.. code::

	.\xsInterface\inputsets\inp10_dyn3d_corrections\fuelAssembly3d\2group

A bried walk-through is provided here.
There are 38 universes in total; 2 reflectors (denoted as universes 54 [bottom] and 55[upper]), and 36 active core regions ranging from 1 [bottom] to 36 [upper] regions.

The breakdown of the directories and files are:

1. ``debug_corr_2gr.py`` is the execution file that contains the execution commands and post processing commands.

2. ``inputs`` directory contains:

	1.1. Serpent input file ``bwr_rho1_2gr``. Not used here and provided only for reference.
	
	1.2. Serpent result file ``bwr_rho1_2gr_res.m``.
	
	1.3. ``controlDict`` required to define the main file for the ``xsInterface``, which also includes the maps of all the channels and layers.
	
	1.4. ``univs`` description of the universe cards.

	1.5. ``template_dyn3d_2g`` a template file.

2. ``dyn3d`` directory contains:

	2.1. ``bwr_kin.dat``, ``bwr_thy.dat``, ``bwr_wqs.dat`` files all set up by the user. Please note that in the ``bwr_wqs.dat`` the user must already specify the names of the cross section files.
	
	2.2. ``bwr_lst.dat``, ``bwr_red.dat``, ``bwr_res.dat`` are generated during the runs.
	
	2.3. ``XS`` directory is a directory to which all the cross section files will be written to.
	
Here, we will describe only the main execution .py file	``debug_corr_2gr.py``


Step 1: Read cross section data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

	# Read the control dict
	xs = Main(inputFile=".\\inputs\\controlDict")
	
	# Read xs data only
	xs.Read(readUniverses=True)

	
Step 2: Populate core data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start by defining the states.

.. code::

	nchs = 1
	nlayers = 38
	states = {
	'history':[['nom']*nlayers]*nchs,
	'time': [[0.0]*nlayers]*nchs,
	'dens': [[700.]*nlayers]*nchs,
	}
	
If there is any volume manipulation required specify it:

.. code::

	volmanip = {'infflx': 'divide'}
	
Populate data and define additional attributes:

.. code::

	xs.PopulateCoreData(
	                    states=states, 
	                    attributes=None,  # specify only if specific attrs needed
	                    volManip=volmanip,
	                    adf=None, bottomadf=None, topadf=None, sph=None,)
                    
Step 3: Execute DYN3D iteratively
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

	casedir = ".\\dyn3d"   # dyn3d dir
	casefile = "bwr"  # name of dyn3d file
	exefile = "RUN_DYN3D" # dyn3d executuin file
	
	# Reset correction factors
	reslt = DYN3D(xs, casedir, casefile, exefile)
	reslt.Iterate(
	    corrattrs=['topadf'], refFlx=refFlx, newtonIters=4, krylovSpan=8, 
	    dampingF=1.0)   
	    
Step 4: Process results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   


.. code::

	layers = np.linspace(0, 365.76, 37)  #active core
	layers = np.hstack((-20.0, layers, 385.76))  # with reflectors
	zmid = 0.5*(layers[0:-1] + layers[1:])
	
	
	plt.figure()
	reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
	               chId="S1", layers=None, egroup=0)
	
	plt.figure()
	reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
	               chId="S1", layers=None, egroup=1)
	
	
	xs.ChannelsPlot('infflx', zmid, ylabel='Flux', xlabel='Height, cm', markers='ro',
	                layers=np.linspace(1,30,30, dtype=int), markerfill=True)     