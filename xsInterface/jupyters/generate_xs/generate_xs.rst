Generate Cross Sections
=======================

This Notebook demonestrates how to read cross sections from a serpent
``_res.m`` file. The capabilities to store and process the data are also
presented.

Case Description
----------------

The ``.\inputs`` directory includes: - ``bwr_rho1_2gr`` a serpent input
file. This is a 3D BWR assembly divided into 36 layers (i.e., universes
1,2,…,36) of fuel surrounded by a bottom (universe 54) and upper layers
(universe 55) of reflectors. - ``bwr_rho1_2gr_res.m`` a serpent results
file with all the cross sections. - ``univs`` a file that describes how
to read ``bwr_rho1_2gr_res.m`` - ``controlDict`` the main files that is
required by the ``xsInterface``.

Required imports
~~~~~~~~~~~~~~~~

.. code:: ipython3

    from xsInterface.functions.main import Main

.. code:: ipython3

    inputFile = ".\\inputs\\controlDict"

Read the cross sections
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    # Reset the main object
    xs = Main(inputFile)


.. parsed-literal::

    ... Reading control dict ...
    <.\inputs\controlDict>
    
    

Read xs data without populating the templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: ipython3

    xs.Read(readUniverses=True)


.. parsed-literal::

    SERPENT Serpent 2.1.32 found in .\inputs\bwr_rho1_2gr_res.m, but version 2.1.31 is defined in settings
      Attemping to read anyway. Please report strange behaviors/failures to developers.
    

.. parsed-literal::

    ... Reading universe <u> ...
    ... Reading coe/_res.m file for hisotry <nom> ...
    

Process results
~~~~~~~~~~~~~~~

.. code:: ipython3

    xs.Table("u1", ['infnsf', 'infrabsxs'])




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>history</th>
          <th>time</th>
          <th>dens</th>
          <th>infnsf</th>
          <th>infrabsxs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>nom</td>
          <td>0.0</td>
          <td>700.0</td>
          <td>[0.00780015, 0.154742]</td>
          <td>[0.00988701, 0.0895764]</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    xs.Values("u1", 'infnsf')




.. parsed-literal::

    {'history': array(['nom'], dtype='<U3'),
     'time': array([0.]),
     'dens': array([700.]),
     'infnsf': [array([0.00780015, 0.154742  ])]}



.. code:: ipython3

    results = {}
    for i in range(1, 5):
        univId = "u"+str(int(i))
        results[univId] = xs.Values(univId, 'infsp0')

.. code:: ipython3

    results




.. parsed-literal::

    {'u1': {'history': array(['nom'], dtype='<U3'),
      'time': array([0.]),
      'dens': array([700.]),
      'infsp0': [array([[0.517267  , 0.0169944 ],
              [0.00151575, 1.25447   ]])]},
     'u2': {'history': array(['nom'], dtype='<U3'),
      'time': array([0.]),
      'dens': array([700.]),
      'infsp0': [array([[0.518501  , 0.0167034 ],
              [0.00161828, 1.24887   ]])]},
     'u3': {'history': array(['nom'], dtype='<U3'),
      'time': array([0.]),
      'dens': array([700.]),
      'infsp0': [array([[0.518396  , 0.0166698 ],
              [0.00161741, 1.24832   ]])]},
     'u4': {'history': array(['nom'], dtype='<U3'),
      'time': array([0.]),
      'dens': array([700.]),
      'infsp0': [array([[0.517767  , 0.0166212 ],
              [0.00162702, 1.24614   ]])]}}



