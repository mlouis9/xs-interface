# -*- coding: utf-8 -*-
"""universes

Container to collect and store ``MultipleSets``.

Created on Mon June 13 21:20:00 2022 @author: Dan Kotlyar
Last updated on Mon July 18 12:30:00 2022 @author: Dan Kotlyar

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

Need to add error checking!!!

"""

import numpy as np

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
        self.filteredtates = {}  # empty dict to store states & data for print

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
        

    def Values(self, univId, attr, **kwargs):
        """Obtain the values of a single attribute and corresponding states

        This method is similar to the ``TableValues``, but can only be applied
        for a single attribute. This method returns a clean dictionary with
        occurances of all the states and the specific attribute result.


        Parameters
        ----------
        univId : string
            name of the universe
        attr : string
            name of the attribute
        kwargs : named arguments
            keys represent the state name and value represent the values.
            The filtering of data is performed according to kwargs.

        Returns
        -------
        history : array
            

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
        >>> univs.Values("u0", attrs='inf_nsf', dens=600, cool=500, fuel=900)
        ... history  time  ...                   beta                  decay
        ... 0    None   2.5  ...  [1, 1, 1, 1, 1, 1, 1]
        ... 1    None   2.5  ...  [2, 2, 2, 2, 2, 2, 2]  [1, 1, 1, 1, 1, 1, 1]

        """

        _isstr(attr, "Attribute name")
        pd = self.TableValues(univId, attr, **kwargs)
        pdDict = pd.to_dict()
        
        results = {}  # returned dictionary with states and attribute values
        
        # handle the attribute results separately
        attrDict = pdDict.pop(attr)
        # dims = attrDict[0].shape  # attribute dimensions (vector, matrix)
        arr = [None]*len(attrDict)
        for index, val in attrDict.items():
            arr[index] = val
        results[attr] = arr   
        
        # handle the states(history, time, and branches)
        for key, valsDict in pdDict.items():
            arr = [None]*len(valsDict)
            for index, val in valsDict.items():
                arr[index] = val
            results[key] = np.array(arr)

        return results

        
            
    
        