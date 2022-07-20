.. _user-manual:


User's Manual
=============

The User\'s Manual for the ``xsInterface`` package describes the 
various inputs required by the code and its various applications. 
The User\'s Manual also describes the printed output options as well as the embedded post-processing capabilities. 
Input examples are provided for the main applications to assist in the preparation of new problems.

The following table describes all the components to understand how to set and handle:

- Control deck file.
- Multiple files that define data definition for each unique cross-section set. These files include multiple input cards to define andd manipulate the data.
- Template files.

===================== ============================================
Chapters							Description
===================== ============================================
:ref:`controldeck`		Modes of executions
--------------------- --------------------------------------------
:ref:`universecards`	Inputs cards necessary to set an input file for a unique XS set.
--------------------- --------------------------------------------
:ref:`codeexe`				Modes of executions
--------------------- --------------------------------------------
:ref:`processres`		  Results post-processing features.
===================== ============================================


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   controldeck
   input_cards
   code_exe
   process_results


Data Flow Sequence
------------------

1. Define all the universe files with cross-section data.
2. Define all the template
3. Define the control deck with the universe- and template-files includes within.
4. Read the deck file; the code will automatically proceed by reading all the templates and universes files.


.. role:: underline
    :class: underline




	
