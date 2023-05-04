.. _postprocess:


Post process
------------ 

After the execution of ``xs.Read()``, the data can be directly obtained by using multiple methods.

========================= ============================================
Method							   		 Description
========================= ============================================
:ref:`p_table`			      Values presented in a table (pandas) format
------------------------- --------------------------------------------
:ref:`p_values`	          Values presented in a dictionary format.
------------------------- --------------------------------------------
:ref:`p_corevalues`	 			Values for radial channels & layers
========================= ============================================


.. _p_table:

=========
Table
=========


**Obtain values for a single universe and multiple parameters/attributes in a table format**.

**Syntax:**

.. code::

	xs.Table(univId, attrs, **kwargs)
		
where,

- ``univId`` is the universe name. Only a single universe string is allowed to be used.
- ``attrs`` is a list or string containing the parameters of interest.
- ``kwargs`` represent the different states (i.e., branches, history, time) for which data is obtained.

**Example:**

.. code::

	xs.Table("u0", ['inf_rabs', 'beta'], fuel=1500)
	
or

.. code::

	xs.Table("u0", 'beta', fuel=1500, mod=600, time=0.0, history='nom')



.. _p_values:

=========
Values
=========


**Obtain values for a single universe and single attribute in a dictionary format.**

**Syntax:**

.. code::

	xs.Values(univId, attr, **kwargs)
	
where, the parameters are identical to the ones used by the ``Table`` method, but the ``attr`` that can only be a single string describing a single attribute. 
	
**Examples:**

.. code::

	xs.Values("u0", 'inf_rabs', fuel=1500)
	
or

.. code::

	xs.Values("u0", 'beta', fuel=1500, mod=600, time=0.0, history='nom')



.. _p_corevalues:

===========
CoreValues
===========


**Obtain values for multiple attributes and all channels & layers.**


This method returns a dictionary with keys representing attributes
and values that are 2-dim lists representing values across
all channels and layers.

**Syntax:**

.. code::

	xs.CoreValues(attrs, chIds=None, volManip=None, **kwargs)
	
where,

- ``attrs`` is string or list of strings. Name/s of the attribute/s.
- ``chIds`` is a list of strings. List with all the channel names. If None, the results for all the channels are provided.
- ``volManip`` is a string. Volume manipulation that be: 'multiply' or 'divide' or None. Default is None.
- ``kwargs`` represent the different states (i.e., branches, history, time) for which data is obtained.
- ``kwargs`` is named arguments. keys represent the state/branch name and value represent the values

	
**Examples:**

.. code::

	xs.CoreValues(['infkappa', 'infsp0'], 
	             chIds=['S1', 'S2', 'S3', 'S4'], 
	             volManip=None, 
	             history=[['nom', 'nom', 'nom', 'nom']]*4,
	             time=[[0.0, 0.0, 0.0, 0.0]]*4, 
	             fuel=[[900, 900, 900, 900]]*4, 
	             boron=[[0, 0, 0, 0]]*4,
	             dens=[[700, 700, 700, 700]]*4)
	
or

.. code::

	xs.CoreValues('infflx', 
	             chIds=None, 
	             volManip='divide', 
	             history=[['nom', 'nom', 'nom', 'nom']]*4,
	             time=[[0.0, 0.0, 0.0, 0.0]]*4, 
	             fuel=[[900, 900, 900, 900]]*4, 
	             boron=[[0, 0, 0, 0]]*4,
	             dens=[[700, 700, 700, 700]]*4)