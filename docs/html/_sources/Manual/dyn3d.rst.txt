.. _dyn3d:


DYN3D operations
----------------- 

This class allows to use the ``xsInterface`` object with all the stored cross sections and built-in methods 
together with the Nodal Diffusion code - DYN3D.

To initialize the object the following command is used:

.. code::

	reslt = DYN3D(xs, casedir, casefile, exefile)


where,
	- ``xs`` is the ``xsInterface`` ``Main`` object (see :ref:`codeexe`).
	- ``casedir`` [str] full (relative or absolute) directory where the _kin file (for DYN3D) is located
	- ``casefile`` [str] name of the DYN3D case file (i.e., the string prefix before _kin)
	- ``exefile`` [str] name of the file that contains the execution command. This file will be an executable file. On Windows this will be a Batch File. The file will contain the following execution line.

	.. code::
	
		<DYN3D_VERSION>.exe .\<casefile name> .\<casefile name>

e.g., 

	.. code::
	
		DYN3DMG.exe .\bwr .\bwr
 

**Example**

.. code::

	casedir = ".\\dyn3d"   # dyn3d dir
	casefile = "bwr"  # name of dyn3d file
	exefile = "RUN_DYN3D" # dyn3d executuin file
	
	reslt = DYN3D(xs, casedir, casefile, exefile) 


**Remarks**

Before reseting this object, the user is required to generate the data that will be used by objected by using the :ref:`p_poplatedata`.

In the example below all the attributes defined by the user will be used to populate all the channels and layers defined in the problem.
The ``states`` is a dictonary describing at what states cross sections are to be extracted for. Finally, two new variables are defined, i.e., ``sph`` and ``adf``. Both of which are defined as unity values for all the channels, layers and energy groups.  

.. code:: 
	
	xs.PopulateCoreData(attributes=None,
	                    states=states, 
	                    volManip={'infflx': 'divide'},
	                    sph=None, adf=None)

//////////////////////////////////////////////////////////////////





Class Methods
--------------


========================= ============================================
Method							   		 Description
========================= ============================================
:ref:`d_exe`			        A single DYN3D execution.
------------------------- --------------------------------------------
:ref:`d_iterate`	        Iterate on specific inputs via non-linear solution scheme.
------------------------- --------------------------------------------
:ref:`d_plotfluxes`	      dddd.
========================= ============================================



.. _d_exe:

==========
Execution
==========


**A single DYN3D execution that includes reading and storing flux and keff values**.

**Syntax**

.. code::

	reslt.Execute()
	
	
	
.. _d_iterate:

=========
Iterate
=========	

**terative method to calculate correction factors required to match the predicted flux solution with the reference one.**
The governing method for the non-linear solution relies on the JFNK, which includes two main subroutines:

(1) Iterative Arnoldi procedure to determine the required variation of dx for : Fx*dx = b
(2) Newton-Krylov (outer iterations on the variation in x): xk = x0 + s*dx

**Syntax**

.. code::

	reslt.Iterate(corrattrs, refFlx, newtonIters, krylovSpan, krylovErr, 
	newtonErr, dampingF, pert, lbound, ubound, attrObj, groupWeights, sphMultp, sphDiv)
	
