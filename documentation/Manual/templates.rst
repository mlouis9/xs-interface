.. _templates:


Templates
--------- 

The template file makes the use of prescribed rules to efficiently define a template that can be used to output data in the most general possible way.

The text file provided by the user is a format-free. The text contained within the template file is copied to the desired output.
However, the simple rules provided by the user resemble codes' snippets that allow to define variables dynamically rather than using fix values.

A list of three basic rules are listed in the table below, and examples of how to use these are provided in the following sections.

================= ==========================================================
Rule							Description
================= ==========================================================
:ref:`vari`				Definition of an input variable to be executed internally.
----------------- ----------------------------------------------------------
:ref:`varo`				Definition of an output variable to be printed.
----------------- ----------------------------------------------------------
:ref:`values`			Evaluation of parameters defined by the user in :ref:`universecards`
----------------- ----------------------------------------------------------
:ref:`repblocks`	Text blocks to be repeated.
================= ==========================================================


.. _vari:

==============
Input Variable
==============

**Definition of a simple execution line.**

The user has the ability to define a code snippet that will be executed internally within the code.
The code provided by the user should be as simple as possible. For example, assigning value to a variable (scalar or vector), rather than implementing a while loop. 
The use of ``for`` loops is feasibile but not recommended.

Only a **single input variable** can be defined in a single line. The format for defining an input variable is: 

.. code::
		
   "vari"{<command line>}
 
where,

 - ``"vari"{...}`` is preserved (including the curley brackets) keyword.
 - ``<command line>`` is the execution command sequence.

**Notes:**
	
	*	The use of the command is primarily intended for defining indices and changing these dynamically.
	* All the occurrences of ``"vari"{...}`` will not appear in the output files.

**Examples**:


- Index definition

	.. code::
	
		"vari"{idxB=-1}
	
- Index promotion

	.. code::
	
		"vari"{idxB=idxB+1}
		
- Vector definition

	.. code::
	
		"vari"{times=[0.0, 1.0, 5.0, 10.0]}





.. _varo:

===============
Output Variable
===============

**Output the values of a certain input variable.**

Here the user has the ability to write the value/s of :ref:`vari` directly to the output file.

**Multiple output variable** can be defined in a single line. The format for defining an output variable is: 

.. code::
		
   "varo"{<evaluation command><<format>>}
 
where,

 - ``"varo"{...}`` is preserved (including the curley brackets) keyword.
 - ``<evaluation command>`` is the execution sequence for evaluating an input variable.
 - ``<format>`` a standard format notation, e.g., ``3d``, ``3.3f``, ``5.5e`` with which the input variable will be written in the output file. If provided, the format **must** be provided within ``<...>`` brackets.
 - ``<format>`` can be omitted along with the ``<...>`` brackets. In which case, the default value will be used according to the format defined in the control deck (:ref:`j_formats`).

**Notes:**
	
	*	The ``"varo"{...}`` should not be used to execute a new command but rather to evaluate a certain input variable.
	* The input variables to be evaluated and printed must be already defined in the template. 

**Examples**:


- Output a simple variable

	.. code::
	
		"vari"{idxE=-1}
		"vari"{idxE=idxE+1}
		"varo"{idxE}
		
	The outcome in the output file is:

	.. code::
	
		0	
	
	
- Compound evaluation (variable within a variable).

	.. code::
	
		"vari"{times=[0, 1]}
		"vari"{idxB=-1}
		"vari"{idxB=idxB+1}
		* BURNUP  "varo"{times[idxB]<3.3f>} 
		
	The outcome in the output file is:

	.. code::
	
		* BURNUP  0.000 	
		
- Multiple output variables in a single line.

	.. code::
	
		"vari"{idxE0=-1}
		"vari"{idxE0=idxE0+1}
		"vari"{idxE1=-1}
		"vari"{idxE1=idxE1+1}
		*   Group "varo"{idxE0<5d>} --> "varo"{idxE1<5d>}

	The outcome in the output file is:

	.. code::
	
		*   Group     0 -->     0	
		

- Compound evaluation with multiple output variables.

	.. code::
	
		"vari"{inf_sp0=[[0.1, 0.2],[-0.05 , 0.3]]}
		"vari"{idxE0=-1}
		"vari"{idxE0=idxE0+1}
		"vari"{idxE1=-1}
		"vari"{idxE1=idxE1+1}
		*   sp0 value "varo"{inf_sp0[idxE0,indxE1]<6.6e>}

	The outcome in the output file is:

	.. code::
	
		*   sp0 value       1.000000e-01

