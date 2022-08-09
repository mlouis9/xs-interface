.. _serpent_controldeck:

Control Deck
------------

The file below shows a complete example of a control deck file with the following information:

- Two universes (i.e., ``fuel`` and ``ref``) in the ``set universes`` card.
- A single template file denoted as ``template`` with complete path.
- Single output file (with full path) that will be linked to the two universes.
- ``serpent`` card that defines the serpent universe Id to be linked to the universe Ids defined by the user.
- The ``links`` set card links the universes to be used for each template and output file. Please note that ``fuel0`` and ``ref0`` are used instead of ``fuel`` and ``ref`` as here the user-defined and serpen-defined universes are merged to form new universe Ids.
- The format rules to be used here are defined in the ``formats`` set card.

	- The output files will have postfix named .dat.
	- Maximum of 8 values will be written in each row that contains the "values" rule.
	- The formats for a state, attr, and var parameters are ``5.5f``, ``6.6e``, and ``d`` respectively. It is important to note that the format for any ``var`` can, and sometimes should, be overwritten using the ``<>`` capability within the template files themselves.

.. code::


	# -----------------------------------------------------------------------------
	#            CONTROL DICT
	# -----------------------------------------------------------------------------
	
	
	
	# -----------------------------------------------------------------------------
	#                            FILES TO READ
	# -----------------------------------------------------------------------------
	
	
	set universes
	fuel .\inp3\fuel
	ref .\inp3\ref
	
	
	# -----------------------------------------------------------------------------
	#                            Serpent output files
	# -----------------------------------------------------------------------------
	
	
	set serpent
	fuel 0
	ref 0
	
	
	# -----------------------------------------------------------------------------
	#                            TEMPLATE FILES
	# -----------------------------------------------------------------------------
	
	set templates
	template0 .\inp3\template0
	
	
	# -----------------------------------------------------------------------------
	#                            OUTPUT FILES
	# -----------------------------------------------------------------------------
	
	set outputs
	template0 .\inp3\output_
	
	# -----------------------------------------------------------------------------
	#                           UNIVERSE-TO-FILES LINKS 
	# -----------------------------------------------------------------------------
	
	set links
	template0 fuel0 ref0
	
	# -----------------------------------------------------------------------------
	#                            FORMAT
	# -----------------------------------------------------------------------------
	
	set formats 8 .dat
	state 5.5f
	attr 6.6e
	var d