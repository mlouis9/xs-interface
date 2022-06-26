.. _multiplesets_example:


MultipleSets
============

Example on how to collect, store, and process data using the
``MultipleSets`` container.

.. code:: python

       ms = (macro=True, micro=False, kinetics=False, meta=False)

Class Description
-----------------

**Parameters**

-  states : Perturbations object an object with perturbation states
   including branches, history, and time parameters.
-  macro : bool flag to incdicate if all data in macro must be defined
-  micro : bool flag to incdicate if all data in micro must be defined
-  kinetics : bool flag to incdicate if all data in kinetics must be
   defined
-  meta : bool flag to incdicate if all data in meta must be defined

**Attributes**

-  setIds : list of strings complete list of strings for all the sets to
   be provided.
-  macro : bool flag to incdicate if all data in macro must be defined
-  micro : bool flag to incdicate if all data in micro must be defined
-  kinetics : bool flag to incdicate if all data in kinetics must be
   defined
-  meta : bool flag to incdicate if all data in meta must be defined
-  sets : dict keys are indices and values are ``SingleSet`` objects.
-  nsets : int number of ``SingleSet``\ s on the ``MultipleSets``
   object.
-  states : dict description of all the perturbation states.
-  setsmap : dict link between the nametuples that describe the state
   and indices in the ``sets`` dict.

**Methods**

.. code:: python

   -----------------------------------------------------------
       Add(*argv)
   -----------------------------------------------------------

*Add a single set data object*

-  argv : non-named arguments non-keyworded variable length argument
   list. Each argument represents a ``SingleSet`` object that contains
   all the required attributes, e.g. ``macro`` and ``meta``.

.. code:: python

   -----------------------------------------------------------
       Get(setIdx=None, branch=None, time=None, history=None,
           errFlag=False)
   -----------------------------------------------------------

*get a SingleSet object for a specific state* - setIdx : int
index/position of the set in the sets dictionary - history : array
values that represent a history - time : float/number value of the time
point - branch : array set of values for the specific branch - errFlag :
boolean indicates whether error should be raised if state not found

.. code:: python

   -----------------------------------------------------------
       Condense(cutoffE)
   -----------------------------------------------------------

*Energy condensation method* - cutoffE : 1-dim array energy cutoffs

.. code:: python

   -----------------------------------------------------------
       Manipulate(modes, attrs, attrs1, attrs2)
   -----------------------------------------------------------

| *Mathematical operation between two attributes* - modes : string or
  list of strings types of the mathematical relation [“multiply”,
  “divide”, “add”, “subtract”] - attrs : string or list of strings
  name/ss of attribute/s where results will be written to.
| - attrs1 : string or list of strings names of attributes type-1 (can
  be macro or micro) - attrs2 : string or list of strings names of
  attributes type-2 (can be macro or micro)

.. code:: python

   -----------------------------------------------------------
       DataTable(attrs=None, macroFlag=None, microFlag=None,
                 kineticsFlag=None, metaFlag=None)
   -----------------------------------------------------------

*a table with existing states and values for all attributes*\  Loops
over the ``MultipleSets`` object to collect all existing states and
values for a specific attribute. - attrs : string or list of strings
name of existing fields/attributes within a ``SingleSet`` object -
macroFlag : boolean, default is True flag to indicate if all macro
attributes are included in the table - microFlag : boolean, default is
True flag to indicate if all micro attributes are included in the table
- kineticsFlag : boolean, default is True flag to indicate if all
kinetics attributes are included in table - metaFlag : boolean, default
is False flag to indicate if all meta attributes are included in the
table

.. code:: python

   -----------------------------------------------------------
       Values(attrs=None, **kwargs)
   -----------------------------------------------------------

*Obtain the values of the specific attribute across different states*\ 
- attrs : string, list of strings name of the attributes to be included
in the returned table. If None then all the attributes are returned -
kwargs : named arguments keys represent the data name and value
represent the values. The filtering of data is performed according to
kwargs. The use can filter according to a specific state, time, or
history

