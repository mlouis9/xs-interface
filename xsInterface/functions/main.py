# -*- coding: utf-8 -*-
"""main

Main class object that connects and executes all the reading, storing and
printing cabalities.

Created on Fri July 22 10:20:00 2022 @author: Dan Kotlyar
Last updated on Fri July 22 14:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 04/14/2022 - DK
Read - 07/22/2022 - DK
Write - 07/22/2022 - DK
Table - 07/22/2022 - DK
Values - 07/22/2022 - DK

"""


from xsInterface.functions.readcontroldict import Read
from xsInterface.functions.readinput import ReadInput
from xsInterface.functions.readtemplate import ReadTemplate


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

    Methods
    -------
    Read : read all the universes data and templates
    Write : Populate all the data strings with actual values
    Table : Output specific data in a table format
    Values : Obtain specific parameters as arrays

    """

    def __init__(self, inputFile):
        
        # read the main 
        universes, outputs, templates, links, formats, externalIds =\
            Read(inputFile)
        self.univfiles = universes
        self.outputs = outputs
        self.templates = templates
        self.links = links
        self.formats = formats
        self.externalIds = externalIds
        self.dataFiles = {}


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
        