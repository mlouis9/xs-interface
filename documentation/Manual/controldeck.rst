.. _controldeck:


Control Deck
------------ 

This is the main file that controls the flow of data and the corresponding output formatting.

A list of all the input cards within this file is descirbed in the table below.
Description on the format, comments, and magic capabilities is provided in :ref:`gen_comments`.

===================== ===================================================================
Set what?							Description
===================== ===================================================================
:ref:`j_universes`		Definition of universe Ids and correpsonding input files.
--------------------- -------------------------------------------------------------------
:ref:`j_templates`		Definition of template Ids and correpsonding template files.
--------------------- -------------------------------------------------------------------
:ref:`j_outputs`		  Definition of template Ids and correpsonding output file names.
--------------------- -------------------------------------------------------------------
:ref:`j_links`				Linking between template Ids and universe Ids..
--------------------- -------------------------------------------------------------------
:ref:`j_formats`			Formatting control parameters.
===================== ===================================================================

.. _j_universes:

=========
universes
=========

**Names/Ids of the universes and the full dir path of their corresponding input file.**

*Mandatory Card*

.. code::
		
   set universes
   <universe name1> <corresponding universe file 1>
   <universe name2> <corresponding universe file 2>
   ...
  

where,

 - ``universe name`` is a user defined name of that specific cross-section set.
 - ``universe file`` is the full path dir + name to the universe file.


**Notes:**
	
	*	This card cannot be empty.
	*	Unique ``universe name`` must have unique ``universe file``.


**Example**:

.. code::

	set universes
	u0 ..\inputsets\u0
	u1 ..\inputsets\u1
	u2 ..\inputsets\u2


.. _j_templates:

=========
templates
=========

**Names/Ids of the templates and the full dir path of their corresponding template file.**

*Mandatory Card*

.. code::
		
   set templates
   <template name1> <corresponding template file 1>
   <template name2> <corresponding template file 2>
   ...
  

where,

 - ``template name`` is a user defined name/Id of that specific template.
 - ``template file`` is the path dir + file name to the template file.


**Notes:**
	
	*	This card cannot be empty.
	*	Unique ``template name`` must have unique ``template file``.


**Example**:

.. code::

	set templates
	template1 ..\templates\dyn3d
	template2 ..\templates\parcs

.. _j_outputs:

=======
outputs
=======

**Names/Ids of the templates and the full dir path of the output files that will be using that specific template.**

*Mandatory Card*

.. code::
		
   set outputs
   <template name1> <output file 1>
   <template name2> <output file 2>
   ...
  

where,

 - ``template name`` is user defined name/Id of that specific template. Must correspond to the name defined under the :ref:`j_templates` card.
 - ``output file`` is the path dir to where the cross sections will be written to.


**Notes:**
	
	*	This card cannot be empty.
	*	Unique ``template name`` must have unique ``output files``.


**Example**:

.. code::

	set outputs
	template1 ..\junkfiles\output1
	template2 ..\junkfiles\output2

.. _j_links:

=====
links
=====

**Linkage between universes and templates Ids.**

This card allows to apply the same template file for multiple universes without the need to define unique template file for each universe separately.
This capability is convient when the use want to use the same template file for multiple universes.
It must be pointed out that if this card is not provided, the explicit definition of universes must be provided within the template files themselves.

*Optional Card*

.. code::
		
   set links
   <template name1> <universe name11> <universe name12> ...
   <template name2> <universe name21> <universe name22> ...
   ...
  

where,

 - ``template name`` is an user defined name/Id of that specific template. Must correspond to the name defined under the :ref:`j_templates` card.
 - ``universe name1`` is the user defined universe name or Id.


**Notes:**
	
	*	This card can be omitted.
	*	Each ``template name`` can have a single or multiple ``universe name``.
	* If multiple universes are provided for a specific template then multiple ooutput files will be created. Their naming will differe by the postfix name of the specific universe, e.g. ``output_u0``, ``output_u1`` and so on. 


**Example**:

.. code::

	set links
	template1 u0 u1
	template2 u2


.. _j_formats:

=======
formats
=======

**Output formatting.**

This card allows to control the formatting of the different output variables.


*Optional Card*

.. code::
		
   set formats <N> <Postfix>
   state <state_format>
   attr <attr_format>
   var <var_format>
 
where,

 - ``N`` is the maximum number of values printed in each row. Provided as an integer.
 - ``Postfix`` is the postfix of the file name, e.g. .dat and .txt. If ``Postfix`` not provided no postfix will be used.
 - ``state``, ``attr``, and ``var`` are all preserved keywords.
 - ``state`` denotes state perturbation parameter, such as time, history, or branch.
 - ``attr`` denotes a macro or micro data, such as the fission cross section.
 - ``var`` denotes a user-defined variable used within the template file (more dtails can be found in ...).
 - The default values for ``state_format``, ``attr_format``, and ``var_format`` are: 5.3f, 5.5e, d


**Notes:**
	
	*	This card can be omitted.
	*	Only standard python formatting notation is allowed, e.g., 5.5f, 6.6e, 3d.
	* The entries for ``state``, ``attr``, and ``var`` are optional and can provided in any order or partially/fully omitted.


**Example**:

.. code::

	set formats 8
	state 5.5f
	attr 6.6e
	var 5d
	
or

.. code::

	set formats 4 .txt
	attr 6.6e
	