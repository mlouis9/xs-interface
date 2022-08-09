.. _serpent_ref0:


Reflector Universe Data
-----------------------

The following data file defines a complete set for the following states:

- 2 history points
- 1 time points
- 4 fuel branches
- 3 boron branches
- 3 dens branches

Some **important notes**:

- Only macro and kinetics data attributes are defined in the ``settings`` card.
- Data is read from Serpent branch files for two history branches (i.e., ``nom``, ``pert``) defined both in the <set serpent> and <set histories> cards.
- Branch labels that describe how the branches appear in the .coe files is provided by the <set labels> card. The order and number of entries for each branch is consistent with the ``branches`` card.
- The ``serpent`` card also defines the time points defined in <set times> to act as time points (not burnup) because of the positive (+1) entry. Negative value would indicate burnup points.
- A separate data point for a specif state (defined by the single ``set data infFlx 10.0E+6, 0.6025, 0.0`` overwrites a state read by Serpent. This is done here to demonestrate a capability of mixing Serpent- and user-defined states.



.. code::


	# -----------------------------------------------------------------------------
	#            INPUT EXAMPLE FOR A SINGLE CROSS SECTION TYPE
	# -----------------------------------------------------------------------------
	
	
	# -----------------------------------------------------------------------------
	#                            SETTINGS
	# -----------------------------------------------------------------------------
	
	
	set settings 2 9
	macro =  infKappa, infSp0, cmmTranspxs, infFlx
	kinetics =  lambda
	
	# -----------------------------------------------------------------------------
	#                            STATES
	# -----------------------------------------------------------------------------
	
	set branches 3
	fuel 600, 900, 1200, 1500
	boron 0.0, 500.0, 2250.0 
	dens 630.0, 700.0, 780.0 
	
	
	set histories 2
	nom 1000, 750, 710
	pert 1200, 500, 650
	
	set times nounits
	0.0
	
	
	# -----------------------------------------------------------------------------
	#                            DATA
	# -----------------------------------------------------------------------------
	
	# READ BY: SERPENT FILES
	
	set labels 3
	fuel f600, nom, f1200, f1500
	boron b0, nom, b2250 
	dens dens630, nom, dens780 
	
	
	# -----------------------------------------------------------------------------
	#                            PERTURBATIONS
	# -----------------------------------------------------------------------------
	
	
	set data infFlx 10.0E+6, 0.6025, 0.0
	#-------------
	block state
	#----------
	branch 900.0, 500.0, 630.0
	history nom
	time 0.0
	#-------------
	block macro
	#----------
	infKappa 0.1, 0.2
	cmmTranspxs 0.3 0.4
	infFlx 0.1 0.2
	infSp0 = 0.1  0.2 -0.05, 0.3
	
	#-------------
	block kinetics
	#-------------
	lambda 1, 1, 1, 1, 1, 1, 1, 1, 1
	
	
	
	# -----------------------------------------------------------------------------
	#                         .COE SERPENT FILES
	# -----------------------------------------------------------------------------
	
	set serpent 2 +1 infFlx 10.0E+6, 0.6025, 0.0
	nom  .\inp3\ref_nom.coe
	pert .\inp3\ref_pert.coe
	
	
	# -----------------------------------------------------------------------------
	#                         DATA MANIPULATION
	# -----------------------------------------------------------------------------
	
	# n/a
	
	
	# -----------------------------------------------------------------------------
	#                         FILTER DATA & PRINT
	# -----------------------------------------------------------------------------
	
	
	# n/a

