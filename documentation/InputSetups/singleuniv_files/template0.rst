.. _single_template0:

Template 0
----------

This template shows how every state point can be obtained individually. 

The first part (i.e., ``"vari"{times=[0, 0.5, 1]} ...``) defines lists/arrays (using "vari") that represent the various states considered in this case. 

Please note that nested "rep" blocks used here represent nested ``for`` blocks. The analogous pprogramming language:

.. code::
	
	for idxH in (range(len(history)):
		for idxB in (range(len(times)):
			for idxF in (range(len(fuel)):
				for idxM in (range(len(mod)):
					for idxC in (range(len(cool)):
						Do something ...

In this example, we make the use of "varo" to assess different input variables, such as time at specific state points.
For example, ``"varo"{times[idxB]<3.3f>}`` will assess the value of the ``times`` vector for different ``idxB`` values that change as we apply the  ``"vari"{idxB=idxB+1}`` coomand.

Plesae note that we directly specify the format at which the output variable should be printed with (i.e., ``<3.3f>``), but in principle the default format of any output variable is defined in the control deck file (and in our case is ``d``).
There might be a conflict created between the data values type and format used to output the data, e.g. attempt to print string values using float format. In such a case, an error is expected to be raised, and the user will need to change the format type accordingly.

The evaluation of data is handled here through the "values" card. 
In this example, the values are assessed using dynamic values for the ``fuel``, ``mod``, ``cool``, ``time``, ``history``; where ``time`` and ``history`` are preserved keywords.
The ``[]`` capability allows to obtain group-wise values. The term ``group`` is arbitrary chosen here and refers to the number of components defining the basic parameter, e.g. ``group`` for ``macro`` types' variables refers to the energy group, and for ``kinetics`` types' variables it refers to the delayed neutron group.

The following parameters are used in this example:

- ``inf_nsf`` with 2 energy groups
- ``inf_sp0`` with 2-by-2 matrix-like structure
- ``sig_f`` with 3-by-2 matrix (3 indicates the number of isotopes, and 2 the number of energy groups).

Using this template, the ``values`` capability will be iterated (over the history, times, and branches) using the "rep" rules to output energy bins-wise values. The corresponding output file can be found in :ref:`single_output0`.


.. code::

	# ===================================================================================================================================================
	    Each energy group value is written separately for every perturbation state
	    2 histories / 3 time points / 2 fuel temp. / 2 mod. dens. / 2 coolant temp. / 2 energy groups
	# ===================================================================================================================================================
	
	"vari"{times=[0, 0.5, 1]}
	"vari"{fuel=[900, 1200]}
	"vari"{mod=[650, 700]}
	"vari"{cool=[550, 600]}
	"vari"{history=["nom", "pert"]}
	"vari"{isotopes=[531350, 541350, 922350]}
	
	"vari"{idxH=0}
	"rep"{2
	"vari"{idxB=0}
	"rep"{{3
	"vari"{idxF=0}
	"rep"{{{2
	"vari"{idxM=0}
	"rep"{{{{2	
	 "vari"{idxC=0}
	"rep"{{{{{2
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	  History = "varo"{history[idxH]<s>}, Time = "varo"{times[idxB]<3.3f>}, Fuel T. = "varo"{fuel[idxF]<3.3f>}, Mod. T. = "varo"{mod[idxM]<3.3f>}, Cool. T. = "varo"{cool[idxC]<3.3f>} 
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	INF_NSF
	"vari"{idxE=-1}
	"rep"{{{{{{2
	"vari"{idxE=idxE+1}
	  Group "varo"{idxE}
	  "values"{inf_nsf, fuel="varo"{fuel[idxF]<3.1f>}, mod="varo"{mod[idxM]<3.1f>}, cool="varo"{cool[idxC]<3.1f>}, time="varo"{times[idxB]<3.3f>}, history="varo"{history[idxH]<s>}  ["varo"{idxE}]} 
	"rep"}}}}}}
	
	INF_SP0
	"vari"{idxE0=-1}
	"rep"{{{{{{2
	"vari"{idxE0=idxE0+1}
	"vari"{idxE1=-1}
	"rep"{{{{{{{2
	"vari"{idxE1=idxE1+1}
	  Group "varo"{idxE0} --> Group "varo"{idxE1}
	  "values"{inf_sp0, fuel="varo"{fuel[idxF]<3.1f>}, mod="varo"{mod[idxM]<3.1f>}, cool="varo"{cool[idxC]<3.1f>}, time="varo"{times[idxB]<3.3f>}, history="varo"{history[idxH]<s>}  ["varo"{idxE0}, "varo"{idxE1}]} 
	"rep"}}}}}}}
	"rep"}}}}}}
	
	Microscopic Fission 
	"vari"{idxS=-1}
	"rep"{{{{{{3
	"vari"{idxS=idxS+1}
	Isotope "varo"{isotopes[idxS]}
	"vari"{idxE=-1}
	"rep"{{{{{{{2
	"vari"{idxE=idxE+1}
	  Group "varo"{idxE}
	  "values"{sig_f, fuel="varo"{fuel[idxF]<3.1f>}, mod="varo"{mod[idxM]<3.1f>}, cool="varo"{cool[idxC]<3.1f>}, time="varo"{times[idxB]<3.3f>}, history="varo"{history[idxH]<s>}  ["varo"{idxS}, "varo"{idxE}]} 
	"rep"}}}}}}}
	"rep"}}}}}}
	
	"vari"{idxC=idxC+1}
	"rep"}}}}}
	"vari"{idxM=idxM+1}
	"rep"}}}}
	"vari"{idxF=idxF+1}
	"rep"}}}
	"vari"{idxB=idxB+1}
	"rep"}}
	"vari"{idxH=idxH+1}
	"rep"}