.. _values:

===========
Data Values
===========

**Evaluation and output of attributes/states.**

This is the heart of the template capability as different parameters defined in the universes objects - :ref:`universecards` can be evaluated and written to output files.
At the moment, only a single evaluation can be performed in a single line.

The format for evaluating and printing an output attribute, e.g., cross sections or states: 

.. code::
		
   "values"{<universe Id>, <attribute>, <state1>=<value1>, <state2>=<value2>, 
   	   ..., <stateN>=<valueN>  [<indices>] <<format>><N>} 
 
where,

 - ``"values"{...}`` is preserved (including the curley brackets) keyword.
 - ``<universe Id>`` is the name of the universe as defined in :ref:`universecards`.
 - ``<attribute>`` is the name of the output variable. It can represent a state (e.g., fuel temperature) or an attribute (e.g., beta).
 - ``<state1>``, ``<state2>``, ... represent the names of the various states (e.g., fuel, moderator, coolant temperatures). The latter are defined in the :ref:`i_branches`, :ref:`i_histories`, and :ref:`i_times`	cards.
 - ``<value1>``, ``<value2>``, ... are the corresponding singular values for each of the various states.
 - ``<indices>`` are the indices provided to assess the data at specific index values. For example, if beta has six delayed neutron groups, a specific group can be accessed by applying the indices.
 - ``<format>`` a standard format notation, e.g., ``3d``, ``3.3f``, ``5.5e`` with which the input variable will be written in the output file. If provided, the format **must** be provided within ``<...>`` brackets. The format can also include space, delimiter, and spaces again. In which case, these spaces and delimiter will be added to how the results will be printed out.
 - ``<format>`` can be omitted along with the ``<...>`` brackets. In which case, the default value will be used according to the format defined in the control deck (:ref:`j_formats`).
 - ``<N>`` is max number of values that can be printed in a single line. It can be provided only if the ``format`` is provided. It can also be omitted, even if ``format`` is provided.
 - Default values for ``<format>`` and ``<N>`` are defined in :ref:`j_formats`.

**Notes:**
	* ``<universe Id>`` can be provided or omitted. However, if it is omitted, the :ref:`j_links` card must be set under the :ref:`controldeck` file.
	* ``<attribute>`` is mandatory and must exist in the definition of the universe (:ref:`i_settings`). Attribute can also include states' names.
	* ``<state>`` must be defined in :ref:`i_branches` or :ref:`i_histories` or :ref:`i_times`.
	* ``<state>`` can either be a branch name defined in :ref:`i_branches`, or the preserved keyword ``history`` or the preserved keyword ``time``. Not all the states must be provided.
	* ``<value>`` must exist in the data definition provided in :ref:`i_data`. 
	* It must be pointed out that when executing the "values"{...} comand, not all states that exist in :ref:`i_data` must be provided. For example, if the states include multiple fuel and coolant temperatures, and the command is evaluated for a specific fuel temperature then all the existing coolant temperatures that correspond to this fuel temperatures will be evaluated and written.
	* ``<indices>`` must be provided in square brackets [...]. However, indices can also be omitted, in which case no [...] brackets are required.
	* It is up to the user to know how to slice the data as the user was reponsible to feed the data in.
	* The most important note is to understand that when the ``values`` command is provided, the program evaluates the values using the ``universes.Values`` method internally. The end result can yield a scalar, vector, or a matrix.

**Examples**:


- Simple and direct evaluation. 

	.. code::
	
		"values"{u0, inf_rabs, fuel=1500, time=0.0, history=nom  [0] <5.5e>4}

		
	Let's assume that only a single state of fuel=1500 and time=0.0 was defined. The attribute ``inf_rabs`` has 2-group values. Therefore, the index ``0`` will evaluate only the first value in the array. If we want to use multiple spaces and delimiter, the following can be used.

	.. code::

		"values"{u0, inf_rabs, fuel=1500, time=0.0, history=nom  [0] <5.5e  ;  >4}	

	
