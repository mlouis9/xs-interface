# -*- coding: utf-8 -*-
"""main

Main class object that connects and executes all the reading, storing and
printing cabalities.

Created on Fri July 22 10:20:00 2022 @author: Dan Kotlyar
Last updated on Wed May 24 05:00:00 2023 @author: Dan Kotlyar

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

"""

import copy
from matplotlib import rcParams

import numpy as np

from xsInterface.functions.readcontroldict import Read
from xsInterface.functions.readinput import ReadInput
from xsInterface.functions.readtemplate import ReadTemplate
from xsInterface.functions.coresliceplot import coreSlicePlot
from xsInterface.errors.checkerrors import _inlist, _islist, _isequallength,\
    _iszeropositive, _inrange

ALLOWED_MANIPULATION = ['multiply', 'divide']
rcParams['figure.dpi'] = 300


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
        self.univfiles = universes
        self.outputs = outputs
        self.templates = templates
        self.links = links
        self.formats = formats
        self.externalIds = externalIds
        self.dataFiles = {}
        self.core = core

    def Read(self, readUniverses=True, readTemplate=False,
             readMapTemplate=False):
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



        Returns
        -------
        dataFiles : dict
            keys represent universes or dummy variables; values represent
            correponding files populated with data.

        """
        
        if readUniverses:
            # Read the data for all the universes
            self.universes = ReadInput(self.externalIds, **self.univfiles)
        
        # check if a core is provided and verify universes against channels
        self.ValidateMap()

        if readTemplate and readMapTemplate:
            print('readTemplate and readMapTemplate cannot be both '
                  'true.\nreadMapTemplate is set as True and '
                  'readTemplate is swtiched to False.')
            readTemplate = False

        if readMapTemplate:
            self._ReadCoreMap()
            return

        if not readTemplate:  # stop here if templates do not need to be ran
            return

        # Read templates
        self.dataFiles = {}
        
        # Read template files
        for tmplkey, tmplfile in self.templates.items():
            if self.links != {} and tmplkey in self.links:
                for univId in self.links[tmplkey]:
                    # include the univId in the name of the file
                    fileId =\
                        self.outputs[tmplkey]+univId+self.formats['postfix']
                    self.dataFiles[fileId] =\
                        ReadTemplate(tmplfile, self.universes, self.formats,
                                     univId)
            else:
                fileId = self.outputs[tmplkey]
                self.dataFiles[fileId] = ReadTemplate(tmplfile, self.universes,
                                                      self.formats)                




    def Write(self, writemode="w"):
        """Write the data file structure into dedicated output files"""
        
        if self.dataFiles == {}:
            raise ValueError("!!!No data exist. Execute the ``Read`` method.")
        
        print("\n")
        for inpFile, dataFile in self.dataFiles.items():
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



    def _ReadCoreMap(self):
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
        self.dataFiles = {}
        
        self._corexs = {}
        
        # Read template files
        for tmplkey, tmplfile in self.templates.items():
            for ch, layers in self.core.channels.items():
                for idx, layer in enumerate(layers['layers']):
                    fileId =\
                        self.outputs[tmplkey]+ch+'_'+str(idx)+'_'+layer+\
                        self.formats['postfix']        
            
            
                    self.dataFiles[fileId] =\
                        ReadTemplate(tmplfile, self.universes, self.formats,
                                     layer)

