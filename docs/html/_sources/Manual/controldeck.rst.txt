.. _controldeck:


Control Deck
------------ 

This is the main file that controls the flow of data and the corresponding output formatting.

A list of all the input cards within this file is provided in the table below.

===================== ===================================================================
Set what?							Description
===================== ===================================================================
:ref:`j_universes`		Definition of universe Ids and correpsonding input files.
--------------------- -------------------------------------------------------------------
:ref:`j_templates`		Definition of template Ids and correpsonding template files.
--------------------- -------------------------------------------------------------------
:ref:`j_outputs`		  Definition of template Ids and correpsonding output file names.
--------------------- -------------------------------------------------------------------
:ref:`j_links`				Linking between template Ids and universe Ids.
--------------------- -------------------------------------------------------------------
:ref:`j_serpent`			Linking between user-defined universe Ids and serpent-defined universe Ids.
--------------------- -------------------------------------------------------------------
:ref:`j_shift`				Linking between user-defined universe Ids and shift-defined universe Ids.
--------------------- -------------------------------------------------------------------
:ref:`j_formats`			Formatting control parameters.
--------------------- -------------------------------------------------------------------
:ref:`j_map`					Map with radial channels distribution.
--------------------- -------------------------------------------------------------------
:ref:`j_channels`			Definition of the channels using existing universes.
--------------------- -------------------------------------------------------------------
:ref:`j_volumes`			Volumes corresponding to all the defined channels.
===================== ===================================================================

.. _j_universes:

=========
universes
=========

**Names/Ids of the universes and their corresponding input files.**

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

**Names/Ids of the templates and their corresponding template files.**

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

**Names/Ids of the templates and and the corresponding output files that will use these templates.**

*Mandatory Card*

.. code::
		
   set outputs
   <template name1> <output file 1>
   <template name2> <output file 2>
   ...
  

where,

 - ``template name`` is user defined name/Id of that specific template. Must correspond to the name defined under the :ref:`j_templates` card.
 - ``output file`` is the path dir + file name to where the cross sections will be written to.


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
This capability is convenient when the user wishes to apply the same template file for multiple universes.
It must be pointed out that if this card is not provided, the explicit definition of universes must be provided within the template files themselves.

*Optional Card*

.. code::
		
   set links
   <template name1> <universe name11> <universe name12> ...
   <template name2> <universe name21> <universe name22> ...
   ...
  

where,

 - ``template name`` is an user defined name/Id of that specific template. Must correspond to the name defined under the :ref:`j_templates` card.
 - ``universe name`` is the user defined universe name or Id.


**Notes:**
	
	*	This card can be omitted.
	*	Each ``template name`` can have a single or multiple ``universe name``.
	* If multiple universes are provided for a specific template then multiple output files will be created. Their naming will differ by the postfix name of the specific universe, e.g. ``output_u0``, ``output_u1`` and so on. 


**Example**:

.. code::

	set links
	template1 u0 u1
	template2 u2


.. _j_serpent:

=======
serpent
=======

**Linkage between user-defined universes and serpent universe Ids defined within the .coe files.**

*Optional Card*


The card allows to specify which universes defined within the serpent files must be read. These Ids are linked to the universe Ids provided by the user.

This card does not have to be provided, in which case the data is expected to be provided directly by the user. Even if the card provided, it can only be specified for selected universes.

The ``serpent`` card can be defined for selected user-defined universes with matching serpent-defined universe Ids. For these original universes the Id will be renamed according to the following rule:


.. code::

	"original univId"+"serpent Id", e.g.,
	"fuel"+"0" will result in "fuel0".
	
There is no need to use the "" marks. 


.. code::
		
   set serpent
   <univ Id1> <serpent universe Id11> <serpent universe Id12> ...
   <univ Id2> <serpent universe Id21> <serpent universe Id22> ...
   ...
  

where,

 - ``univ Id`` is a user defined universe Id, which must be defined in the :ref:`j_universes` card.
 - ``serpent universe Id`` is the serpent defined universes Ids within the .coe files.


