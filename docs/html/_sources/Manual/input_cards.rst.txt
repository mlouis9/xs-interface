.. _inputcards:


Input Cards 
------------ 

A list of all the input cards is descrbed in the table below.
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
===================== ===================================================================



.. _gen_comments:

=================
General comments
=================
- Comments are denoted as ``#`` and ``%``. Input followowing these signs is ignored.
- Commas are allowed.
- Case insensitive (captial and lower cases are allowed)
- Setting lines can include or exclude the card name.
	- Example of excluding: ``set settings 2 7``
	- Example of including: ``set settings NG=2, DN=7``
	- The benifit of including is to determine the order at which values are provided.
- ``=`` signs are allowed to be added (but not mandatory) when the card name is provided.
- Empty lines are allowed between settings lines.
- Special characters (``? $ & @ ~ < >``) are not allowed.



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
	- ``dim_macro`` dimensions of the macroscopic parameters
	- ``dim_micro`` dimensions of the microscopic parameters
	- ``dim_kinetics`` dimensions of the kinetics parameters (e.g., beta values)
	- ``dim_meta`` dimensions of the metastable parameters

**Notes:**
	
	*	At least one of the following should be provided: `macro`, `micro`, `kinetics`, `meta`. User can omit specific entries (e.g., ``meta``).
	* Dimensions are not required to be provided and the dafualt is 1-dim for every parameter. If a 2D array is provided, the user needs to define the dimensions. ``0`` indicates that dimensions are not required to be verified.
	*	The sub-cards can be defined multiple times, e.g., 

	.. code::

		macro fiss
		macro nsf, kappa

		
	* If sub-cards are defined multiple times, the corresponding dimensions must describe these accordingly, e.g.,
	
	.. code::

		macro fiss nsf
		dim_macro 1 1
		macro sct
		dim_macro 2

	or
	
	.. code::

		macro fiss nsf
		macro sct
		dim_macro 1 1 2	

	* If the sub-card ``micro`` is defined then the sub-card ``isotopes`` will be expected as well.



**Example**:

.. code::

	set settings NG 2 DN 7
	macro =  abs, fiss, nsf
	macro = sct
	dim_macro = 1, 1, 1, 2
	micro =  abs, fiss, nsf
	kinetics =  beta decay_const
	meta =  time keff
	isotopes = 531350, 541350


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
 - ``UNITS`` describe the units of time/burnup dependence.

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
	sig_sct
	11, 12, 21, 22  % isotope-1  
	11, 12, 21, 22  % isotope-2
	11, 12, 21, 22  % isotope-3
	sig_f
	11, 12  % isotope-1  
	11, 12  % isotope-2
	11, 12  % isotope-3
