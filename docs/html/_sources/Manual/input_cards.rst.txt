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
:ref:`i_singleset`		Define data to be added to a specific (branch, history, time) set.
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

.. _i_singleset:

================
Single Set Data
================


**Data for a specific (branch, history, and time) set.**

*Mandatory Card*

.. code::
		
   set singleset <flux> <energy> 
   sub_card <val1> <val2> <val3> ...
   ...
  

where in the **set** line,
 - ``NG`` number of energy groups
 - ``DN`` number of delayed neutrons

and, the list of **sub-cards** options is:
	- ``branch`` numeric values corresponding to all the parameters in the branch-off.
	- ``history``
	- ``time`` 
	- ``macro`` names for the macroscopic parameters
	- ``micro`` names for the microscopic parameters
	- ``kinetics`` names for the kinetics parameters (e.g., beta values)
	- ``meta`` names for the metastable parameters
	- ``isotopes`` a list of isotopes in a ZZAAAM (e.g., 922350). User has a flexibility to define their own format.

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
