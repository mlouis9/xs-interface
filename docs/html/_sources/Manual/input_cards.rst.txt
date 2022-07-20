.. _universecards:


XSs Set Cards 
------------- 

For each unique cross-section set or universe a separate file is defined.
It is up to the user to control the data flow.

A list of all the input cards is descirbed in the table below.
Description on the format, comments, and magic capabilities is provided in :ref:`gen_comments`.

===================== ===================================================================
Set what?							Description
===================== ===================================================================
:ref:`i_settings`			Names and dimensions of variables to be defined.
--------------------- -------------------------------------------------------------------
:ref:`i_branches`			Branch-off names and values.
--------------------- -------------------------------------------------------------------
:ref:`i_histories`		Histories names and values.
--------------------- -------------------------------------------------------------------
:ref:`i_times`				Time units and values.
--------------------- -------------------------------------------------------------------
:ref:`i_data`					Define data to be added to a specific (branch, history, time) set.
--------------------- -------------------------------------------------------------------
:ref:`i_manipulate`		Data manipulation including energy condensation and math operations.
--------------------- -------------------------------------------------------------------
:ref:`i_filter`				States and data names to be filtered/included.
===================== ===================================================================



.. _gen_comments:

=================
General comments
=================
- Comments are denoted as ``#`` and ``%``. Inputs following these signs are ignored.
- Commas are allowed.
- Case insensitive (captial and lower cases are allowed)
- ``=`` signs are allowed to be added (but not mandatory) when the card name is provided.
- Empty lines are allowed between settings lines.
- Special characters (``? $ & ~ < >``) are not allowed.



.. _i_settings:

=========
settings
=========

**Names and dimensions of variables to be provided.**

*Mandatory Card*

.. code::
		
   set settings <NG> <DN>
   sub_card <val1> <val2> <val3> ...
   ...
  

where in the **set** line,
 - ``NG`` number of energy groups
 - ``DN`` number of delayed neutrons

and, the list of **sub-cards** options is:
	- ``macro`` names for the macroscopic parameters
	- ``micro`` names for the microscopic parameters
	- ``kinetics`` names for the kinetics parameters (e.g., beta values)
	- ``meta`` names for the metastable parameters
	- ``isotopes`` a list of isotopes in a ZZAAAM (e.g., 922350). User has a flexibility to define their own format.
	- ``nuclides`` name of the nuclide densities variable.

**Notes:**
	
	*	At least one of the following should be provided: `macro`, `micro`, `kinetics`, `meta`. User can omit specific entries (e.g., ``meta``).
	*	The sub-cards can be defined multiple times, e.g., 

	.. code::

		macro fiss
		macro nsf, kappa


	* If the sub-card ``micro`` is defined then the sub-cards ``isotopes`` and the ``nuclides`` will be expected as well.



**Example**:

.. code::

	set settings NG 2 DN 7
	macro =  abs, fiss, nsf
	macro = sct
	micro =  abs, fiss, nsf
	kinetics =  beta decay_const
	meta =  time keff
	isotopes = 531350, 541350
	nuclides = nd


.. _i_branches:

============
Branches
============


**Branchoff names and values.** 

*Mandatory Card*

.. code::
		
   set branches <N> <UNIT-1> ... <UNIT-N>
   <branch-1> <val1> <val2> <val3> ...
   <branch-2> <val1> <val2> <val3> ...
   ...
  

where in the **set** line,
 - ``N`` number of branch types (mandatory)
 - ``UNIT-N`` units corresponding to branch ``N``. Units are optional, but if provided must be given in the order the branches are provided.

and, in the **<branch> sub-cards**,
	- number of sub-cards must be equal to ``N``.
	- ``branch-N`` is the user-defined name (e.g., fuel) that will be assigned the N-th branch.
	- arbitrary number of numeric values can be provided for each branch.

	.. code::

		fuel 600.0 900.0 1200.0 1500.0 1800.0


**Notes:**	
	*	At least one branch must be provided.
	* If only a partial ``units`` list is provided, the remaining unprovided units are set to ``n/a``

