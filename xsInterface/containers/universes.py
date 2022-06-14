# -*- coding: utf-8 -*-
"""universes

Container to collect and store ``MultipleSets``.

Created on Mon June 13 21:20:00 2022 @author: Dan Kotlyar
Last updated on Mon June 13 21:20:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 04/14/2022 - DK
addset - 04/14/2022 - DK
Need to add error checking!!!

"""

from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.multiplesets import MultipleSets
from xsInterface.errors.checkerrors import _isstr, _isobject


class Universes():
    """A container unique MultipleSets objects

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
    AddUniverse : add new multiset object
    GetUniverse : obtain the object for a specific node

    """

    def __init__(self):
        # Init to empty dictionary
        
        self.universeIds = []  # names of all the universes
        self.universes = {}  # empty dictionary to store all universes


    def Add(self, univId, rc, states, multisets):
        """Add new data for a specific set

        The ``addset`` method allows to add  a ``SingleSet`` object
        with all its attributes to the ``MultipleSets`` object.
        The ``addset`` creates a new attribute with a name that
        corresponds to the single set Id.

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
        ValueError
            If ``univId`` already exists.

        Examples
        --------
        >>> univs = Universes()
        >>> univs.AddUniverse("u0", rc0, states0, multisets0)


        """

        # check variables types
        _isstr(univId, "Universe")
        if univId in self._universeIds:
            raise ValueError("Universe <{}> exists.".format(univId))
            
        _isobject(rc, DataSettings, "Data settings")
        _isobject(states, Perturbations, "Perturbation states")
        _isobject(multisets, MultipleSets, "Multiple Sets")

        # assign data
        self.universes[univId] = (rc, states, multisets)
        self.universeIds = self.universes.keys()  # names for all universes

    def Get(self, univId):
        """Obtains the SingleSet object for a specific set Id

        Parameters
        ----------
        univId : string
            identifier of the universe

        Returns
        -------
        Multisets object

        Raises
        ------
        TypeError
            If the ``univId`` is not str.
        KeyError
            If ``univId`` is not in the ``universes`` dict.

        Examples
        --------
        >>> univs = Universes()
        >>> univs.AddUniverse("u0", rc0, states0, multisets0)
        >>> ms.Get("u0")

        """
        # check variable type
        _isstr(univId, "Universe Identifier")
        return self.universes[univId]

    def __getitem__(self, univId):
        return self.universes[univId]

    def getvalues(self, univId, pty):
        """Obtain the values of the specific property for a given node

        The method obtains the values across all the radial regions for a
        specific channel-layer set.

        Parameters
        ----------
        channel : str
            identifier of the channel
        layer : int
            identifier of the axial layer
        pty : str
            name of the property

        Returns
        -------
        vals : float, str, list or ndarray
            values for the property across multiple spatial regions

        Raises
        ------
        TypeError
            If ``channel`` is not str and ``layer`` is not int.
        KeyError
            If the node (channel, layer) does not exist.
        AttributeError
            If the property ``pty`` does not exist.

        Examples
        --------
        >>> inputs.getvalues('A1', 1, 'Q')
        3000

        """

        pass
