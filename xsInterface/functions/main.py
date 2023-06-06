# -*- coding: utf-8 -*-
"""main

Main class object that connects and executes all the reading, storing and
printing cabalities.

Created on Fri July 22 10:20:00 2022 @author: Dan Kotlyar
Last updated on Mon June 05 07:45:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 04/14/2022 - DK
Read - 07/22/2022 - DK
Write - 07/22/2022 - DK
Table - 07/22/2022 - DK
Values - 07/22/2022 - DK
ValidateMap - 05/02/2023 - DK
CoreValues - 05/20/2023 - DK
Condense - 05/03/2023 - DK
SlicePlot - 05/24/2023 - DK
PopulateCoreData - 05/29/2023 - DK
ChannelsPlot - 06/05/2023 - DK
"""

import copy
from matplotlib import rcParams

import numpy as np

from xsInterface.functions.readcontroldict import Read
from xsInterface.functions.readinput import ReadInput
from xsInterface.functions.readtemplate import ReadTemplate
from xsInterface.functions.plotters import coreSlicePlot, Plot1d
from xsInterface.errors.checkerrors import _inlist, _islist, _isequallength,\
    _iszeropositive, _inrange, _isstr, _isnonNegativeArray

ALLOWED_MANIPULATION = ['multiply', 'divide']
rcParams['figure.dpi'] = 300
FONT_SIZE = 16
MARKER_SIZE = 6


