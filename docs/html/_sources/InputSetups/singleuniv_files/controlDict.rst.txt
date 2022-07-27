.. _single_controldeck:

Control Deck
------------

The file below shows a complete example of a control deck file with the following information:

- A single universe file (denoted as ``u0``) and the path provided within the ``set universes`` card.
- Three template files denoted as ``template0``, ``template1``, and ``template2`` with complete path.
- Three ouput files (with full path) that will be linked to the three provided template files.
- The ``links`` set card links the universes to be used for each template and output file. If the ``links`` set card is defined an explicit Id of the universes should NOT be included in the template files. If the card is not defined the template files must include the universe Id when the "values" rule is used.
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
	u0 .\inputsets\inp2\u0
	
	
	# -----------------------------------------------------------------------------
	#                            TEMPLATE FILES
	# -----------------------------------------------------------------------------
	
	set templates
	template0 .\inputsets\inp2\template0
	template1 .\inputsets\inp2\template1
	template2 .\inputsets\inp2\template2
	
	# -----------------------------------------------------------------------------
	#                            OUTPUT FILES
	# -----------------------------------------------------------------------------
	
	set outputs
	template0 .\inp2\output0_
	template1 .\inp2\output1_
	template2 .\inp2\output2_
	
	
	# -----------------------------------------------------------------------------
	#                           UNIVERSE-TO-FILES LINKS 
	# -----------------------------------------------------------------------------
	
	set links
	template0 u0
	template1 u0
	template2 u0
	
	# -----------------------------------------------------------------------------
	#                            FORMAT
	# -----------------------------------------------------------------------------
	
	set formats 8 .dat
	state 5.5f
	attr 6.6e
	var d