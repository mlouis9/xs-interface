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
:ref:`i_states`				Branches, history, and time-dependent perturbations.
--------------------- -------------------------------------------------------------------
:ref:`i_data`					Define data to be added.
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
_______________________________________________________________________________________________________________________________

**Names and dimensions of variables to be provided.**


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

.. note::
	
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


.. _i_states:

=========
states
=========
_______________________________________________________________________________________________________________________________


TBC


.. _i_data:

=========
data
=========
_______________________________________________________________________________________________________________________________


TBC