class Main():
    """A container to store unique universes having MultipleSets objects

    Parameters
    ----------
    inputFile : str
        file directory path + file name.

    Attributes
    ----------
    univfiles : dict
        keys represent universe Ids; values the correposnding input files.
    templates: dict
        keys represent template Ids; values the correposnding template files.
    outputs: dict
        keys represent template Ids; values the correposnding output files.
    links: dict
        keys represent template Ids; values the universes Ids linked to these.
    formats: dict
        formats used for printing variables, states, attributes.
        {"state": "{:5.3f}", "var": "{:d}", "attr": "{:5.5e}", "nrow": 5}
    externalIds: dict
        keys represent universe Ids; values the external codes Ids 
        (e.g., serpent or shift) linked to these.       
    core : Map object
        an object with attributes and map that links the cross sections
        and the distribution of channels and universes.

    Methods
    -------
    Read : read all the universes data and templates
    Write : Populate all the data strings with actual values
    Table : Output specific data in a table format
    Values : Obtain specific parameters as arrays

    """

    def __init__(self, inputFile):
        
        # read the main 
        universes, outputs, templates, links, formats, externalIds, core =\
            Read(inputFile)
        self._univfiles = universes
        self._outputs = outputs
        self._templates = templates
        self._links = links
        self._formats = formats
        self._externalIds = externalIds
        self._dataFiles = {}
        self.core = core


    def Read(self, readUniverses=True, readTemplate=False,
             readMapTemplate=False, userdata=None):
        """Read universes cross-section data and associated templates
        
        The ``Read`` method also populates the template files with data. 

        Parameters
        ----------
        readTemplate : bool
            flag that indicates if templates need to be read and populated
            with data
        readUniverses : bool
            flag that indicates if cross sections for different universes
            need to be read
        userdata : dict
            contains the data for all the attributes in a 3-dim list
            with the structure #channels x #layers x #groups
            keys represent the attributes.


        Returns
        -------
        dataFiles : dict
            keys represent universes or dummy variables; values represent
            correponding files populated with data.

        """
        
        if readUniverses:
            # Read the data for all the universes
            self.universes = ReadInput(self._externalIds, **self._univfiles)
        
        # check if a core is provided and verify universes against channels
        self.ValidateMap()

        if readTemplate and readMapTemplate:
            print('readTemplate and readMapTemplate cannot be both '
                  'true.\nreadMapTemplate is set as True and '
                  'readTemplate is swtiched to False.')
            readTemplate = False

        if readMapTemplate:
            self._ReadCoreMap(userdata)
            return

        if not readTemplate:  # stop here if templates do not need to be ran
            return

        # Read templates
        self._dataFiles = {}
        
        # Read template files
        for tmplkey, tmplfile in self._templates.items():
            if self._links != {} and tmplkey in self._links:
                for univId in self._links[tmplkey]:
                    # include the univId in the name of the file
                    fileId =\
                        self._outputs[tmplkey]+univId+self._formats['postfix']
                    self._dataFiles[fileId] =\
                        ReadTemplate(tmplfile, self.universes, self._formats,
                                     univId)
            else:
                fileId = self._outputs[tmplkey]
                self._dataFiles[fileId] = ReadTemplate(tmplfile, self.universes,
                                                      self._formats)                


    def Write(self, writemode="w"):
        """Write the data file structure into dedicated output files"""
        
        if self._dataFiles == {}:
            raise ValueError("!!!No data exist. Execute the ``Read`` method.")
        
        print("\n")
        for inpFile, dataFile in self._dataFiles.items():
            print("... Writing to ...\n{}".format(inpFile))   
            # write the output files
            with open(inpFile, writemode) as txtFile:
                txtFile.writelines(dataFile)
        print("\n")


    def Table(self, univId, attrs=None, **kwargs):
        """Obtain the values of the specific attribute across different states

        The method obtains the values across all the provided states.
        Specific attributes can be selected. The results are ouputted for a
        specific universe in a table format.


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


        Examples
        --------
        >>> univs.Values("u0", attrs=None, dens=600)
        ... history  time  ...                   beta                  decay
        ... 0    None   2.5  ...  [1, 1, 1, 1, 1, 1, 1]  [1, 1, 1, 1, 1, 1, 1]
        ... 1    None   2.5  ...  [2, 2, 2, 2, 2, 2, 2]  [1, 1, 1, 1, 1, 1, 1]

        """
        
        return self.universes.TableValues(univId, attrs, **kwargs)


    def Values(self, univId, attr, **kwargs):
        """Obtain the values of a single attribute and corresponding states

        This method is similar to the ``Table``, but can only be applied
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

        Examples
        --------
        >>> universes.Values("u0", attr="inf_nsf", fuel=900)
        ... {'inf_nsf': [array([0.36666667]), array([0.36666667])],
        ...  'history': array(['nom', 'nom'], dtype='<U3'),
        ...  'time': array([0., 0.]),
        ...  'fuel': array([900., 900.]),
        ...  'mod': array([600., 600.]),
        ...  'cool': array([600., 500.])}

        """

        return self.universes.Values(univId, attr, **kwargs)


    def Condense(self, cutoffE):
        """Energy condensation method

        Condensation is performed for a new energy structure and for all the
        parameters in the macro and micro dictionaries over all existing states

        Parameters
        ----------
        cutoffE : 1-dim array
            energy cutoffs

        Raises
        ------
        TypeError
            If ``cutoffE`` is not array.
        ValueError
            If ``cutoffE`` is negative.

        Examples
        --------
        >>> xs.Condense([0.0625, 1E+03])

        """
        
        condObj = copy.deepcopy(self)  # deep copy of for the condensed object
        for univId in self.universes.universeIds:
            rc, states, msets =\
                self.universes.Condense(univId, cutoffE)
            condObj.universes.universes[univId] = (rc, states, msets)
            condObj.universes.PandaTables()
        return condObj


    def _Attributes(self):
        """obtain all the attribues stored for every universe"""
        
        attrs = {}  # keys represent the universe Id and values the attributes
        for univId in self.universes.universeIds:
            rc, states, msets =\
                self.universes.universes[univId]
            attrs[univId] = rc.macro+rc.micro+rc.kinetics+rc.meta
            

        return attrs


    def CoreValues(self, attrs, chIds=None, volManip=None, **kwargs):
        """Obtain the values for multiple attributes and all channels & layers.

        This method returns a dictionary with keys representing attributes
        and values that are 2-dim lists representing values across
        all channels and layers.


        Parameters
        ----------
        attrs : string or list of strings
            name of the attribute
        chIds : list of string
            list with all the channel names. If None, the results for all the
            channels is provided.
        volManip : string or list of string
            volume manipulation ['multiply', 'divide']. Default is None.
        kwargs : named arguments
            keys represent the state/branch name and value represent the values
            The filtering of data is performed according to kwargs.

        Returns
        -------
        results : dict
            keys represent attributes and values are the attributes value.

        Raises
        ------
        TypeError
            If ``attrs`` is not a list ot str.
        ValueError
            If the number of rows in kwrags does not match the number of
            channels defined.        
        
        Examples
        --------
        >>> xs.CoreValues(['infkappa', 'infsp0'], 
        ...              chIds=['S1', 'S2', 'S3', 'S4'], 
        ...              volManip=[None]*4, 
        ...              history=[['nom', 'nom', 'nom', 'nom']]*4,
        ...              time=[[0.0, 0.0, 0.0, 0.0]]*4, 
        ...              fuel=[[900, 900, 900, 900]]*4, 
        ...              boron=[[0, 0, 0, 0]]*4,
        ...              dens=[[700, 700, 700, 700]]*4)
        >>> xs.CoreValues('infflx', 
        ...              chIds=['S1', 'S2', 'S3', 'S4'], 
        ...              volManip=['divide'], 
        ...              history=[['nom', 'nom', 'nom', 'nom']]*4,
        ...              time=[[0.0, 0.0, 0.0, 0.0]]*4, 
        ...              fuel=[[900, 900, 900, 900]]*4, 
        ...              boron=[[0, 0, 0, 0]]*4,
        ...              dens=[[700, 700, 700, 700]]*4)
        """

        
        if chIds is None:
            chIds = self.core.chIds
            
        if isinstance(attrs, str):
            attrs = [attrs]  # convert to a list
            
        _islist(attrs, "Attributes")
        nattrs = len(attrs)  # number of attributes
        
        if (isinstance(volManip, str)) or (volManip is None):
            volManip = [volManip]*nattrs  # duplicate as number of channels
        else:
            _islist(volManip, "volManip")
        _isequallength(volManip, nattrs, "volManip")

       
        nchannels = len(chIds)  # number of channels
        results = {}  # create a dictionary to host all the results
        for attr in attrs:
            results[attr] = [None]*nchannels
        
        # check that the states for all the channels are provided            
        for key, value in kwargs.items():
            nvals = len(value)
            if nvals != nchannels:
                raise ValueError(
                    "The number of states for <{}> must be of size {} and not "
                    "{}".format(key, nchannels, nvals))

            
        for idx, chId in enumerate(chIds):
            state = {}  # construct the channel state
            for key, value in kwargs.items():
                state[key] = value[idx]   
        
            for jattr, attr in enumerate(attrs):
                # Evaluate the results for a specific channel
                results[attr][idx] =\
                    self._ChannelValues(chId, attr, volManip[jattr], **state)
        
            
        return results, chIds
            
                            
    def _ChannelValues(self, chId, attr, volManip=None, **kwargs):
        """Obtain the values of a single attribute and corresponding states

        This method returns a list vector for all the layers in the channel.
        All the state branches must be provided.


        Parameters
        ----------
        chId : string
            name of the channel
        attr : string
            name of the attribute
        volManip : string
            volume manipulation ['multiply', 'divide']. Default is None.
        kwargs : named arguments
            keys represent the state name and value represent the values.
            The filtering of data is performed according to kwargs.

        Examples
        --------
        >>> core.ValueChannel('ch1', 'infkappa', None,
        ...                   history=['nom', 'nom', 'nom', 'nom'],
        ...                   time=[0.0, 0.0, 0.0, 0.0],
        ...                   fuel=[900, 900, 900, 900],
        ...                   boron=[0, 0, 0, 0],
        ...                   dens=[700, 700, 700, 700])

        """

        if volManip is not None:
            _inlist(volManip, "Volume manipulation", ALLOWED_MANIPULATION)

        if chId not in self.core.chIds:
            raise KeyError("chId <{}> does not exist in {}"
                           .format(chId, self.core.chIds))

        univs = self.core[chId]['layers']  # all the universes in a specific channel
        nlayers = self.core[chId]['nlayers']  # number of layers
        vols = self.core[chId]['volumes']  # volumes
        
        values = [None]*nlayers

        for idx, univ in enumerate(univs):
            
            # loop over all the perturbations to build the current state
            state = {}
            for key, value in kwargs.items():
                if (idx==0) and (len(value) != nlayers):
                    raise ValueError(
                        "The number of entries for state {} must equal to the"
                        " number of universes <{}> in channel <{}>"
                        .format(len(value), nlayers, chId))
                state[key] = value[idx]


            values[idx] = self.Values(univ, attr, **state)[attr][0]
            if volManip == 'multiply':
                manipvals = [val*vols[idx] for val in values[idx]]
                values[idx] = manipvals
            elif volManip == 'divide':
                manipvals = [val/vols[idx] for val in values[idx]]
                values[idx] = manipvals 

        return values


    def ValidateMap(self):
        """post validation to check that all channels were defined

        This function is executed once all the channels were added
        to the ``Map`` container. 
        If the number of defined channels is not equal to
        the number of expected channels the ``VerifyChannels`` will alert.

 

        Raises
        ------
        ValueError
            If the number of defined channels does not match the number of
            channels defined in the radial map.

        """

        if self.core is not None:
            # verify that all the universes exist
            for channel in self.core.channels.values():
                for univ in channel['layers']:
                    _inlist(univ, "universe", self.universes.universeIds)
                

    def PopulateCoreData(self, states, attributes=None, volManip=None,
                         **addattrs):
        """Populate new data for all the channels and layers
    
        Instead of using the universes directly, the data is evaluated for
        the different channels and layers.
        
    
        Parameters
        ----------
        attributes : list
            all the attributes required for the problem. If None the attributes
            are obtained automaitically for all existing attributes.
        states : dict
            dict with keys as the states names, e.g., history, time, and pert 
            names and values as 2-dim list with the values of the state for 
            channels and layers. e.g., time = [[0.0, 0.0, 0.0, 0.0]]*5
        volManip : string or list of string
            volume manipulation ['multiply', 'divide']. Default is None.
        addattrs : **kwargs
            keys are the names of the new variables and corrsponding values
            are the values for these new attributes. If the values are None
            then the attribute is reset with unity values for all channels 
            and layers. 
    
       
        Attributes
        ----------
        core.corestates : dict
            dict with keys as the states names, e.g., history, time, and pert names 
            and values as 2-dim list with the values of the state for channels and
            layers. e.g., time = [[0.0, 0.0, 0.0, 0.0]]*5
        core.corevalues : dict
            keys represent attributes and values are 3-dim lists corrsponding
            to states provided in _states
        core.chIds : list
            list with all the names for all the channels

        Examples
        --------
        >>> xs.PopulateCoreData(attributes=['infkappa', 'infsp0', 'infflx'],
        ...                     states=states, 
        ...                     volManip=[None, None, 'divide'],
        ...                     sph=None, adf=adfvals)

        """
        
        # Obtain all attributes if not provided
        if attributes is None:
            for key, attrsvals in self._Attributes().items():
                attributes = attrsvals
                nattrs = len(attributes)
                break
            
        # define for which attributes manipulation is needed
        if isinstance(volManip, dict):
            volManipulations = [None]*nattrs
            for volkey, volval in volManip.items():
                _inlist(volkey, "Key in volManip", attributes)
                idx = attributes.index(volkey)
                volManipulations[idx] = volval  # insert the manipulation
        else:
            volManipulations = volManip
                    
                       
        # obtain all the values for the reference points
        nomvalues, chIds =\
        self.CoreValues(attributes, 
                        chIds=self.core.chIds, 
                        volManip=volManipulations, 
                        **states)
        
        chIds = list(chIds)
        nchs = len(chIds)  # number of channels
        ng = len(nomvalues[attributes[0]][0][0])  # number of energy groups

        layers = np.zeros(nchs, dtype=int)  # number of layers in each channel
        for chidx in range(nchs):
            layers[chidx] = len(nomvalues[attributes[0]][chidx])

        for key, value in addattrs.items():
            if value is None:
                x0 = [1.0]*nchs
                for ich, ch in enumerate(nomvalues[attributes[0]]):
                    nlayers = len(ch)  # number of layers
                    x0[ich] = [np.ones(ng)]*nlayers
                nomvalues[key] = x0  # add the new attribute
            else:
                _islist(value, "Values for {}".format(key))
                _isequallength(value, nchs, "1st-dim for {}".format(key))
                for ich, ch in enumerate(nomvalues[attributes[0]]):
                    nlayers = len(ch)  # number of layers
                    _isequallength(value[ich], nlayers, "2nd-dim for {}"
                                   .format(key))
                    for layer in value[ich]:
                         _isequallength(layer, ng, 
                                        "3rd-dim for {}".format(key))
                nomvalues[key] = value  # add the new attribute

        self.core.chIds = chIds
        self.core.corevalues = nomvalues
        self.core.corestates = states
        self.core.ng = ng
        self.core.layers = layers
        

        # Read xs data and templates and populate data for channels & layers
        self.Read(readUniverses=False, readMapTemplate=True,
                  userdata = nomvalues)   

    def SlicePlot(self, values, chIds=None, layer=0, egroup=0, radmap=None,
                  label=None, shift=None,  geomarker='s', norm=1.0,
                  spacesize=1.0, markersize=500, cmap='viridis', text=True, 
                  textsize=7, textcolor="w", textweight="bold", precision=".2f",
                  edge=2.5, chnls2Ignore=None, includeRows=None,
                  includeCols=None):

        """Plot radial selected property distribution
    
        Parameters
        ----------
        values : 3-dim list
            values for all the channels, layers, and energy groups. 
            values[channel][layer][group]
            The order of the provided values in terms of channels correspond to
            the order of the ``chIds`` list.
        chIds : list
            identification strings of all the channels.
        layer : int
            layer number integer. Default is 0.
        egroup : int
            energy group integer. Default is 0.
        label : str
            description of the output variable. A default exist for every
            parameter.
        shift : list of int
            shift rows by increments of 0.5 or 1 (negative or positive)
        geomarker : str
            marker type {"hexagonal": "h", "square": "s", "circular": "o"}
        norm : float
            data normalization factor
        spacesize : float
            determines the space between elements. The larger the number the
            the larger is the spacing.
        markersize : float
            hexagon/square/circles marker/shape size
        cmap : str
            color map
        text : bool
            flag to indicate if the text should be printed or not
        textsize : float
            size of the text
        textcolor : str
            color of the text
        textweight : str
            font weight of the text
        precision : str
            defines the precision of printing inside the markers.
            e.g., ".2f", ".5e" - must follow the format allowed in python.
        chnls2Ignore : str
            if this string appears (even partially) in the channel naming
            this channel will be ignored when presenting the results.
        includeRows : list with two integers
            only two components marking the first row and the last row
            that must be included. If None then all rows are included in the
            results presentation.
        includeCols : list with two integers
            only two components marking the first column and the last column
            that must be included. If None then all columns are included in the
            results presentation.            
    
        Examples
        --------
        >>> xs.SlicePlot(results['infflx'], layer=3, markersize=160, spacesize=60.0,
        ...              textsize=5, chnls2Ignore='R', textcolor='w', textweight="bold", 
        ...              precision=".2f", edge=2.0, norm=1E+16, label="flux [1E+16]")
    
        """
        
        # obtain the radial map
        if radmap is None:
            radmap = self.core.radmap

        if chIds is None:
            chIds = list(self.core.chIds)

        _iszeropositive(layer, "layer")
        _iszeropositive(egroup, "energy group")

        nrow = len(radmap)
        ncol = len(radmap[0])
        valsMap = np.zeros((nrow, ncol))

        for irow, rowVals in enumerate(radmap):
            for icol, colVal in enumerate(rowVals):
                if colVal is not None:
                    idx = chIds.index(colVal)
                    nlayers = len(values[idx])
                    _inrange(layer, "layer", [0, nlayers-1])
                    ngroups = len(values[idx][layer])
                    _inrange(egroup, "energy groups", [0, ngroups-1])
                    valsMap[irow, icol] = values[idx][layer][egroup]
           
        
        coreSlicePlot(
            radmap=radmap, values=valsMap, label=label, shift=shift,
            geomarker=geomarker, norm=norm,
            spacesize=spacesize, markersize=markersize, cmap=cmap, text=text,
            textsize=textsize, textcolor=textcolor, textweight=textweight,
            precision=precision, edge=edge, chnls2Ignore=chnls2Ignore,
            includeRows=includeRows, includeCols=includeCols)



    def ChannelsPlot(self, attr, xvalues, chIds=None, layers=None, egroup=0, 
                     flip=False, xlabel=None, ylabel=None,
                     norm=1.0, fontsize=FONT_SIZE, markers="--*", 
                     markerfill=False, markersize=MARKER_SIZE):
        """plot the 1-dim data of a property over multiple channels/layers
    
    
        Parameters
        ----------
        attr : str
            name of the attribute to be plot
        xvalues : array
            x-axis values, e.g., heights in cm.
        chIds : list
            identification strings of all the channels. If None then all
            channels are plotted
        flip : bool
            boolean flag to indicate whether results should flipped
        layers : int, list of int, ndarray of int
            identifier/s of the axial layer. If None then all layers are plotted
        xlabel : str
            x-axis label with a default ``Axial height, meters``
        ylabel : str
            y-axis label with a default for any existing parameter
        norm : float
            data normalization factor
        fontsize : float
            font size value
        markers : str or list of strings
            markers type
        markerfill : bool
            True if the marking filling to be included and False otherwise
        markersize : int or float
            size of the marker with a default of 8.
    
        Raises
        ------
        TypeError
            If ``chIds`` is not list ``layer`` is not int.
            If ``ylabel`` is not str or ``fontsize`` is not int.
            If ``egroup`` is not int.
        
        ValueError
            If ``layers`` is negative or does not exist.
            If ``egroup`` does not exist.
            If ``attr`` does not exist.
       
        """
    
        # Check potential errors
        _isstr(attr, "Attribute")
    
        allchIds = list(self.core.chIds)
        if chIds is None:
            chIds = allchIds
        else:
            for chId in chIds:
                _inlist(chId, "Channel Id", allchIds)
        
        if layers is not None:
            _isnonNegativeArray(layers, "layers")
        
        _iszeropositive(egroup, "energy group")

        allresults = self.core.corevalues
        allattrs = list(allresults.keys())
        _inlist(attr, "Attribute", allattrs)
        
        _inrange(egroup, "energy groups", [0, self.core.ng-1])

        results = allresults[attr]  # 3-dim 
        yvalues = {}  # results for all channels
        
        for chId in chIds:
            idxch = allchIds.index(chId)  # channel index
            nlayers = self.core.layers[idxch]  # number of layers
            if layers is None:
                layers = np.linspace(0, nlayers-1, nlayers, dtype=int)
            else:
                maxlayer = max(layers)
                # check that layers exist
                _inrange(maxlayer, "Max layer in {}".format(layers), 
                         [0, nlayers-1])
                nlayers = len(layers)
            yvals = np.empty(nlayers)
            xvals = np.empty(nlayers) 
            for idx, ilayer in enumerate(layers):
                yvals[idx] = results[idxch][ilayer][egroup]
                xvals[idx] = xvalues[ilayer]
            
            yvalues[chId] = yvals 
               
        # plot results for the chosen channels
        Plot1d(xvals, yvalues, flip=flip, xlabel=xlabel, ylabel=ylabel, 
               norm=norm, fontsize=fontsize, markers=markers, 
               markerfill=markerfill, markersize=markersize)  


    def _ReadCoreMap(self, attrsvals):
        """Read and store cross sections for all the channels and layers
        

        Returns
        -------
        dataFiles : dict
            keys represent universes or dummy variables; values represent
            correponding files populated with data.

        """
        

        # check if a core is provided and verify universes against channels
        self.ValidateMap()

        # get all the attributes for each of the universes
        # attrs = self._Attributes()

        # Read templates
        self._dataFiles = {}
                
        # Read template files
        for tmplkey, tmplfile in self._templates.items():
            for ich, ch in enumerate(self.core.chIds):
                layers = self.core.channels[ch]
                for idx, layer in enumerate(layers['layers']):
                    fileId =\
                        self._outputs[tmplkey]+ch+'_'+str(idx)+'_'+layer+\
                        self._formats['postfix']        
            
                    attrval = self._ChannelLayerValue(attrsvals, ich, idx)        
            
            
                    self._dataFiles[fileId] =\
                        ReadTemplate(tmplfile, self.universes, self._formats,
                                     layer, attrval)

    @staticmethod
    def _ChannelLayerValue(attrsvals, ich, ilayer):
        """obtain the values for all the attributes for a channel-layer pair"""
        
        attrval = {}
        if attrsvals is not None:
            for attr, vals in attrsvals.items():
                attrval[attr] = np.array(vals[ich][ilayer])
        return attrval


# class _Container():
#     """General container to hold whatever data is provided to it"""

#     def __init__(self, **kwargs):     
#         for key, value in kwargs.items():
#             setattr(self, key, value)


