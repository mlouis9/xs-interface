# -*- coding: utf-8 -*-
"""multiplesets

Container to collect and store ``SingleSet``s.
It also includes processing of data, such as:
    - Intersecting aspecific values over multiple single sets.
    - Spatial homogenization.
    - COMPLETE



Created on Thu Apr 14 05:45:00 2022 @author: Dan Kotlyar
Last updated on Fri Apr 15 05:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 04/14/2022 - DK
addset - 04/14/2022 - DK

"""

from xsInterface.containers.singleset import SingleSet
from xsInterface.errors.checkerrors import _islist, _isuniquelist, _isstr,\
    _isobject, _inlist, _isbool


class MultipleSets():
    """A container to store the input data for all the data sets

    Attributes
    ----------
    names : list of strings
        complete list of strings for all the sets to be provided.

    Attributes
    ----------
    setIds : list of strings
        complete list of strings for all the sets to be provided.
    macro : bool
        flag to incdicate if all data in macro must be defined
    micro : bool
        flag to incdicate if all data in micro must be defined
    kinetics : bool
        flag to incdicate if all data in kinetics must be defined
    meta : bool
        flag to incdicate if all data in meta must be defined

    Methods
    -------
    AddSet : add new nodal object
    GetSet : obtain the object for a specific node
    GetValues : obtain values of a specific property

    """

    def __init__(self, names, macro=False, micro=False, kinetics=False,
                 meta=False):
        # Init to empty dictionary
        _islist(names, "Complete list of sets' names")
        _isuniquelist(names, "Complete list of sets' names")
        _isbool(macro, "Macro flag")
        _isbool(micro, "Micro flag")
        _isbool(kinetics, "Kinetics flag")
        _isbool(meta, "Meta flag")

        self._setsIds = names  # store names/Ids
        self.sets = {}  # empty dictionary to store all sets
        self._flags = {"macro": macro, "micro": micro, "kinetics": kinetics,
                       "meta": meta}

    def AddSet(self, setId, setData):
        """Add new data for a specific set

        The ``addset`` method allows to add  a ``SingleSet`` object
        with all its attributes to the ``MultipleSets`` object.
        The ``addset`` creates a new attribute with a name that
        corresponds to the single set Id.

        Parameters
        ----------
        setId : string
            identifier of the set
        specific : SingleSet object
            an object that contains all the attributes, e.g. ``macro``

        Raises
        ------
        TypeError
            If the ``setId`` is not str.
            If ``setData`` is not a ``SingleSet`` object.
        KeyError
            If ``setId`` is not defined in the ``setIds`` list.
            If ``setId`` already exists in the ``sets`` dict.
        ValueError
            If ``SingleSet`` is not fully populated with data.

        Examples
        --------
        >>> ms = MultipleSets(["u0", "u1"])
        >>> ms.AddSet("u0", ss0)


        """

        # check variable type
        _isstr(setId, "Set Identifier")
        _inlist(setId, "Set Identifier", self._setsIds)
        _isobject(setData, SingleSet, "Single Set Data")
        # check if setId already exist
        if setId in self.sets:
            raise KeyError("Set Id {} already exists".format(setId))
        # internal method to check that data was provided
        setData.ProofTest(self._flags["macro"], self._flags["micro"],
                          self._flags["kinetics"], self._flags["meta"])
        # assign data
        self.sets[setId] = setData

    def GetSet(self, setId):
        """Obtains the SingleSet object for a specific set Id

        Parameters
        ----------
        setId : string
            identifier of the set

        Returns
        -------
        SingleSet object

        Raises
        ------
        TypeError
            If the ``setId`` is not str.
        KeyError
            If ``setId`` is not in the ``sets`` dict.

        Examples
        --------
        >>> ms = MultipleSets(["u0", "u1"])
        >>> ms.AddSet("u0", ss0)
        >>> ms.AddSet("u0")

        """
        # check variable type
        _isstr(setId, "Set Identifier")
        return self.sets[setId]

    def __getitem__(self, setId):
        return self.sets[setId]

    def getvalues(self, channel, layer, pty):
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

        self._checknode(channel, layer)

        # Routine to collect results
        node = NodeID(channel, layer)
        return self._nodes[node].get(pty)