**Examples**:

.. code::

		set branches 3
		fuel 600 900 1200 1500
		mod 500 600 700
		cool 500 600

or,

.. code::

		set branches 3 Kelvin Kelvin kg/m3
		fuel 600 900 1200 1500
		mod 500 600 700
		cool 500 600


.. _i_histories:

==========
Histories
==========


**Histories names and values.**

*Optional Card*

.. code::
		
   set histories <N>
   <history-1> <val1> <val2> <val3> ...
   <history-2> <val1> <val2> <val3> ...
   ...
  

where in the **set** line,
 - ``N`` number of history types (mandatory)

and, in the **<history> sub-cards**,
	- number of sub-cards must be equal to ``N``.
	- ``history-N`` is the user-defined name (e.g., nominal) that will be assigned the N-th history.
	- For each history, the number of values must be identical to the number of branches provided in the :ref:`i_branches` card. The order of these entries also corresponds the order the branches are provided. 
	- In the example below, three branches were provide in the ``set branches`` card ordering fuel temperature, moderator temperature, and coolant density. The card below describes a history named as nominal, in which the values correspond the branches in a respective order. 

	.. code::

		nominal 900.0, 550.0, 750.0


**Notes:**	
	*	At least one history must be provided.

**Examples**:

.. code::
	
	set histories 2
	nom 600 500 500
	pert 900 700 625


.. _i_times:

==========
Times
==========


**Time units and values.**

*Optional Card*

.. code::
		
   set times <UNITS>
   <val1> <val2> <val3> ...
   ...
  

where in the **set** line,
 - ``UNITS`` describe the units of time/burnup dependence. Can be arbitrary defined.

and, the time/burnup  values are provided in the following lines.
	- The values can be provided in a single or multiple lines.
	- Values must be given in ascending order.


**Notes:**	
	*	At least one time/burnup value must be provided.

**Examples**:

.. code::
		
	set times nounits
	0 1 2 3 4 5 6 7 8
	9 11 18 19
	40 50

.. _i_data:

======
Data
======


**Data for a specific (branch, history, and time) set.**

*Mandatory Card*

.. code::

	set data <FLUX> <ENE>
	block <BLOCK-1>
		<block_card1> <val1> <val2> <val3> ...
		<block_card2> <val1> <val2> <val3> ...
		...
	block <BLOCK-2>
		<block_card1> <val1> <val2> <val3> ...
		<block_card2> <val1> <val2> <val3> ...
		...  


where in the **set** line,
 - ``FLUX`` name of the flux variable
 - ``ENE`` energy structure in descending order. Must include upper and lower boundaries, e.g., for a 2-group structure:

	.. code::

		set data inf_flx 10.0E+6, 0.6025, 0.0


the  **BLOCK** options must include one of the following options to indicate what information comes next:
	- ``state`` state parameters (e.g., branch, time, history)
	- ``macro`` macroscopic parameters (e.g., energy groups dependent cross sections)
	- ``micro`` microscopic parameters (e.g., energy groups dependent cross sections)
	- ``kinetics`` kinetics parameters (e.g., beta values)
	- ``meta`` metastable parameters


the **sub-cards** defined under the different blocks are described below.
	**block** ``state``:
		- ``branch`` numeric values corresponding to all the parameters in the branch-off (e.g., 900.0, 500.0, 760.). Mandatory card.
		- ``time`` numeric value of the time point. Optional card.
		- ``history`` name of the history (e.g., `nominal`). Optional card.
		
	**block** ``macro``, ``kinetics``, ``meta``:
		- ``<block_card>`` is name corresponding to existing parameters provided under the :ref:`i_settings` card.
	**block** ``micro``:
		- ``name`` of the microscopic properties followed by numeric values.
		- the ``name`` of the property must be defined in a new line. Values must also be provided in new lines, where represents a specific isotope. e.g.,

		.. code::

			sig_f
			val11, val2  % isotope-1
			val11, val2  % isotope-2
			val11, val2  % isotope-3 

