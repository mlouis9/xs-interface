.. _codeexe:


Code Execution
--------------- 

Import the ``Main`` class from ``xsInterface`` package.

.. code::

	from xsInterface.functions.main import Main

Read the control deck file.

.. code::

	xs = Main(inputfile)

Where, ``inputfile`` is the name of the controlDict file (e.g., "controlDeckFile")

If the results were previously saved using the :ref:`e_store` method then these can be loaded using the same execution:

.. code::

	xs = Main(inputfile)
	
but in this case ``inputfile`` must be an existing pickle file (e.g., "xsdata.pkl")


Read universes' data and templates files and populate data.

.. code::

	xs.Read()

The ``Read method`` has some flexibility in filtering what data to read and what data to read.

**Syntax:**

.. code::

	xs.Read(readUniverses, readTemplate, readMapTemplate)
	
where,

- ``readUniverses`` (boolean) indicates whether cross sections for all the universes should be read. The defualt is True.
- ``readTemplate`` (boolean) indicates whether template files should be read. Default is False. This is useful if the data is not written anywhere but rather just read.
- ``readMapTemplate`` (boolean) indicates whether the data should be read for each channel and layer, which might contain the same universes. Default is False.
- ``readTemplate`` and ``readMapTemplate`` cannot be both True. If they are, then reading and data storing is performed according to ``readMapTemplate=True`` and  ``readTemplate=False``.


**Example 1:** Read only the universes data.

.. code::

	xs.Read(readUniverses=True)


**Example 2:** Read cross section data and templates and populate data for each channel and layer.

.. code:: 

	xs.Read(readUniverses=False, readTemplate=True, readMapTemplate=True)




//////////////////////////////////////////////////////////////////





Manipulation methods
--------------------

After the execution of ``xs.Read()``, the data can be manipulated and presented using different methods. 

========================= ============================================
Method							   		 Description
========================= ============================================
:ref:`e_write`			      Write data to a user-defined template
------------------------- --------------------------------------------
:ref:`e_store`			      Store data to a pickle (binary) file
------------------------- --------------------------------------------
:ref:`e_condense`	        Perform energy condensation.
========================= ============================================


.. _e_write:

=========
Write
=========


**Write the data to output files.**

The data is written according to the :ref:`templates` provided by the user.

**Syntax:**

.. code::

	xs.Write(writemode)
	
where, ``writemode`` defines the writing mode and can be 'w', 'a', and so on.

``writemode`` can be omitted, in which case the default will be 'w'. e.g.,

.. code::

	xs.Write(writemode='w')
	

.. _e_store:

=========
Store
=========


**Store the data already read to a pickle (binary) file.**

The entire object that includes values and object methods is stored. There is no need to execute the ``Read`` method (but it is allowed if needed).

**Syntax:**

.. code::

	xs.Store(file)
	
where, ``file`` is the name (path+file name) of the file to be stored. This file must be a pickle file. If the file does not end with ``.pkl`` it will be auto added by the package.


.. code::

	xs.Store(file='xsdata.pkl')
	
	
.. _e_condense:

=========
Condense
=========	

**Energy condensation method.**

Condensation is performed for a new energy structure and for all the parameters in the macro and micro dictionaries over all existing perturbation states.


**Syntax:**

.. code::

	xs.Condense(cutoffE)
	
where, ``cutoffE`` energy cutoffs used for energy condensation.

**Notes:**
	
*	``cutoffE`` must contain at least one number (which will generate a 2-group or 1-group structure). ``cutoffE`` must be within the energy bounds <ENE> defined in the :ref:`i_data` card.
	* ``cutoffE`` must be provided in descending order. To avoid energy condensation use the same cutoffs as defined in <ENE>.
* A new energy grid will be created based on the provided ``cutoffE`` and closest energy boundaries <ENE> defined in the :ref:`i_data` card.
	* If <ENE> = ``10.0E+6, 0.6025, 0.0`` and <cutoffE> = ``0.005`` then a 1-group ``10.0E+6, 0.0`` will be created.
	* If <ENE> = ``10.0E+6, 0.6025, 0.0`` and <cutoffE> = ``0.6025`` or above then 2-groups ``10.0E+6, 0.6025, 0.0`` will be created.
	* For the provided <ENE> structure if <cutoffE> equals to the outermost left or right boundary a 1-group ``10.0E+6, 0.0`` will be utilized.
	* <cutoffE> cannot create a finer grid than <ENE> regardless to how many ``cutoffE`` boundaries are provided (as no interpolation is used).