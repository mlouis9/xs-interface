.. _single_template1:

Template 1
----------

This template shows how all the state points (i.e., history, time, and branches) are obtained together. 

The first part (i.e., ``"vari"{times=[0, 0.5, 1]} ...``) defines lists/arrays (using "vari") that represent the various states considered in this case. 

The second part uses nested "rep" blocks to define the order of all the different state points.

The evaluation of data is handled here through the "values" card. 

In this example, the "values" are assessed without specifying directly the values for the ``fuel``, ``mod``, ``cool``, ``time``, ``history``.
However, the different attributes (e.g., ``inf_nsf``) already contain all the value points corresponding to all the states defined earlier.

Therefore, when ``"values"{inf_nsf,  ["varo"{idxE}]}`` is used, the end result is a vector of values for the specific energy group (corresponding to ``idxE``).
The default ordering of data follows the ``history``, ``time``, and the order at which branches are provided in the ``states`` card when the universe is defined.
In our case, the order follows:

.. code::

	for idxH in (range(len(history)):
		for idxB in (range(len(times)):
			for idxF in (range(len(fuel)):
				for idxM in (range(len(mod)):
					for idxC in (range(len(cool)):
						Do something ...



Using this template, the ``values`` capability will be printed in a matrix-form for each energy bin. The corresponding output file can be found in :ref:`single_output1`.



.. code::


	# ===================================================================================================================================================
	    Each energy group value is written separately but all the states are printed together in a matrix form.
	    
	    The default order of states is: history, time/burnup, the order at which the branches were provided in the universe file.
	    Here, the order of the states is as follows: coolant temp., mod. temp., fuel temp., times, histories
	# ===================================================================================================================================================
	
	"vari"{times=[0, 0.5, 1]}
	"vari"{fuel=[900, 1200]}
	"vari"{mod=[650, 700]}
	"vari"{cool=[550, 600]}
	"vari"{history=["nom", "pert"]}
	"vari"{isotopes=[531350, 541350, 922350]}
	
	
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	  STATES ORDER
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	
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
	History = "varo"{history[idxH]<s>}, Time = "varo"{times[idxB]<3.3f>}, Fuel T. = "varo"{fuel[idxF]<3.3f>}, Mod. T. = "varo"{mod[idxM]<3.3f>}, Cool. T. = "varo"{cool[idxC]<3.3f>} 
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
	
	
	
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	  INF_NSF
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	"vari"{idxE=-1}
	"rep"{2
	"vari"{idxE=idxE+1}
	  Group "varo"{idxE}
	  "values"{inf_nsf,  ["varo"{idxE}]} 
	"rep"}
	
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	  INF_SP0
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	"vari"{idxE0=-1}
	"rep"{2
	"vari"{idxE0=idxE0+1}
	"vari"{idxE1=-1}
	"rep"{{2
	"vari"{idxE1=idxE1+1}
	  Group "varo"{idxE0} --> Group "varo"{idxE1}
	  "values"{inf_sp0,  ["varo"{idxE0}, "varo"{idxE1}]} 
	"rep"}}
	"rep"}
	
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	  MICROSCOPIC FISSION XS
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	"vari"{idxS=-1}
	"rep"{3
	"vari"{idxS=idxS+1}
	* ----------------------------
	Isotope "varo"{isotopes[idxS]}
	* ----------------------------
	"vari"{idxE=-1}
	"rep"{{2
	"vari"{idxE=idxE+1}
	  Group "varo"{idxE}
	  "values"{sig_f, ["varo"{idxS}, "varo"{idxE}]} 
	"rep"}}
	
	"rep"}
