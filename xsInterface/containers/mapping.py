# -*- coding: utf-8 -*-
"""mapping

Container to collect, store, and process universe inputs provided in a map.

First the different channels are created and then the map with all these
channels must be provided. 


Created on Mon May 01 13:00:00 2023 @author: Dan Kotlyar
Last updated on Mon Sep 04 06:15:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu


List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Validate - 05/02/2023 - DK
_reshapeTo1D, _reshapeTo3D - 09/04/2023 - DK

"""


import copy

import numpy as np

from xsInterface.errors.checkerrors import _isstr, _inlist,\
    _is1darray, _inrange, _isequallength, _islist, _compare2lists


ALLOWED_MANIPULATION = ['multiply', 'divide']


class Map:
    """A container to store the input data for all channels

    The data for all the radial channels is included in this container.
    In addition, the radial distribution (map) of the channels is provided.
    Each channel contains the information about the axial distribution.

    Parameters
    ----------
    radmap : 2D list of str
        description of the channels radial distribution/map
        e.g.
        ...   `1` `1` `1`
        ... `2` `3` `3` `2`
        ...   `1` `1` `1`
    idxBounds : 2D list of int
        indices of the start and end position for each row
        e.g. [[-1, 1], [-2, 1], [-1, 1]]
        In the above example [-1, 1] represents the components that correspond
        to columns -1, 0, and 1. For this specific row, three entries will
        be expected in the ``radmap``.
        The entries do not have to start from negative numbers. An alternative
        for the above example is: [[0, 2], [-1, 2], [0, 2]] or
        [[1, 3], [0, 3], [1, 3]]

    Attributes
    ----------
    radmap : 2D list of str
        square matrix with radial distribution of radial channels
        ``None`` represent the lack of a channel.
    chIds : set of strings
        Identifiers/names of all the unique channels.
        Following the above example, the unique channels identifiers are `1`
        and `2`.

    Methods
    -------
    AddChannel : add a new channel object
    GetChannel : obtain a specific channel object
    Validate : post validation to check that all channels are defined properly

    Raises
    ------
    TypeError
        If ``radmap`` or ``idxBounds`` is not a list.
    ValueError
        If the number of entries for each row in ``radmap`` does not allign
        with the starting and ending indices in ``idxBounds``.

    Notes
    -----
    The values passed to ``radmap`` should correspond to exisiting channels
    defined using the ``Channel`` container.

    Examples
    --------
    >>> core = Map([['A'], ['B', 'A', 'B'], ['C']],
    ... [[0, 0], [-1, 1], [0, 0]])

    """

    def __init__(self, radmap, idxBounds):

        # check potential errors
        _islist(radmap, "channels radial map")
        _islist(idxBounds, "bounds of left and right indices")

        if len(radmap) != len(idxBounds):
            raise ValueError("number of rows in radmap {} and idxBounds {} "
                             "must be equal".format(radmap, idxBounds))

        bounds = np.asarray(idxBounds)  # convert from a list
        # Outermost left and right bounds
        maxBounds = bounds.min(), bounds.max()

        # Init a square radial map:
        nrows = len(radmap)  # number of rows
        ncols = maxBounds[1] - maxBounds[0] + 1  # number of columns
        self.radmap = [[None for x in range(ncols)] for y in range(nrows)]
        self.idxmap = copy.deepcopy(self.radmap)
        
        # the left and right bounds must align to the number
        # of values in the corresponding row of the radial map
        for idx, rowVals in enumerate(radmap):
            rowBounds = idxBounds[idx]
            if len(rowBounds) != 2:
                raise ValueError("Only two values (left and right bounds) "
                                 "are expected and not {}".format(rowBounds))

            # check that bounds of each row are within max. bounds
            _inrange(rowBounds[0], "left row bound", maxBounds)
            _inrange(rowBounds[1], "right row bound", maxBounds)

            if rowBounds[1] < rowBounds[0]:
                raise ValueError("Right bound {} cannot be lower than left "
                                 "bound {}".format(rowBounds[1], rowBounds[0]))

            if rowBounds[1] - rowBounds[0] + 1 != len(rowVals):
                raise ValueError("The left/right bounds {} do not match the "
                                 "number of entries {}"
                                 .format(rowBounds, rowVals))

            self.radmap[idx][rowBounds[0] - maxBounds[0]:
                             rowBounds[1] - maxBounds[0] + 1] = rowVals
        self.idxBounds = idxBounds
        # Init to empty dictionary for storing data of a specific channel
        self.channels = {}
        # Identify all the unique channels types
        self.chIds = [] #set() +DK
        for row in radmap:
            self.chIds = self.chIds + row  # +DK
            # self.chIds.update(row)
        self.chIds = list(np.unique(self.chIds))
            
        self.linkChannelsInMap = {}
        self.orderedChIds = []
        c = 0  # the first channel is the zero channel
        for irow, row in enumerate(radmap):
            for jcol, col in enumerate(row):
                self.idxmap[irow][jcol] = c
                # map the channels to their positions
                chId = radmap[irow][jcol]  # get chId in this location
                self.orderedChIds.append(chId)
                if chId in self.linkChannelsInMap:
                    self.linkChannelsInMap[chId] =\
                        self.linkChannelsInMap[chId] + [c]
                else:
                    self.linkChannelsInMap[chId] = [c]                    
                c += 1

        
        # core operational states for the results (not used here directly)
        self.corestates = {}
        # core values for different attributes (not used here directly)
        self.corevalues = {}

    def Channel(self, chId, universes, volumes=None):
        """Add the name, universes and volumes for a specific channel


        Parameters
        ----------
        chId : str
            identifier/name of the channel
        universes : list of strings
            universe for each of the layers in this channels
        volumes : list or array
            volume for each of the layers in this channels       

        Raises
        ------
        TypeError
            If the ``chId`` is not a string.
            If ``universes`` not a list.
        KeyError
            If the channel already exists.
            If the channel Id does not appear in ``radmap``.

        Examples
        --------
        >>> core.Channel("A", ['u0', 'u0', 'u0', 'u0', 'u0'],
                         [1, 1, 1, 1, 1])

        """

        _isstr(chId, "Channel Id")
        if chId not in self.chIds:
            raise ValueError("ChId {} does not exist in {}"
                             .format(chId, self.chIds))
        
        # check that universes are provided as a list
        _islist(universes, "universes")
        
        # check that list is not empty
        nvals = len(universes)
        if nvals == 0:
            raise ValueError("universes cannot be empty.")
        
        # if volume is not provided set to unity volume
        if volumes is None:
            volumes = np.ones(nvals)
        
        # convert to numpy array (if provided as a list)
        volumes = np.array(volumes)

        # arrays' dimensions
        _is1darray(volumes, "volumes")
        
        # number of values in ``volumes``
        _isequallength(volumes, nvals, "volumes")
        
        # check if the channel was already defined
        if chId in self.channels:
            raise ValueError("Channel <{}> already exist.".format(chId))
        
        # assign values to the specific channel
        self.channels[chId] = {"nlayers": nvals,
                               "layers": universes,
                               "volumes": volumes}
            

    def Copy(self, existId, newId):
        """Copy an already existing universe for a new universe Id 


        Parameters
        ----------
        existId : str
            identifier/name of the channel
        newId : list of strings
            universe for each of the layers in this channels
    
        Raises
        ------
        TypeError
            If the ``existId`` or ``newId`` are not strings.
        KeyError
            If the ``existId`` does not exist.
            If the ``newId`` does not already exist.

        Examples
        --------
        >>> core.Copy("A", "C")

        """

        _isstr(existId, "existId")
        _isstr(newId, "newId")
        
        
        if existId not in self.channels:
            raise ValueError("existId {} does not exist in channels {}"
                             .format(existId, self.channels.keys()))

        if newId in self.channels:
            raise ValueError("newId {} already exists in channels {}"
                             .format(newId, self.channels.keys()))        
        
        self.channels[newId] = copy.deepcopy(self[existId])
        

    def __getitem__(self, pos):
        return self.channels[pos]


    def _NumSpatialNodes(self):
        """count the total number of spatial nodes in the system ch x layers"""
        # this method can only be executed if all the fields already exist

        numChannels = 0
        numNodes = 0
        for chId, chData in self.channels.items():
            chs = self.linkChannelsInMap[chId]
            nchs = len(chs)
            chData['channelsIdx'] = chs   # indices
            chData['nchannels'] = nchs    # number of repetitions
            self.channels[chId] = chData  # update the data
            numChannels += nchs
            numNodes += nchs*chData['nlayers']
        self.numNodes = numNodes
        self.numChannels = numChannels



    def _reshapeTo1D(self, valsIn, normFlag=True, weights=None):
        """reshape the 3D matrix to a 1D vector corresponding to radial map
        
        Parameters
        ----------
        self : core Map object
            the object includes data about the channels, layers, ng
            the ``self`` object also includes channels Ids
        valsIn : 1-dim list (with 2-dim arrays)
            input vector with the following structure:
            [channel][layer, energy]
            valsIn are provided in the order of the self.chIds
        normFlag : bool
            indicator whether the returned value should be normalized to 1.
        groupWeights : list
            energy group-wise weighting factors for the objective function.
            Should include a value for each enegy group.
            Envisioned to be used for normalization techniques.
            
        Returns
        -------
        valsOut : 1-dim array
            output vector with the following structure:
            
             gr1, gr-2, ...    gr1, gr-2, ...  gr1, gr-2, ...    gr1, gr-2, ...
            \______________/ \______________/ \______________/ \______________/
                 layer-0         layer-1                      ...
                \___________________________/  \___________________________/
                         channel-0                      channels-N
            
        
        """

        valsChs = [None]*self.numChannels  # total number of channels
        for idxFrom, chId in enumerate(self.chIds):
            # all the parameters that describe the channels
            # nlayers, layers, volumes, channelsIdx, nchannels
            chData = self.channels[chId]
            
            # 1-dim array with all the values for all layers and group
            # layer0 [g0, g1, ...], layer1 [g0, g1, ...], ...
            valsFrom = valsIn[idxFrom]
            
            valsFrom = valsFrom.reshape(valsFrom.shape[0]*valsFrom.shape[1])
            
            # insert the values to the correct channel
            for idxTo in chData['channelsIdx']:
                valsChs[idxTo] = valsFrom
            
        # produce a 1-dim array [channel][layer][group]
        valsOut = np.concatenate(valsChs)
        
        # normalization (if needed)
        if weights is not None:
            for ig in range(self.ng):
                valsOut[ig::self.ng] =\
                    weights[ig]*valsOut[ig::self.ng]/valsOut[ig::self.ng].sum()
        elif normFlag:
            valsOut = valsOut / valsOut.sum()
        
        # final 1-dim numpy array        
        return valsOut
            

    def _reshapeTo3D(self, valsIn):
        """reshape the 1D matrix to a 3D vector corresponding to radial map
        
        Parameters
        ----------
        self : core Map object
            the object includes data about the channels, layers, ng
            the ``self`` object also includes channels Ids
        valsIn : 1-dim numpy array
            input vector with the following structure:
             gr1, gr-2, ...    gr1, gr-2, ...  gr1, gr-2, ...    gr1, gr-2, ...
            \______________/ \______________/ \______________/ \______________/
                 layer-0         layer-1                      ...
                \___________________________/  \___________________________/
                         channel-0                      channels-N
                                     
        Returns
        -------
        valsOut : 3-dim array
            output vector with the following structure:
            [channels][layers][groups]
            
        """

        numUniqueChannels = len(self.chIds)
        ng = self.ng
        # loop over all the channels in the radial maps 
        # even if these have the same chId
        valsInFull = [None]*self.numChannels  # holds the entire distribution
                                              # of channels with repetitive ids
        idx0 = 0
        for idx, chId in enumerate(self.orderedChIds):
            chData = self.channels[chId]  # includes layers, channels, ...
            
            idx1 = idx0 + chData['nlayers']*ng
            
            chVals1D = valsIn[idx0:idx1]  # layers and groups for a specific ch
            idx0 = idx1  # update for the next channel
            
            # reshape the values to 2-m array [layers][groups]
            chVals2D = chVals1D.reshape((chData['nlayers'], ng))
                
            # insert the layer-group values into the channels values list
            valsInFull[idx] = chVals2D
        
        
        # the final 3D list os only defined for the defined unique channels
        valsOut = [None]*numUniqueChannels
        # insert the values to the correct channel
        for idxTo, chId in enumerate(self.chIds):
            chData = self.channels[chId]
            # reset group values for all the layers
            groupVals = np.zeros((chData['nlayers'], ng))  
            for idxFrom in chData['channelsIdx']:
                groupVals = groupVals + valsInFull[idxFrom]
            valsOut[idxTo] = groupVals / chData['nchannels']
            
        # final 3-dim numpy array        
        return valsOut


            
    def Validate(self):
        """post validation to check that all channels were defined

        This function is executed once all the channels were added
        to the ``Map`` container. 
        If the number of defined channels is not equal to
        the number of expected channels the ``Validate`` will alert.

 
        Raises
        ------
        ValueError
            If the number of defined channels does not match the number of
            channels defined in the radial map.

        """

        expChannels = len(self.chIds)
        prdChannels = len(self.channels)
        if prdChannels != expChannels:
            raise ValueError("{} channels exist in the radmap, but {} "
                             "channels were defined "
                             .format(expChannels, prdChannels))

        
        # Check for potential errors
        chMap = list(self.chIds)
        chChnls = list(self.channels.keys())
        _compare2lists(chMap, chChnls, "Channel names in set <map>", 
                       "Channel names in set <channels>")

        

    # def Values(self, attr, chIds=None, volManip=None, **kwargs):
    #     """Obtain the values of a single attribute for all the channels

    #     This method returns a 2-dim list for a specific attribute across
    #     all channels and layers.


    #     Parameters
    #     ----------
    #     attr : string
    #         name of the attribute
    #     chIds : list of string
    #         list with all the channel names. If None, the results for all the
    #         channels is provided.
    #     volManip : string
    #         volume manipulation ['multiply', 'divide']. Default is None.
    #     kwargs : named arguments
    #         keys represent the state name and value represent the values.
    #         The filtering of data is performed according to kwargs.

    #     Examples
    #     --------
    #     >>> universes.Values("u0", attr="inf_nsf", fuel=900)
    #     ... TBC ....

    #     """

        

    #     if chIds is None:
    #         chIds = self.core.chIds

    #     nchannels = len(chIds)  # number of channels
    #     results = [None]*nchannels  # results will be stored here
        
        
    #     # check that the states for all the channels are provided            
    #     for key, value in kwargs.items():
    #         nvals = len(value)
    #         if nvals != nchannels:
    #             raise ValueError(
    #                 "The number of states for <{}> must be of size {} and not "
    #                 "{}".format(key, nchannels, nvals))

            
    #     for idx, chId in enumerate(chIds):
    #         state = {}  # construct the channel state
    #         for key, value in kwargs.items():
    #             state[key] = value[idx]   
        
    #         # Evaluate the results for a specific channel
    #         results[idx] = self._ChannelValues(chId, attr, volManip, **kwargs)
        
            
    #     return results
            
                            
    # def _ChannelValues(self, chId, attr, volManip=None, **kwargs):
    #     """Obtain the values of a single attribute and corresponding states

    #     This method returns a list vector for all the layers in the channel.
    #     All the state branches must be provided.


    #     Parameters
    #     ----------
    #     chId : string
    #         name of the channel
    #     attr : string
    #         name of the attribute
    #     volManip : string
    #         volume manipulation ['multiply', 'divide']. Default is None.
    #     kwargs : named arguments
    #         keys represent the state name and value represent the values.
    #         The filtering of data is performed according to kwargs.

    #     Examples
    #     --------
    #     >>> core.ValueChannel('ch1', 'infkappa', None,
    #     ...                   history=['nom', 'nom', 'nom', 'nom'],
    #     ...                   time=[0.0, 0.0, 0.0, 0.0],
    #     ...                   fuel=[900, 900, 900, 900],
    #     ...                   boron=[0, 0, 0, 0],
    #     ...                   dens=[700, 700, 700, 700])

    #     """

    #     if volManip is not None:
    #         _inlist(volManip, "Volume manipulation", ALLOWED_MANIPULATION)

    #     if chId not in self.core.chIds:
    #         raise KeyError("chId <{}> does not exist in {}"
    #                        .format(chId, self.core.chIds))

    #     univs = self[chId]['layers']  # all the universes in a specific channel
    #     nlayers = self[chId]['nlayers']  # number of layers
    #     vols = self[chId]['volumes']  # volumes
        
    #     values = [None]*nlayers

    #     for idx, univ in enumerate(univs):
            
    #         # loop over all the perturbations to build the current state
    #         state = {}
    #         for key, value in kwargs.items():
    #             if (idx==0) and (len(value) != nlayers):
    #                 raise ValueError(
    #                     "The number of entries for state {} must equal to the"
    #                     " number of universes <{}> in channel <{}>"
    #                     .format(len(value), nlayers, chId))
    #             state[key] = value[idx]


    #         if volManip == 'multiply':
    #             values[idx] = vols[idx]*self.Values(univ, attr, **state)[attr]
    #         elif volManip == 'divide':
    #             values[idx] = self.Values(univ, attr, **state)[attr]/vols[idx]   
    #         else:  # None
    #             values[idx] = self.Values(univ, attr, **state)[attr]

    #     return values
            