**Notes:**
	
	*	``state`` must be defined. 
	* At least one of the following should be provided: `macro`, `micro`, `kinetics`, `meta`.


**Example**:

.. code::

	set data inf_flx 10.0E+6, 0.6025, 0.0

	#-------------
	block state
	#----------
	branch 900.0, 550.0, 650.0
	history nom
	time 0.0
	
	#-------------
	block macro
	#----------
	inf_rabs 0.1, 0.2
	inf_nsf 0.3 0.4
	inf_flx 0.1 0.2
	inf_sp0 = 0.1  0.2 -0.05, 0.3
	
	#-------------
	block kinetics
	#-------------
	beta 1, 1, 1, 1, 1, 1, 1
	decay 1, 1, 1, 1, 1, 1, 1 
	
	#-------------
	block meta
	#-------------
	date April 09, 2022
	
	#-------------
	block micro
	#-------------
	nd
	1
	1
	1
	sig_sct
	11, 12, 21, 22  % isotope-1  
	11, 12, 21, 22  % isotope-2
	11, 12, 21, 22  % isotope-3
	sig_f
	11, 12  % isotope-1  
	11, 12  % isotope-2
	11, 12  % isotope-3



.. _i_manipulate:

==========
Manipulate
==========

**Macro and micro data manipulation including energy condensation and math operations.**

*Optional Card*

.. code::
		
   set manipulate <cutoffE>
   <var> <var1> <var2> <operation>
   ...
  

where in the **set** line,
 - ``cutoffE`` energy cutoffs used for energy condensation.

and, the following **lines** represent binary (between variable ``var1`` and ``var2``) mathematical operations to be performed.
	- ``var`` name of the new variable to be created. 
	- ``var1`` name of the first variable (e.g., ``inf_rabs``). Can only be of type ``macro`` or ``micro``.
	- ``var2`` name of the second variable (e.g., ``sig_f``).	Can only be of type ``macro`` or ``micro``.
	- ``operation`` mode of the mathematical operation with the following options only: ``add``, ``subtract``, ``multiply``, ``divide``.

**Notes:**
	
	*	``cutoffE`` must contain at least one number (which will generate a 2-group or 1-group structure). ``cutoffE`` must be within the energy bounds <ENE> defined in the :ref:`i_data` card.
		* ``cutoffE`` must be provided in descending order. To avoid energy condensation use the same cutoffs as defined in <ENE>.
	* A new energy grid will be created based on the provided ``cutoffE`` and closest energy boundaries <ENE> defined in the :ref:`i_data` card.
		* If <ENE> = ``10.0E+6, 0.6025, 0.0`` and <cutoffE> = ``0.005`` then a 1-group ``10.0E+6, 0.0`` will be created.
		* If <ENE> = ``10.0E+6, 0.6025, 0.0`` and <cutoffE> = ``0.6025`` or above then 2-groups ``10.0E+6, 0.6025, 0.0`` will be created.
		* For the provided <ENE> structure if <cutoffE> equals to the outermost left or right boundary a 1-group ``10.0E+6, 0.0`` will be utilized.
		* <cutoffE> cannot create a finer grid than <ENE> regardless to how many ``cutoffE`` boundaries are provided (as no interpolation is used).

	*	The number of lines that follow the set line represent the number of mathematical operations to be performed.
	* ``var1`` (e.g., inf_nsf) and ``var2`` (e.g., sig_f)  must be defined under the ``macro`` or ``micro`` blocks in :ref:`i_data` card.

	.. code::

		set manipulate 0.0
		reduced_nsf, inf_nsf, sig_f, subtract
		
	* The created ``var`` can also be used as ``var1`` or ``var2``. Note that if ``var`` already exists it will be overwritten with the newly created ``var``.

	.. code::

		...
		reduced_nsf1, inf_nsf, reduced_nsf, add
			
	
	
	* The order at which ``var1`` and ``var2`` are provided is important for the mathematical operation. 

	The following code:

	.. code::

		set manipulate 0.625
		a a1 a2 subtract
		b b1 b2 divide

	Correspond to:

	.. math::

		a = a_1 - a_2
		
		b = b_1 : b_2


	* ``var1`` and ``var2`` must be of either macro or micro types. The newly created variable ``var`` depends on the definitions of ``var1`` and ``var2``. 
	* Let us use the following example to describe the possible outcomes:
	
	.. code::

		set manipulate 0.625
		a a1 a2 subtract
	
	* If both are macro then a new macro variable ``a`` is created.
		
		.. math::
			a = a_1 - a_2
		
	* If ``var1`` macro and ``var2`` is micro then the new variable ``a`` is of type macro. Note that ``var1`` can be micro and ``var2`` macro as well. The :math:`N_j` represents the nuclide densities that are expected to be defined.
		
		.. math::
			a = a_1 - \sum a_{2,j}N_j		
		

	* If ``var1`` and ``var2`` are both micro then the new variable ``a`` is of type micro.
		
		.. math::
			a = a_1 - a_{2,j}	

	* In all the cases the variable ``a`` will preserved the original size of the condensed (or original) energy structure.



