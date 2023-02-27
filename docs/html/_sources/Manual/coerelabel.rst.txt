.. _coerelabel:


Relabel .coe files
------------------ 

A simple pre-procesing tool to convert the .coe file to be readable by the ``xsInterface`` package.


=========
Execution
=========

Requires to import using the following command:

	.. code::
			
			from xsInterface.functions.relabelcoe import coeRelabel


The actual run is performed using the next command line:


	.. code::
			
   		coeRelabel(origCoeFile, modCoeFile, inpLabels)


where,

- ``origCoeFile``: [string] full path to the original (and existing) .coe file.
- ``modCoeFile``: [string] name of the modified .coe file
- ``inpLabelsFile`` : [string] Config file with description of the labels.


=========================
Configuration Labels File
=========================

An additional label configuration file must be provided.
It can be any txt file, where each line describes
the original and modified labels in the following manner.

   <original label>  <modified label>

The ``original label`` is used in Serpent to generate the individual
perturbation/branching states. The ``modified label`` is broken to separate
strings, each describing a certain perturbation.


**Example**:


	.. code::
			
	  f600b0dens630        f600 b0 dens630
	  f600b0densNom        f600 b0 nom
	  f600b0dens780        f600 b0 dens780
	  f600bNomdens630      f600 nom dens630
	  f600bNomdensNom      f600 nom nom
	  f600bNomdens780      f600 nom dens780
	  f600b2250dens630     f600 b2250 dens630
	  f600b2250densNom     f600 b2250 nom
	  f600b2250dens780     f600 b2250 dens780


**Instructions**:

- For the modified labeling use patterns,
  e.g. ``f600``, ``f1500`` as these are needed for gcwrite
- The number of columns in each row must be identical.
- The first column describes the original labels.
  Each column that follows describes a specific perturbation. Be consistent.
  More specifically, if the second column represents the fuel temperature, this
  perturbation should always be present in the same column.
- The nominal branch must be denoted by a specific string (e.g. nom).
- Lines with spaces are allowed.

**Monitored errors** (the function should alert):

- If the original .coe file or label file do not exist.
- If no perturbations exist in the label file.
- If the modified labeling is not specified in the labels file.
- If the labeling used in the original Seprent execution is repetitive,
  i.e. same branch appears multiple times.
- If the modified labeleing repetitive.
- If the modified labels do not create a square matrix. More specifically, if
  the number of perturbation states include 4 fuel temperature,
  3 coolant densities, and 3 levels of ppm-Boron, then a total pf 36 unique
  perturbation points must be provided. The function should identify this
  potential error.

A full example is provided in the ``example`` directory (see ``ex_relabelcoe.py``).


============
Full Example
============


	.. code::

		from xsInterface.functions.main import Main
		from xsInterface.functions.relabelcoe import coeRelabel
		
		# Define input files
		inputFile = "./controlDict"
		coeRelabelFile = "./branchLabels"
		coeOrigFile = "./combTest2.i.coe"
		
		# This file will be used in controlDict
		coeModFile = "./u0.coe"
		
		# create a modified .coe file with branches relabeled to a readable
		# xsInterface format
		coeRelabel(origCoeFile=coeOrigFile,
		           modCoeFile=coeModFile,
		           inpLabels=coeRelabelFile)
		
		
		# Read the control dict
		xs = Main(inputFile)
		
		# Read xs data and templates and populate data
		xs.Read()
		
		# Write data to txt files
		xs.Write()