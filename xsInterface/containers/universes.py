# -*- coding: utf-8 -*-
"""universes

Container to collect and store ``MultipleSets``.

Created on Mon June 13 21:20:00 2022 @author: Dan Kotlyar
Last updated on Sun Sep 03 19:20:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 04/14/2022 - DK
Add - 06/16/2022 - DK
Get - 06/16/2022 - DK
PandaTables - 06/16/2022 - DK
Values - 06/16/2022 - DK
PrintValues - 07/18/2022 - DK
PandaTables - 07/21/2022 - DK
Condense - 05/03/2023 - DK
Values - 09/03/2023 - DK

Need to add error checking!!!

"""

import numpy as np
import pandas as pd
import itertools

from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.multiplesets import MultipleSets
from xsInterface.errors.checkerrors import _isstr, _isobject


class Universes():
    """A container to store unique universes having MultipleSets objects

    Parameters
    ----------
    settings : DataSettings object
        Complete container with all the data settings.
    states: Perturbations object
        Complete container with names and values of perturbation parameters
    multisets : MultipleSets object
        Complete container with data corresponding to all the states

    Attributes
    ----------
    settings : DataSettings object
        Complete container with all the data settings.
    states: Perturbations object
        Complete container with names and values of perturbation parameters
    multisets : MultipleSets object
        Complete container with data corresponding to all the states

    Methods
    -------
    Add : add new multiset object
    Get : obtain the object for a specific node

    """

    def __init__(self):
        # Init to empty dictionary
        
        self.universeIds = []  # names of all the universes
        self.universes = {}  # empty dictionary to store all universes
        self.filteredstates = {}  # empty dict to store states & data for print
        self.squareattrs = {}  # attributes with square matrices in universes
        
        
    def Add(self, univId, rc, states, multisets):
        """Add new data for a specific set

        The ``Add`` method allows to add  ``MultipleSets`` object
        ``Perturbations``, and ``DataSettings`` objects.
        The ``Add`` creates a new key (that represents the universe Id), and
        values that includes the settings, states description, and data sets.

        Parameters
        ----------
        settings : DataSettings object
            Complete container with all the data settings.
        states: Perturbations object
            Complete container with names and values of perturbation parameters
        multisets : MultipleSets object
            Complete container with data corresponding to all the states

        Raises
        ------
        TypeError
            If the ``univId`` is not str.
            If ``rc`` is not a ``DataSettings`` object.
            If ``states`` is not a ``Perturbations`` object.
            If ``multisets`` is not a ``MultipleSets`` object.

        Examples
        --------
        >>> univs = Universes()
        >>> univs.Add("u0", rc0, states0, multisets0)


        """

        # check variables types
        _isstr(univId, "Universe")
        # if univId in self.universeIds:
        #     raise ValueError("Universe <{}> exists.".format(univId))
            
        _isobject(rc, DataSettings, "Data settings")
        _isobject(states, Perturbations, "Perturbation states")
        _isobject(multisets, MultipleSets, "Multiple Sets")

        # assign data
        self.universes[univId] = (rc, states, multisets)
        self.universeIds = list(self.universes.keys())  # universes names

    def Get(self, univId):
        """Obtains the MultipleSet object for a specific universe

        Parameters
        ----------
        univId : string
            identifier of the universe

        Returns
        -------
        A tuple with (rc, states, multisets)

        Raises
        ------
        TypeError
            If the ``univId`` is not str.
        KeyError
            If ``univId`` is not in the ``universes`` dict.

        Examples
        --------
        >>> univs = Universes()
        >>> univs.Add("u0", rc0, states0, multisets0)
        >>> ms.Get("u0")

        """
        # check variable type
        _isstr(univId, "Universe Identifier")
        return self.universes[univId]

    def __getitem__(self, univId):
        return self.universes[univId]


    def PandaTables(self):
        """Create tables with states and values for all attributes & universes

       Raises
        ------
        TypeError
            If ``attrs`` is not string, list, or None.

        Examples
        --------
        >>> univs.PandaTables()

        """
        
        for univId in self.universeIds:
            rc, states, msets = self[univId]
            if msets.filterstates != {}:
                df = pd.DataFrame()
                fltrs = msets.filterstates
                histories = fltrs['histories']
                times = fltrs['times']
                branchesDict = fltrs['branches']
                attrs = fltrs['attrs']
                msets.DataTable(attrs)
                # filter the data
                brvals = list(branchesDict.values())
                brkeys = list(branchesDict.keys())
                for hist in histories:
                    for time in times: 
                        for branch in itertools.product(*brvals):
                            brdict = {}
                            for idx, key in enumerate(brkeys):
                                brdict[key] = branch[idx]
                            # append the current state to the pd table
                            df =\
                            df.append(msets.Values(None, history=hist,
                                                   time=time, **brdict),
                                      ignore_index=True)
                msets.pandasTable = df  # update the pandas table
            else:
                msets.DataTable()
            
            self.Add(univId, rc, states, msets)


    def TableValues(self, univId, attrs=None, **kwargs):
        """Obtain the values of the specific attribute across different states

        The method obtains the values across all the provided states.
        Specific attributes can be selected. The results are ouputted for a
        specific universe.


        Parameters
        ----------
        univId : string
            name of the universe
        attrs : string, list of strings
            name of the attributes to be included in the returned table.
            If None then all the attributes are returned
        kwargs : named arguments
            keys represent the data name and value represent the values.
            The filtering of data is performed according to kwargs.
            The use can filter according to a specific state, time, or history

        Returns
        -------
        pd : Pandas Object (dataframe)
            states and values across multiple states

        Raises
        ------
        TypeError
            If ``univId`` is not str.
            If ``attrs`` is not str, list of str, or None.
        KeyError
            If ``univId` does not exist.

        Examples
        --------
        >>> univs.Values("u0", attrs=None, dens=600)
        ... history  time  ...                   beta                  decay
        ... 0    None   2.5  ...  [1, 1, 1, 1, 1, 1, 1]  [1, 1, 1, 1, 1, 1, 1]
        ... 1    None   2.5  ...  [2, 2, 2, 2, 2, 2, 2]  [1, 1, 1, 1, 1, 1, 1]

        """

        _isstr(univId, "Universe Identifier")
        rc, states, msets = self[univId]
        return msets.Values(attrs, **kwargs)


    def Condense(self, univId, cutoffE):
        """Energy condensation method

        Condensation is performed for a new energy structure and for all the
        parameters in the macro and micro dictionaries over all existing states
        for this specific universe.

        Parameters
        ----------
        univId : string
            name of the universe
        cutoffE : 1-dim array
            energy cutoffs

        Raises
        ------
        TypeError
            If ``cutoffE`` is not array.
            If ``univId`` is not str.
        ValueError
            If ``cutoffE`` is negative.
            If ``univId` does not exist.

        Examples
        --------
        >>> ss.Condense("u0", [0.0625, 1E+03])

        """

        _isstr(univId, "Universe Identifier")
        
        rc, states, msets = self[univId]
        condMsets, condNg = msets.Condense(cutoffE)
        rc.ng = condNg  # update the number of energy groups
                
        return rc, states, condMsets
        

    def Values(self, univId, attrs, **kwargs):
        """Obtain the values of a single attribute and corresponding states

        This method is similar to the ``TableValues``, but can only be applied
        for a single attribute. This method returns a clean dictionary with
        occurances of all the states and the specific attributes results.
        States are stored in list and attributes values in 2-dim array, where
        the column represents the energy or delayed group and row the state.


        Parameters
        ----------
        univId : string
            name of the universe
        attrs : string or list of strings
            name of the attribute
        kwargs : named arguments
            keys represent the state name and value represent the values.
            The filtering of data is performed according to kwargs.

        Returns
        -------
        results : dict
            dictionary with occurances of all the states and the specific 
            attributes results.
            States are stored in list and attributes values in 2-dim array, 
            where the column represents the energy or delayed group and row 
            the state.
            

        Raises
        ------
        TypeError
            If ``univId`` is not str.
            If ``attrs`` is not str.
        KeyError
            If ``univId` does not exist.
            If ``attr` does not exist.

        Examples
        --------
        >>> universes.Values("u0", attr=["infnsf", "inffiss"], fuel=900)
        ... {'infnsf': array([[0.36666667], [0.36666667]),
        ...  'inffiss': array([[0.36666667], [0.36666667]),                       
        ...  'history': ['nom', 'nom'],
        ...  'time': [0., 0.],
        ...  'fuel': [900., 900.],
        ...  'mod': [600., 600.],
        ...  'cool': [600., 500.]}

        """

        if isinstance(attrs, str):
            attrs = [attrs]

        pd0 = self.TableValues(univId, attrs, **kwargs)
        pdDict = pd0.to_dict()
                
        results = {}  # returned dictionary with states and attribute values
        self.squareattrs[univId] = []
        
        # handle the states(history, time, and branches)
        for key, valsDict in pdDict.items():
            nstates = len(valsDict)
            valsDictKeys = list(valsDict.keys())
            if key in attrs:
                if valsDict[valsDictKeys[0]].ndim == 2:
                    ng = len(valsDict[valsDictKeys[0]][0])  # number of values
                    ng = int(ng*ng)
                    # square matrices (e.g., scattering)
                    if key not in self.squareattrs[univId]:
                        self.squareattrs[univId] = self.squareattrs[univId]+[key]
                    vals = np.empty((nstates, ng))  # reset a matrix
                    for istate, statevals in enumerate(valsDict.values()):
                        vals[istate, :] = statevals.flatten()
                else:
                    ng = len(valsDict[valsDictKeys[0]])  # number of values
                    vals = np.empty((nstates, ng))  # reset a matrix
                    for istate, statevals in enumerate(valsDict.values()):
                        vals[istate, :] = statevals
            else:
                vals = [None]*nstates  # a list to hold states and not attrs
                for istate, statevals in enumerate(valsDict.values()):
                    vals[istate] = statevals
            # assign the attributes to results
            results[key] = vals 
        return results

        