.. _codeexe:


Code Execution
--------------- 

Import the ``Main`` class from ``xsInterface`` package.

.. code::

	from xsInterface.functions.main import Main

Read the control deck file.

.. code::

	xs = Main("controlDeckFile")

Read universes' data and templates files and populate data.

.. code::

	xs.Read()


Write the data to output files.

.. code::

	xs.Write(writemode)
	
where, ``writemode`` defines the writing mode and can be 'w', 'a', and so on.

``writemode`` can be omitted, in which case the default will be 'w'. e.g.,

.. code::

	xs.Write(writemode='w')


Access Data Directly
-------------------- 

After the execution of ``xs.Read()``, the data can be directly obtained by using two methods.

1. Obtain values for a single universe and multiple parameters/attributes in a table format.

	.. code::
	
		xs.Table(univId, attrs, **kwargs)
		
	where,
	
	- ``univId`` is the universe name. Only a single universe string is allowed to be used.
	- ``attrs`` is a list or string containing the parameters of interest.
	- ``kwargs`` represent the different states (i.e., branches, histories, times) for which data is obtained.
	
	Example:
	
	.. code::
	
		xs.Table("u0", ['inf_rabs', 'beta'], fuel=1500)
		
	or
	
	.. code::
	
		xs.Table("u0", 'beta', fuel=1500, mod=600, time=0.0, history='nom')

2. Obtain values for a single universe and single attribute in a dictionary format.


	.. code::
	
		xs.Values(univId, attr, **kwargs)
		
	where, the parameters are identical to the ones used by the ``Table`` method, but the ``attr`` that can only be a single string describing a single attribute. 
		
	Examples:
	
	.. code::
	
		xs.Values("u0", 'inf_rabs', fuel=1500)
		
	or
	
	.. code::
	
		xs.Values("u0", 'beta', fuel=1500, mod=600, time=0.0, history='nom')
	
