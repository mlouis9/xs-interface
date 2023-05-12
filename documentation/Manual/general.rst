.. _general-card:

=======
General
=======

*	Comment lines and section can be set-up 
	using \# and \%. Anything that follows these signs is
	considered as a comment and excluded. 

* Commas to separate between values are allowed but not required.

* The cards themselves are case insensitive and captial letters are internally converted to small letters.

*	A special repetition sign \* can be used to define a
	repition of a certain value.

**Syntax**:

.. code:: 

	STR*N
	
The string ``STR`` will be replicated N times. 

	
	For example:

.. code:: 

	FE*5 
	
and 

.. code::

	FE FE FE FE FE	

are equivalent. 

.. note::

	The repetition sign \* does not have to be used for all the values, but the star operator will replicate only the string it is adjacent to. The following is allowed:


.. code::

	REF FE*10 ME*5 FE*10 REF

* The special card can also be added with indices which will essentially mimic the operation of a for loop. 

The syntax is:

.. code:: 

	STR*N1[N2, N3]
	
where:

- ``N1`` is the number of times the string ``STR`` will be repeated.
- ``N2`` is the initital intreger assigned to the string STR, and
- ``N3`` is the increment step. Negative steps are allowed as long as it does not result in a negative index assigned to the string. For example, ``FE_*5[3, -10]`` is not allowed. 


	For example:

.. code:: 

	FE_*5[3, 2] 
	
and 

.. code::

	FE_3 FE_5 FE_7 FE_9 FE_11

are equivalent. 