.. code:: python

   -----------------------------------------------------------
       CheckFilters(branches=None, histories=None, times=None,
                    attrs=None)
   -----------------------------------------------------------

*Check that data used to filter the multiset container is valid*\  -
branches : dictionary keys represent the names of the branches and
values correspond to the branches values. - histories : list of strigs
names of the histories. If not provided then - times : list or array of
floats time points to be included - attrs : list of strings attributes
to be included

Execution Sequence
------------------

.. code:: ipython3

    from xsInterface.containers.datasettings import DataSettings
    from xsInterface.containers.perturbationparameters import Perturbations
    from xsInterface.containers.singleset import SingleSet
    from xsInterface.containers. import 

**Data Settings**
~~~~~~~~~~~~~~~~~

Define what data needs to be collected.

.. code:: ipython3

    # Reset the data
    rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=False,
                      meta=False, isotopes=[531350, 541350, 922350], nuclides="nd")
    # Add the variables names to be collected
    rc.AddData("macro",
               ["inf_rabs", "inf_nsf", "kappa", "inf_flx"])
    rc.AddData("macro", ["inf_sp0"])

.. code:: ipython3

    rc.macro
    




.. parsed-literal::

    ['inf_rabs', 'inf_nsf', 'kappa', 'inf_flx', 'inf_sp0']



Define Perturbation States
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                           histN=2, histories=["nom", "pert"],
                           timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')
    states.AddBranches(fuel=[600, 900, 1200, 1500],
                       dens=[600, 700, 800],
                       cool=[500, 600])
    states.AddHistories(nom=[900, 700, 550],
                        pert=[950, 750, 600])

Multiple Sets
~~~~~~~~~~~~~

.. code:: ipython3

    ms = (states, macro=True, micro=False, kinetics=False, meta=False)

.. code:: ipython3

    rc.macro




.. parsed-literal::

    ['inf_rabs', 'inf_nsf', 'kappa', 'inf_flx', 'inf_sp0']



Data for Single States
~~~~~~~~~~~~~~~~~~~~~~

State-0
^^^^^^^

.. code:: ipython3

    # Reset and define operation state point
    ss0 = SingleSet(rc, states, fluxName="inf_flx",
                   energyStruct=[10.0E+6, 0.6025, 0.0])
    ss0.AddState([600.0, 600, 500], "nom", time=2.5)
    # macro data
    ss0.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
               kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
    ss0.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

.. code:: ipython3

    rc.macro




.. parsed-literal::

    ['inf_rabs', 'inf_nsf', 'kappa', 'inf_flx', 'inf_sp0']



.. code:: ipython3

    ms.Add(ss0)

.. code:: ipython3

    rc.macro




.. parsed-literal::

    ['inf_rabs', 'inf_nsf', 'kappa', 'inf_flx', 'inf_sp0']



State-1
^^^^^^^

.. code:: ipython3

    # Reset and define operation state point
    ss1 = SingleSet(rc, states, fluxName="inf_flx",
                   energyStruct=[10.0E+6, 0.6025, 0.0])
    ss1.AddState([900.0, 600, 500], "nom", time=2.5)
    # macro data
    ss1.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
               kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
    ss1.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

.. code:: ipython3

    ms.Add(ss1)

State-2
^^^^^^^

.. code:: ipython3

    # Reset and define operation state point
    ss2 = SingleSet(rc, states, fluxName="inf_flx",
                   energyStruct=[10.0E+6, 0.6025, 0.0])
    ss2.AddState([1200.0, 600, 500], "nom", time=2.5)
    # macro data
    ss2.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
               kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
    ss2.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

.. code:: ipython3

    ms.Add(ss2)

Create a table from  Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    pdTable = ms.DataTable(['inf_nsf', 'inf_flx'])

.. code:: ipython3

    pdTable




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>inf_nsf</th>
          <th>inf_flx</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>nom</td>
          <td>2.5</td>
          <td>600.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>1</th>
          <td>nom</td>
          <td>2.5</td>
          <td>900.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>2</th>
          <td>nom</td>
          <td>2.5</td>
          <td>1200.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
          <td>[0.3, 0.4]</td>
        </tr>
      </tbody>
    </table>
    </div>