where,
	- ``corrattrs`` [list of strs] name/s of the iterative attributes to be iterated for correction.
	- ``refFlx`` [3-dim list] reference flux solution for all the channels, layers, energy groups. Default is None. In which case the results will be obtained from the results on the xs object. The order/structure has to follow ``refFlx[channel][layer][group]``
	- ``newtonIters`` [int] number of Newton iterates. This is the limit but if the precision set by ``newtonErr`` is achieved the iterations are stopped.
	- ``krylovSpan`` [int] number of Krylov iterates/vectors, must be >= 1. This is the limit but if the precision set by ``krylovErr`` is achieved the iterations are stopped.
	- ``krylovErr`` [float] tolerance for stopping the iterations on Krylov. Default is 5E-03. Lower number leads to more Krylov vectors created and higher computational overheads.
	- ``newtonErr`` [float] tolerance for stopping Newton iterations. Default is 1E-05. Lower number leads to more Newton iterations executed and thus higher computational overheads.
	- ``dampingF`` [float] a damping factor between 0 and 1. It can also be a string equal to ``RM`` standing for Robbins Monro variable weighting factor (1/N). The RM factor can slow the convergence but in principle ensures convergence. 
	- ``attrObj`` : [str] objective attribute used to multiply the flux to create a reaction rate objective function.
	- ``pert`` : [float] a fraction that represents the perturbation that is required to be applied for x for each vector of the Krylov space.  
	- ``lbound`` : [float] lower bound to limit the variation of correction factors during Newton iterations.
	- ``ubound`` : [float] upper bound to limit the variation of correction factors during Newton iterations.   
	- ``groupWeights``: [list] energy group-wise weighting factors for the objective function. These are normalization factors used only when SPH normalization is used.  
	- ``sphMultp``: [list] attributes that will be multiplied by the iterated SPH factors. Default is None. These attributes must be explicitly defined and exist otherwise an error will be thrown.    
	- ``sphDiv``: [list] attributes that will be divided by the iterated SPH factors. Default is None. These attributes must be explicitly defined and exist otherwise an error will be thrown.   

**Note**:
If ``corrattrs`` contains the preserved word 'sph' then all the printed cross sections will be multipled by the superhumanization (SPHs) factors.
So far, there is no normalization of the SPH factors.

**Example**

.. code::

	reslt.Iterate(corrattrs=['adf], refFlx=refFlx, newtonIters=10, krylovSpan=10, groupWeights=None, dampingF=0.5, lbound=0.70, ubound=1.3, pert=1E-03, newtonErr=0.001)

Please note that all the correction attributes defined for ``corrattrs`` must exist. You can define new attributes using the ``PopulateCoreData`` method.

**Example**

.. code::

	reslt.Iterate(corrattrs=['sph], refFlx=refFlx, newtonIters=10, krylovSpan=10, groupWeights=None, dampingF=0.5, lbound=0.70, ubound=1.3, pert=1E-03, newtonErr=0.001,
	sphMultp=['infTranspxs', 'trcTranspxs', 'infrabsxs', 'infnsf', 'fissjoule', 'infsp0'], sphDiv=None)


.. _d_plotfluxes:

===========
PlotFluxes
===========	

**plot the fluxes and difference in fluxes for the different newton iterations**

**Syntax**

.. code::

	reslt.PlotFluxes(xvalues, iters,  
                   chId, layers, egroup, refFlag, flip, xlabel, ylabel,
                   norm, fontsize, markers, markerfill, markersize)

where,
	- ``iters`` [array]. iteration indices. If None, the 0th and last iterations will be plotted.
	- ``xvalues`` [array 1-d] x-axis values, e.g., heights in cm.
	- ``chId`` [str] identification string of the channel. Only a single channel is allowed.
	- ``layers`` [array 1-d]. layers indices  to be included in the plot. If None all the layers included. 
	- ``egroup`` [int]. energy group integer. Default is 0 (i.e., Fast group).
	- ``refFlag``	[bool]. flag to indicate if the reference flux to be included in the plot.
	- ``flip`` [bool]. boolean flag to indicate whether results should be axially flipped.
	- ``xlabel`` [str] x-axis label with a default ``Axial height, meters``. 
	- ``ylabel`` [str] y-axis label with a default ``Normalized flux``.
	- ``fontsize`` [float] font size value.
	- ``markers`` [str os list of str] markers type/s. 
	- ``markerfill`` [bool] True if the marking filling to be excluded and False otherwise.
	- ``markersize`` [float] size of the marker with a default of 8.						


**Example**

.. code::

	reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
               		 chId="S1", layers=None, egroup=0)


**Remark**

Following a successful execution of the ``Iterate`` method, the user can also plot the channels results using :ref:`p_channelsplot` using the ``xs`` object as results will be added to it.

e.g.,  

.. code::

	xs.ChannelsPlot('infflx', zmid, ylabel='Flux', xlabel='Height, cm', markers='ro',
	                layers=np.linspace(1,30,30, dtype=int), markerfill=True)


//////////////////////////////////////////////////////////////////

==============================
Complete application examples
==============================

1. :ref:`dyn3d_example1`: Complete example of the iterative technique applied to find axial discontinuity factors for the 3D single fuel assembly case.
2. Full core to be completed.