.. _single_template2:

Template 2
----------

This template presents a mix of :ref:`single_template0` and  :ref:`single_template1`. The template also demonestrates how to change the order of writing data.

Please note that every time the "values" rule is used all the variables are dynamically defined excluding the ``fuel`` parameter. This results in obtaining 2 values for the parameter of interest (e.g., ``inf_nsf``) corresponding to the 2 fuel state points of 900K and 1200K.
The following iterative sequence is implemented here via the use of the "rep" rules.

.. code::

	for idxH in (range(len(history)):
		for idxB in (range(len(times)):
			for idxE in (range(2)):
				for idxM in (range(len(mod)):
					for idxC in (range(len(cool)):
						Do something ...

The corresponding output file can be found in :ref:`single_output2`.



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
	  INF_NSF
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	
	"vari"{idxH=0}
	"rep"{2
	"vari"{idxB=0}
	"rep"{{3
	
	"vari"{idxE=-1}
	"rep"{{{2
	"vari"{idxE=idxE+1}
	  ---- Group "varo"{idxE} 
	"vari"{idxM=0}
	"rep"{{{{2
	"vari"{idxC=0}
	"rep"{{{{{2	
		History = "varo"{history[idxH]<s>}, Time = "varo"{times[idxB]<3.3f>}, Mod. T. = "varo"{mod[idxM]<3.3f>}, Cool. T. = "varo"{cool[idxC]<3.3f>}, Fuel T. = "varo"{fuel<3.3f>}
	  "values"{inf_nsf, history="varo"{history[idxH]<s>}, time="varo"{times[idxB]<3.3f>}, mod="varo"{mod[idxM]<3.1f>}, cool="varo"{cool[idxC]<3.1f>}  ["varo"{idxE}]} 
	
	"vari"{idxC=idxC+1}
	"rep"}}}}}
	"vari"{idxM=idxM+1}
	"rep"}}}}  
	"rep"}}}  % Energy
	"vari"{idxB=idxB+1}
	"rep"}}   % time
	"vari"{idxH=idxH+1}
	"rep"}    % history
	
	
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	  INF_SP0
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	
	"vari"{idxH=0}
	"rep"{2
	"vari"{idxB=0}
	"rep"{{3
	
	"vari"{idxE0=-1}
	"rep"{{{2
	"vari"{idxE0=idxE0+1}
	"vari"{idxE1=-1}
	"rep"{{{{2
	"vari"{idxE1=idxE1+1}
	  ---- Group "varo"{idxE0} --> Group "varo"{idxE1} 
	"vari"{idxM=0}
	"rep"{{{{{2
	"vari"{idxC=0}
	"rep"{{{{{{2	
		History = "varo"{history[idxH]<s>}, Time = "varo"{times[idxB]<3.3f>}, Mod. T. = "varo"{mod[idxM]<3.3f>}, Cool. T. = "varo"{cool[idxC]<3.3f>}, Fuel T. = "varo"{fuel<3.3f>}
	  "values"{inf_sp0, history="varo"{history[idxH]<s>}, time="varo"{times[idxB]<3.3f>}, mod="varo"{mod[idxM]<3.1f>}, cool="varo"{cool[idxC]<3.1f>}  ["varo"{idxE0}, "varo"{idxE1}]} 
	
	"vari"{idxC=idxC+1}
	"rep"}}}}}}
	"vari"{idxM=idxM+1}
	"rep"}}}}}  
	"rep"}}}}  % Energy  
	"rep"}}}  % Energy
	"vari"{idxB=idxB+1}
	"rep"}}   % time
	"vari"{idxH=idxH+1}
	"rep"}    % history
	
	
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	  MICROSCOPIC FISSION XS
	* ---------------------------------------------------------------------------------------------------------------------------------------------------
	
	
	"vari"{idxH=0}
	"rep"{2
	"vari"{idxB=0}
	"rep"{{3
	
	"vari"{idxS=-1}
	"rep"{{{3
	"vari"{idxS=idxS+1}
	Isotope "varo"{isotopes[idxS]}
	"vari"{idxE=-1}
	"rep"{{{{2
	"vari"{idxE=idxE+1}
	  ---- Group "varo"{idxE}
	"vari"{idxM=0}
	"rep"{{{{{2
	"vari"{idxC=0}
	"rep"{{{{{{2	
		History = "varo"{history[idxH]<s>}, Time = "varo"{times[idxB]<3.3f>}, Mod. T. = "varo"{mod[idxM]<3.3f>}, Cool. T. = "varo"{cool[idxC]<3.3f>}, Fuel T. = "varo"{fuel<3.3f>}
	  "values"{sig_f, history="varo"{history[idxH]<s>}, time="varo"{times[idxB]<3.3f>}, mod="varo"{mod[idxM]<3.1f>}, cool="varo"{cool[idxC]<3.1f>}  ["varo"{idxS}, "varo"{idxE}]} 
	
	"vari"{idxC=idxC+1}
	"rep"}}}}}}
	"vari"{idxM=idxM+1}
	"rep"}}}}}  
	"rep"}}}}  % Energy  
	"rep"}}}  % isotope
	"vari"{idxB=idxB+1}
	"rep"}}   % time
	"vari"{idxH=idxH+1}
	"rep"}    % history