Create Values from  Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    ms.Values(attrs=["inf_nsf"], fuel=900)




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>inf_nsf</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1</th>
          <td>nom</td>
          <td>2.5</td>
          <td>900.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    ms.Values(attrs=["inf_nsf"], dens=600, cool=500)




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>inf_nsf</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>nom</td>
          <td>2.5</td>
          <td>600.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>1</th>
          <td>nom</td>
          <td>2.5</td>
          <td>900.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>2</th>
          <td>nom</td>
          <td>2.5</td>
          <td>1200.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    ms.Values(attrs=["inf_nsf"], history="nom")




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>inf_nsf</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>nom</td>
          <td>2.5</td>
          <td>600.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>1</th>
          <td>nom</td>
          <td>2.5</td>
          <td>900.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>2</th>
          <td>nom</td>
          <td>2.5</td>
          <td>1200.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    ms.Values(attrs=["inf_nsf"], time=2.5)




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>inf_nsf</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>nom</td>
          <td>2.5</td>
          <td>600.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>1</th>
          <td>nom</td>
          <td>2.5</td>
          <td>900.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
        <tr>
          <th>2</th>
          <td>nom</td>
          <td>2.5</td>
          <td>1200.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.3, 0.4]</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    ms.Values(attrs=["inf_nsf"], time=0.0)




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>inf_nsf</th>
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>
    </div>



Condense in energy
~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    ms1, NG = ms.Condense([0.0])  # 1-group

.. code:: ipython3

    pdTable = ms1.DataTable(['inf_nsf', 'inf_flx'])
    ms1.Values(attrs=["inf_nsf"], time=2.5)




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>inf_nsf</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>nom</td>
          <td>2.5</td>
          <td>600.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.35714285714285715]</td>
        </tr>
        <tr>
          <th>1</th>
          <td>nom</td>
          <td>2.5</td>
          <td>900.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.35714285714285715]</td>
        </tr>
        <tr>
          <th>2</th>
          <td>nom</td>
          <td>2.5</td>
          <td>1200.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.35714285714285715]</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    NG




.. parsed-literal::

    2



Data manipulation
~~~~~~~~~~~~~~~~~

.. code:: ipython3

    ms2 = ms.Manipulate(["add"], ["new_add"], ["inf_rabs"], ["inf_nsf"])

.. code:: ipython3

    pdTable = ms2.DataTable(['new_add', 'inf_rabs'])
    ms2.Values(attrs=["new_add", "inf_rabs"], time=2.5)




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
          <th>fuel</th>
          <th>dens</th>
          <th>cool</th>
          <th>new_add</th>
          <th>inf_rabs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>nom</td>
          <td>2.5</td>
          <td>600.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.4, 0.6000000000000001]</td>
          <td>[0.1, 0.2]</td>
        </tr>
        <tr>
          <th>1</th>
          <td>nom</td>
          <td>2.5</td>
          <td>900.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.4, 0.6000000000000001]</td>
          <td>[0.1, 0.2]</td>
        </tr>
        <tr>
          <th>2</th>
          <td>nom</td>
          <td>2.5</td>
          <td>1200.0</td>
          <td>600.0</td>
          <td>500.0</td>
          <td>[0.4, 0.6000000000000001]</td>
          <td>[0.1, 0.2]</td>
        </tr>
      </tbody>
    </table>
    </div>



CheckFilters
~~~~~~~~~~~~

.. code:: ipython3

    missingData = ms.CheckFilters({'fuel':[600, 1200], 'mod': [600], 'cool': [500]}, ["nom"], [2.5], ["inf_nsf"])

.. code:: ipython3

    missingData




.. parsed-literal::

    []



.. code:: ipython3

    missingData = ms.CheckFilters({'fuel':[600, 888], 'mod': [600], 'cool': [500]}, ["nom"], [2.5], ["inf_nsf"])

.. code:: ipython3

    missingData




.. parsed-literal::

    [State(history='nom', time=2.5, branch=(888, 600, 500))]