- Compound evaluation.

	.. code::
	
		"vari"{times=[0, 1]}
		"vari"{idxB=0}
		"vari"{idxE=0}
		"values"{u0, inf_rabs, fuel=1500, time="varo"{times[idxB]}  ["varo"{idxE}]} 

		
	This example will yield exactly the same result as the previous one. However, the slicing of data is performed dynamically by using the "varo"{...} commands.


- Compound evaluation without defining the universe explicitly in the file.

	.. code::
	
		"vari"{times=[0, 1]}
		"vari"{idxB=0}
		"vari"{idxE0=0}
		"vari"{idxE1=1}
		"values"{inf_sp0, fuel=1500, time="varo"{times[idxB]}  ["varo"{idxE0}, "varo"{idxE1}]}

		
	This example shows the flexibility of the slicing method defined within the [...] brackets as in this case the attribute ``inf_sp0`` is a 2-dim array. Note that the universe is not explicitly defined here. This means that the universe Ids and templates must be linked using the ``set links`` card in :ref:`j_links`.



- Evaluation without slicing.

	.. code::
	
		"vari"{times=[0, 1]}
		"values"{inf_rabs, fuel=1500}

		
	Let's still assume we only have a single state or data point. However, now we do not use the indices. Therefore, the written outcome will include both group values.
	

- Evaluation of multiple states.

	.. code::
	
		"vari"{times=[0, 1]}
		"values"{inf_rabs, fuel=1500 <5.5e>4}

		
	Let's now assume that we have one fuel temperature as a state and 10 coolant tempeatures. For similicity we will assume that there is a single energy group. The command above will return 10 values that correspond to all the coolant densities.
	

Please note that according to the above example the maximum number of values allowed to be printed in a single line is 4. However, the previous command yields 10 values. These will be printed in the following order. First four in one line, next four values in the following line, and the remaining two values in the third line. 


.. _repblocks:

=================
Repetitive Blocks
=================

**Repetitive text blocks that are duplicated.**

This capability allows to duplicate blocks without the explicit need of the user to copy the data multiple times within the file.
Sub-blocks can be defined within blocks, and these can also include dynamic commands for effective templating. 

The format for defining a repetitive block is: 

.. code::
		
   "rep"{<N>
   ...
   ...
   "rep"}		

 			 
