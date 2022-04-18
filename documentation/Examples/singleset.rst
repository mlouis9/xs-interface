.. _singleset_example:

SingleSet
=========

Example on how to collect, store, and process data using the
``SingleSet`` container.

.. code:: python

   SingleSet(dataSetup, statesSetup, fluxName=None,
             energyStruct=None, relPrecision=REL_PRECISION)

Class Description
-----------------

**Parameters**

-  dataSetup : DataSettings object, an object that defines the data (and
   type) to be collected
-  statesSetup : Perturbations object, an object to store the
   perturbation states including branches, history, and time parameters.
-  fluxName : string, name of the flux variable on the ``datasets``
   object.
-  energyStruct : array, descending sorted energy structure array.
   Includes the energy structure including the lowest and highest energy
   values. For a two group structure: [E1, E2, E3], where E1 is the
   upper energy bound, E2 is energy cutoff, and E3 is the lowest energy
   bound.
-  relPrecision : float, relative precision that is used to find if a
   close perturbation exists

**Attributes**

-  state : dict, describes the state (branch, time, history)
-  macro : dict, names and values of macro data
-  micro : dict, names and values of micro data
-  kinetics : dict, names and values of kinetics data
-  meta : dict, names and values of meta data

**Methods**

.. code:: python

       AddState(branch, history=None, timeIdx=None, timePoint=None)

*describes the state (branch, time, history)*

-  branch : array, set of values to describe a specific branch-off
   e.g. [Tf, Tm]=[900, 600]
-  history : string, the name of the history
-  timeIdx : int, time index
-  timePoint : float, an existing time point. If ``timeIdx`` is defined
   then this is redundant

.. code:: python

       GetValues(attributes)

*get data for specific attribute/s* - attributes : str or list of
strings, names of the attributes

.. code:: python

       Condense(cutoffE)

*Energy condensation method*\  Condensation is performed for a new
energy structure and for all the parameters in the macro and micro
dictionaries. - cutoffE : 1-dim array, energy cutoffs

.. code:: python

       ProofTest(macro=True, micro=True, kinetics=True, meta=True)

*Check that all data was inputted*\  - macro : bool, flag to incdicate
if all data in macro must be defined - micro : bool, flag to incdicate
if all data in micro must be defined - kinetics : bool, flag to
incdicate if all data in kinetics must be defined - meta : bool, flag to
incdicate if all data in meta must be defined

Execution Sequence
------------------

.. code:: 

    from xsInterface.containers.datasettings import DataSettings
    from xsInterface.containers.perturbationparameters import Perturbations
    from xsInterface.containers.singleset import SingleSet

**Data Settings**
~~~~~~~~~~~~~~~~~

Define what data needs to be collected.

.. code:: 

    # Reset the data
    rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                      meta=True, isotopes=[531350, 541350, 922350])
    # Add the variables names to be collected
    rc.AddData("macro",
               ["inf_rabs", "inf_nsf", "kappa", "inf_flx"],
               [1, 1, 1, 1])
    rc.AddData("macro", ["inf_sp0"], [2])
    rc.AddData("kinetics", ["beta", "decay"])
    rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"])
    rc.AddData("micro", ["sig_sct"], [2])
    rc.AddData("meta", ["burnup", "keff"], [1, 1])
    rc.AddData("meta", ["date"])

Define Perturbation States
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

    states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                           histN=2, histories=["nom", "pert"],
                           timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')
    states.AddBranches(fuel=[600, 900, 1200, 1500],
                       dens=[600, 700, 800],
                       cool=[500, 600])
    states.AddHistories(nom=[900, 700, 550],
                        pert=[950, 750, 600])

Data for a Single State
~~~~~~~~~~~~~~~~~~~~~~~

Reset and define operation state point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: 

    ss = SingleSet(rc, states, fluxName="inf_flx",
                   energyStruct=[10.0E+6, 0.6025, 0.0])
    ss.AddState([600.001, 600, 500], "nom", timePoint=2.5)

Add macro data
^^^^^^^^^^^^^^

.. code:: 

    ss.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
               kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
    ss.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

Add micro data
^^^^^^^^^^^^^^

.. code:: 

    ss.AddData("micro", sig_c=[[1, 1], [2, 2], [3, 3]])
    ss.AddData("micro", sig_sct=[[11, 12, 21, 22], [11, 12, 21, 22],
                                 [11, 12, 21, 22]])

Add kinetics data
^^^^^^^^^^^^^^^^^

.. code:: 

    ss.AddData("kinetics", beta=[1, 1, 1, 1, 1, 1, 1],
               decay=[1, 1, 1, 1, 1, 1, 1])

Add meta data
^^^^^^^^^^^^^

.. code:: 

    ss.AddData("meta", burnup=[1, 1, 1, 1],
               keff=[1, 1, 1, 1], date="April 09, 2022")

Check that all the data was properly defined
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: 

    ss.ProofTest(micro=False, kinetics=False, meta=False)

Get values
^^^^^^^^^^

.. code:: 

    ss.GetValues(["inf_flx", "beta"])




.. parsed-literal::

    {'inf_flx': array([0.3, 0.4]), 'beta': array([1, 1, 1, 1, 1, 1, 1])}



Energy condensation
^^^^^^^^^^^^^^^^^^^

.. code:: 

    ss1 = ss.Condense([0.6025])

