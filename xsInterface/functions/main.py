# -*- coding: utf-8 -*-
"""main

Main class object that connects and executes all the reading, storing and
printing cabalities.

Created on Fri July 22 10:20:00 2022 @author: Dan Kotlyar
Last updated on Wed May 03 17:30:00 2023 @author: Dan Kotlyar

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
CoreValues - 05/03/2023 - DK
Condense - 05/03/2023 - DK

"""

import copy

from xsInterface.functions.readcontroldict import Read
from xsInterface.functions.readinput import ReadInput
from xsInterface.functions.readtemplate import ReadTemplate
from xsInterface.errors.checkerrors import _inlist, _islist


ALLOWED_MANIPULATION = ['multiply', 'divide']


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

    def Read(self):
        """Read universes cross-section data and associated templates
        
        The ``Read`` method also populates the template files with data. 

        Returns
        -------
        dataFiles : dict
            keys represent universes or dummy variables; values represent
            correponding files populated with data.

        """

        # Read the data for all the universes
        self.universes = ReadInput(self.externalIds, **self.univfiles)
        
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

        # check if a core is provided and verify universes against channels
        self.ValidateMap()


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
        volManip : string
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
        ...              volManip=None, 
        ...              history=[['nom', 'nom', 'nom', 'nom']]*4,
        ...              time=[[0.0, 0.0, 0.0, 0.0]]*4, 
        ...              fuel=[[900, 900, 900, 900]]*4, 
        ...              boron=[[0, 0, 0, 0]]*4,
        ...              dens=[[700, 700, 700, 700]]*4)
        >>> xs.CoreValues('infflx', 
        ...              chIds=['S1', 'S2', 'S3', 'S4'], 
        ...              volManip='divide', 
        ...              history=[['nom', 'nom', 'nom', 'nom']]*4,
        ...              time=[[0.0, 0.0, 0.0, 0.0]]*4, 
        ...              fuel=[[900, 900, 900, 900]]*4, 
        ...              boron=[[0, 0, 0, 0]]*4,
        ...              dens=[[700, 700, 700, 700]]*4)
        """

        

        if chIds is None:
            chIds = self.core.chIds
            
        if isinstance(attrs, str):
            attrs = [attrs]  # convert to a string
            
        _islist(attrs, "Attributes")

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
        
            for attr in attrs:
                # Evaluate the results for a specific channel
                results[attr][idx] =\
                    self._ChannelValues(chId, attr, volManip, **state)
        
            
        return results
            
                            
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


            values[idx] = self.Values(univ, attr, **state)[attr]
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
                
                      