**Example**:

.. code::

	set manipulate 0.0
	new_nsf, inf_nsf, sig_f, subtract
	new_sct, inf_sp0, sig_sct, add



.. _i_filter:

======
Filter
======

**States and data names to be filtered.**

*Optional Card*

.. code::
		
   set filter <N-branches> <history> <time> <attrs>
   branch_card1 <val1> <val2> <val3> ...
   ...
   branch_cardN <val1> <val2> <val3> ...
   history-1 history-2 ...
   time-1 time-2 ...
   attr-1 attr-2 ...
   

where in the **set** line,
 - ``N-branches`` integer number of the filtered branches. 
 - ``history`` a boolean flag to indicate if histories are to be filtered. 0 = no filtering; filtering is done for any number above zero.
 - ``time`` a boolean flag to indicate if time is to be filtered. 0 = no filtering; filtering is done for any number above zero.
 - ``attrs`` a boolean flag to indicate if attributes are to be filtered. 0 = no filtering; filtering is done for any number above zero.

and, the list of **sub-cards** options is:
	- ``branch_card`` name of the branch followed by values of that branch. Use new line for each branch. e.g., 

	.. code::

		fuel 900 1500
		mod 600	
	
	- ``history-1 history-2 ...`` A single line that contains histories to be included. Can be defined only if <history> is above zero, otherwise omitted.
	- ``time-1 time-2 ...`` A single line that contains time values to be included. Can be defined only if <time> is above zero, otherwise omitted.
	- ``attr-1 attr-2 ...`` A single line that contains attribute names to be included. Can be defined only if <attrs> is above zero, otherwise omitted.

**Notes:**
	
	*	If any of the branches is not provided but does exist in the :ref:`i_branches` it will be automatically included.
		
		* For example, if the following branches are defined:
		
		.. code::

			set branches 3 Kelvin Kelvin kg/m3
			fuel 600 900 1200 1500
			mod 500 600 700
			cool 500 600
		
		* Using the following definition, the ``cool`` branch (with 500 600 kg/m3) will be included when priniting.

		.. code::
		
			set filter 2 0 0 0
			fuel 1500
			mod 600	

	* Similarly, if any of the <history> <time> <attrs> is omitted, but included in the :ref:`i_histories`, :ref:`i_times` or :ref:`i_data` it will be automatically included.
		* For example, if the following histories are defined:
		
		.. code::

			set histories 2
			nom 600 500 500
			pert 900 700 625
		
		* Using the following definition, both the ``nom`` and ``pert`` histories are included when printing.

		.. code::
		
			set filter 2 0 0 0
			fuel 1500
			mod 600	

	* Values that are defined in the ``filter`` card must exist in the :ref:`i_branches`, :ref:`i_histories`, :ref:`i_times` and :ref:`i_data` .



**Example**:

.. code::

	set filter 3 1 1 1
	fuel 1500
	mod 600
	cool 500
	nom
	0.0
	inf_rabs inf_nsf sig_f nd