where,

 - ``"rep"{...}`` is preserved (including the curley brackets) keyword.
 - ``<N>`` represent the number of times the block will be replicated.
 - It is important to note that ``<N>`` can be represented by an existing variable called by the ``"varo"{...}`` capability.
 
	.. code::
	
		"rep"{"varo"{num} 
 
 
 - The number of curley brackets indicates the hierarchy of the block. Nested blocks can be defined within blocks, but with structured hierarchy.
 
	.. code::
			
	   "rep"{<N>
	   block-1
	   "rep"{{<M>
	   block-2
	   "rep"}}
	   "rep"}		 

 - In the application above, block-2 will be duplicated M times and then block-1 (including the duplicated block-2) will be duplicated N times.

 - The hierarchy rules allow to have ``{{``  blocks within ``{``, ``{{{`` within ``{{``, and so on. Several same-level blocks can appear in higher level blocks. For example:
 
	.. code::
			
	   "rep"{<N1>
	   Block-1- repreated N1 times
	   "rep"{{<M1>
	   Block-2.1- repreated M1 times
	   "rep"}}
	   "rep"{{<M2>
	   Block-2.2- repreated M2 times
	   "rep"}}	   
	   "rep"}	
 
 - The outcome of the above block results in outputting:
 
	.. code::
			
	   Block-1- repreated N1 times.
	   Block-2.1- repreated M1 times
	   ...
	   Block-2.1- repreated M1 times
	   Block-2.2- repreated M2 times
	   ...
	   Block-2.2- repreated M2 times
	   Block-1- repreated N1 times.
	   Block-2.1- repreated M1 times
	   ...
	   Block-2.1- repreated M1 times
	   Block-2.2- repreated M2 times
	   ...
	   Block-2.2- repreated M2 times
	   ...
	   Block-1- repreated N1 times.
	   Block-2.1- repreated M1 times
	   ...
	   Block-2.1- repreated M1 times
	   Block-2.2- repreated M2 times
	   ...
	   Block-2.2- repreated M2 times

**Notes:**
	* Several same-level blocks can exist.
	* Lower-level blocks (e.g., ``{{``) can not contain higher-level blocks (e.g., ``{``). The following shows an example of an *erroneous* snippet:

	.. code::

	   "rep"{{<N>
	   block-1
	   "rep"{{<M>
	   block-2
	   "rep"}
	   "rep"}}
	   
	* A higher-level (e.g., ``{``) cannot end before all lower-level blocks are closed. An example of an *erroneous* snippet:

	.. code::

	   "rep"{<N>
	   block-1
	   "rep"{{<M>
	   block-2
	   "rep"}
	   "rep"}}	
	
	* The real strength of the repetitive blocks is the ability to use dynamic commands that will assess the data/variables.

**Examples**:

The examples below integrate the use of all the rules in conjuction with the "rep"{...} blocks.


- Two-tier hierarchy levels example

	.. code::
		
		"vari"{times=[0, 1]}
		"vari"{idxB=-1}
		"rep"{2
		* ----------------------------------------------------------------
		"vari"{idxB=idxB+1}
		* BURNUP  "varo"{times[idxB]<3.3f>} 
		* ----------------------------------------------------------------
		* 
		* Transport XSEC Table
		* 
		"vari"{idxE=-1}
		"rep"{{2
		"vari"{idxE=idxE+1}
		  
		  Group "varo"{idxE}
		  "values"{inf_rabs, fuel=1500, time="varo"{times[idxB]}  ["varo"{idxE}]} 
		
		"rep"}}
		"rep"}
		
	The energy group values of the ``inf_rabs`` cross section are 0.1 and 0.2 respectively for both the 0.0 and 1.0 time points. The format chosen by the ``set formats`` (:ref:`j_formats`) card is ``6.6e``. The printed output is therefore:


	.. code::
	
		* ----------------------------------------------------------------
		* BURNUP  0.000 
		* ----------------------------------------------------------------
		* 
		* Transport XSEC Table
		* 
		  
		  Group     0
		   1.000000e-01 
		
		  
		  Group     1
		   2.000000e-01 
		
		* ----------------------------------------------------------------
		* BURNUP  1.000 
		* ----------------------------------------------------------------
		* 
		* Transport XSEC Table
		* 
		  
		  Group     0
		   1.000000e-01 
		
		  
		  Group     1
		   2.000000e-01 
		

- Three-tier hierarchy levels example

	.. code::
		
		"vari"{times=[0, 1]}
		"vari"{idxB=-1}
		"rep"{2
		* ----------------------------------------------------------------
		"vari"{idxB=idxB+1}
		* BURNUP  "varo"{times[idxB]<3.3f>} 
		* ----------------------------------------------------------------
		* 
		* Scattering XSEC Table
		* 
		"vari"{idxE0=-1}
		"rep"{{2
		"vari"{idxE0=idxE0+1}
		"vari"{idxE1=-1}
		"rep"{{{2
		"vari"{idxE1=idxE1+1}
		*   Group "varo"{idxE0} --> "varo"{idxE1}
			"values"{inf_sp0, fuel=1500, time="varo"{times[idxB]}  ["varo"{idxE0}, "varo"{idxE1}]}
		* 
		"rep"}}}
		"rep"}}
		
		"rep"}
		
	The arbitrary defined scattering group-to-group matrix of ``inf_sp0`` is [[0.1, 0.2], [-0.05, 0.3]] for both the 0.0 and 1.0 time points. The format chosen by the ``set formats`` (:ref:`j_formats`) card is ``6.6e``. The printed output is therefore:


	.. code::
	
		* ----------------------------------------------------------------
		* BURNUP  0.000 
		* ----------------------------------------------------------------
		* 
		* Scattering XSEC Table
		* 
		*   Group     0 -->     0
			 1.000000e-01
		* 
		*   Group     0 -->     1
			 2.000000e-01
		* 
		*   Group     1 -->     0
			 -5.000000e-02
		* 
		*   Group     1 -->     1
			 3.000000e-01
		* 
		
		* ----------------------------------------------------------------
		* BURNUP  1.000 
		* ----------------------------------------------------------------
		* 
		* Scattering XSEC Table
		* 
		*   Group     0 -->     0
			 1.000000e-01
		* 
		*   Group     0 -->     1
			 2.000000e-01
		* 
		*   Group     1 -->     0
			 -5.000000e-02
		* 
		*   Group     1 -->     1
			 3.000000e-01
		* 
		

		