**Notes:**
	
	*	This card can be omitted, in which case all the data would be expected to be provided directly by the user.
	*	Each ``univ Id`` can have a single or multiple ``serpent universe Id``.


**Example**:

.. code::

	set universes
	fuel ..\inputsets\fuel
	ref ..\inputsets\reflector

	set serpent
	fuel 0, 1, 2, 3, 4, 5


*	In the example above, it is important to note that the universes ``0``, ..., ``5`` must exist in the .coe files provided within ``..\inputsets\fuel``
* As the ``serpent`` card is defined, the universe Ids for the original ``fuel`` will become ``fuel0``, ..., ``fuel5``
* As the ``serpent`` card does not include the ``ref`` universe, its name still remains ``ref`` universe.
* The definition in the ``links`` card must be consistent with the ``serpent`` one, such that:
	
.. code::

	set links
	template1 fuel0, fuel1, fuel2, fuel3, fuel4, fuel5
	template2 ref


.. _j_shift:

=======
shift
=======

**Linkage between user-defined universes and shift universe Indices defined within the .h5 files.**

*Optional Card*


This card is identical to the :ref:`j_serpent` card with the slight difference in syntax:


.. code::
		
   set shift
   <univ Id1> <shift universe Id11> <shift universe Id12> ...
   <univ Id2> <shift universe Id21> <shift universe Id22> ...
   ...
  
	

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
 - ``var`` denotes a user-defined variable used within the template file, but this can be over-written if the format is specified directly in the template file using  :ref:`varo`.
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


.. _j_map:

====
map
====

Description of the channels radial distribution/map.
**Not required**. 

Create a map the describes the layout for all the channels.
This is useful for post-processing the results and linking the universes to specific channels.

**Syntax**:

.. code::

	set map <idx1> <idx2> ...
	<chId11> <chId12> ...
	<chId21> <chId22> ...
	...
	
**Example**:

.. code::

	set map 0 -1 0	
       S1  S2
     S3  S4  S3 
       S5  S6

	
.. note::

	*	The indices defined in the ``set map`` indicate the location of the first channel in the corresponding row.
	
	* The number of indices and rows must be identical.
	
	* However, indices are not required, and if not given the position of the first channel in the row will be at the origin.
		
	*	In the given example, three rows will be given as three indices are provided. The second row will be shifted to the left (start at -1).	
	
	

.. _j_channels:

========
channels
========

Description of universes in each of the defined channels.
**Not required**. But, if provided the ``set map`` card must also be defined.

.. code::

	set channels
	<ch1> <univ1> <univ2> <univ3> ...
	<ch2> <univ2> <univ2> <univ2> ...
	...
	
**Example**:

.. code::

	set channels
	S1 ref0 fuel0 fuel0 fuel0 fuel0 ref0            
	S2 fuel0 fuel0 fuel0 fuel0 fuel0            
	S3 fuel0 fuel0 fuel0 fuel0 fuel0 fuel0 fuel0           
	S4 fuel0 fuel0 fuel0 fuel0  
	
	
.. note::

	*	The first entry in each row is the name of the channel and should correspond to the channels provided in ``set map``.

	*	The values that follow the name of the channel represent the universes in the different layers. These universes must be defined. 

	*	Each row/channel can contain different number of entries.


.. _j_volumes:

========
volumes
========

Description of universes in each of the defined channels.
**Not required card**. If provided then ``set channels`` must be defined.

.. code::

	set volumes
	<ch1> <vol11> <vol12> <vol13> ...
	<ch2> <vol21> <vol22> <vol23> ...
	...
	
**Example**:

.. code::

	set volumes
	S1 1 1 1 1 1 1        
	S2 1 1 1 1 1            
	S3 1 1 1 1 1 1 1          
	S4 1 1 1 1  
	
	
.. note::

	*	The first entry in each row is the name of the channel and should correspond to the channels provided in ``set map``.

	*	The values that follow the name of the channel represent the volumes of the different layers. 

	*	Each row/channel must contain number of entries corresponding to the number of entries provided in ``set channels``.

	*	If ``set channels`` card is defined and this card is omitted all the volumes are assumed as unity volumes.