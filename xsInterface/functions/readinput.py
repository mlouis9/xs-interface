"""readinput.py

Serves as an user-friendly input interface.
Read the user-based input file.
All the input data are provided via the use of input cards.

Created on Mon May 06 12:10:00 2022 @author: Dan Kotlyar
Last updated on Tue Aug 09 11:50:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Clean the inpit file from comments  - 05/06/2022 - DK
Import Settings, States - 05/12/2022 - DK
Import single data set - 05/22/2022 - DK
Import & populate multiple data set - 05/24/2022 - DK
Import & populate serpent data - 08/09/2022 - DK

"""

from pathlib import Path
from re import compile, IGNORECASE

import numpy as np

from xsInterface.containers.container_header import DataSettingsCard,\
    BranchCard, HistoryCard, TimeCard, DataCard, ManipulateCard, FilterCard,\
        SerpentCard, LabelCard
from xsInterface.functions.readserpent import ReadSerpent
from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.singleset import SingleSet
from xsInterface.containers.multiplesets import MultipleSets
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.universes import Universes
from xsInterface.errors.checkerrors import _isstr, _isnonNegativeArray
from xsInterface.errors.customerrors import NonInputError, InputGeneralError,\
    InputCardError, ControlFileError

# General regular expressions needed for processing data
SPECIAL_CHAR = compile(r'[\?\$\&\@\~\<\>\`]')  # special character
REPETITION_REGEX = compile(r'\*\s*[\d\.]+')
SET_REGEX = compile(r'\s*(set\s+)', IGNORECASE)
BLOCK_REGEX = compile(r'\s*(block\s+)', IGNORECASE)
COMMENT_REGEX = compile(r'[\%\#]')  # a comment in a line
EQUAL_REGEX = compile(r'\s*\w+\s*\=\s*', IGNORECASE)
PUNCT_MARKS_REGEX = compile(r'\"[^\"]+\"')  # everything in punctuation marks
FIRSTWORD_REGEX = compile(r'\w+[_-]\w+|\w+')  # 1st word (e.g., dim_mac or mac)
SECONDWORD_REGEX = compile(r'\s*(set\s+)(\w+[_-]\w+)')  # 2nd word
NUM_REGEX = compile(r'[0-9+-eE]*', IGNORECASE)
# Regular expressions for all set cards
CARD_REGEX = {
    "settings": compile(r'\s*(set\s+)(settings)', IGNORECASE),
    "branches": compile(r'\s*(set\s+)(branches)', IGNORECASE),
    "histories": compile(r'\s*(set\s+)(histories)', IGNORECASE),
    "times": compile(r'\s*(set\s+)(times)', IGNORECASE),
    "data": compile(r'\s*(set\s+)(data)', IGNORECASE),
    "manipulate": compile(r'\s*(set\s+)(manipulate)', IGNORECASE),
    "filter": compile(r'\s*(set\s+)(filter)', IGNORECASE),
    "serpent": compile(r'\s*(set\s+)(serpent)', IGNORECASE),
    "labels": compile(r'\s*(set\s+)(labels)', IGNORECASE),}

INPUT_CARDS =\
    {'settings': DataSettingsCard,
     'branches': BranchCard,
     'histories': HistoryCard,
     'times': TimeCard,
     'data': DataCard,
     'manipulate': ManipulateCard,
     'filter': FilterCard,
     'serpent': SerpentCard, 
     'labels': LabelCard, }



def ReadInput(serpentIds, **kwargs):
    """Read the input file defined by the user

    This function reads the input defined by the user and populates the
    corresponding required containers with settings, perturbations, and data.
    It is important to note that multiple universes' data is read at once.

    Parameters
    ----------
    SerpentIds : dict
        Link between user-defined and serpent-defined Ids, e.g.
        {'fuel':['0', '1']}. The dict can be empty is serpent Ids are not used
    kwargs : named arguments
        keys represent the universe Id and value represent the full
        file directory path + file name.


    Raises
    ------
    TypeError
        If ``inputFile`` is not str.
    OSError
        If the path ``inputFile`` does not exist.
    ValueError
        If ``set element`` has no entries in the line.
        If ``material.temperatures`` and ``material.pressures`` are both None.
        If there are no properties for the material.
        If the number of items in ``serpentIds`` and ``kwargs`` not the same.

    """


    univs = Universes()

    if serpentIds == {}:
        for univId, inputFile in kwargs.items():
            serpentIds[univId] = [None]

    for univId, inputFile in kwargs.items():

        serpSets = {} # dict to store serpent data
        print("... Reading universe <{}> ...".format(univId))
        # check that `inputFile` variable is a string
        _isstr(inputFile, "Input file")
    
        # read the file and return its content
        filePath = Path(inputFile)
        if not filePath.is_file():
            raise OSError("The file {} does not exist.".format(inputFile))
    
        with open(inputFile, 'r') as fObject:
            dataFile = fObject.readlines()
            
        # strip comments and empty lines
        data = _CleanFile(dataFile)    
        
        for serpId in serpentIds[univId]:  
            # Process all cards
            rc, states, msets, serpSets = _ProcessCards(data, serpId, serpSets)
            
            if serpId is not None:
                univId = univId + serpId
            # add the data to the universe containers
            univs.Add(univId, rc, states, msets)
        
    
    # Build Pandas Tables for all the universes
    univs.PandaTables()
    
    return univs


def _ProcessCards(data, serpentId, serpentSets):
    """Process the set lines and corresponding data"""

    # Reset all values
    # -------------------------------------------------------------------------    
    setLine = []
    sd = {"brN": None, "branches": None, "histN": None,
          "histories": None, "times": None, "units": None}
    singlesets = {}  # dictionary to store all the single sets
    iset = 0
    cutoffE = None  # new wnergy condensation cutoff groups
    manipData = {}  # data to be manipulated
    filterData = {}  # filter data
    labels = {}  # labels for reading serpent .coe files
    # dict to store serpent files
    serpent = {"files": None, "time": True, "flx": None, "energy": None}
    multisets = None
    # -------------------------------------------------------------------------    

    cardsList = list(INPUT_CARDS.keys())

    for cardKey, cardData in data.items(): 
    
        cFound = {}  # cards Found dictionary
        for key in cardsList:
            cFound[key] = CARD_REGEX[key].search(cardKey)  
            errmsg = cardKey
        try:
            if cFound['settings'] is not None:
                card = 'settings'
                # strip the ``set <card>`` from data
                setLine = cardKey[cFound['settings'].span()[1]:]
                # return container with settings
                rc = _ImportSettings(setLine, cardData)
            elif cFound['branches'] is not None:
                card = 'branches'
                setLine = cardKey[cFound['branches'].span()[1]:]
                sd["brN"], sd["branches"] = _ImportBranches(setLine, cardData) 
            elif cFound['histories'] is not None:
                card = 'histories'
                setLine = cardKey[cFound['histories'].span()[1]:]
                sd["histN"], sd["histories"] =\
                    _ImportHistories(setLine, cardData) 
            elif cFound['times'] is not None:
                card = 'times'
                setLine = cardKey[cFound['times'].span()[1]:]
                sd["units"], sd["times"] = _ImportTimes(setLine, cardData)
            elif cFound['data'] is not None:
                card = 'data'
                setLine = cardKey[cFound['data'].span()[1]:]
                singlesets[iset] = _ImportData(setLine, cardData)
                iset += 1
            elif cFound['manipulate'] is not None:
                card = 'manipulate'
                setLine = cardKey[cFound['manipulate'].span()[1]:]
                cutoffE, manipData = _ImportManipulations(setLine, cardData) 
            elif cFound['filter'] is not None:
                card = 'filter'
                setLine = cardKey[cFound['filter'].span()[1]:]
                filterData = _ImportFilter(setLine, cardData) 
            elif cFound['serpent'] is not None:
                card = 'serpent'
                setLine = cardKey[cFound['serpent'].span()[1]:]
                serpent["files"], serpent["timeFlag"], serpent["flx"],\
                    serpent["energy"] = _ImportSerpentFiles(setLine, cardData) 
            elif cFound['labels'] is not None:
                card = 'labels'
                setLine = cardKey[cFound['labels'].span()[1]:]
                labels = _ImportLabels(setLine, cardData)
            else:
                raise InputGeneralError("Card does not exist: <{}>"
                                        .format(cardKey))
        except ValueError as detail:   
            raise InputCardError("{}\n{}\n".format(detail, errmsg),
                                 INPUT_CARDS, card)     
        except TypeError as detail:   
            raise InputCardError("{}\n{}\n".format(detail, errmsg),
                                 INPUT_CARDS, card)    
        except KeyError as detail:   
            raise InputCardError("{}\n{}\n".format(detail, errmsg),
                                 INPUT_CARDS, card)    

    # Populate containers
    # -------------------------------------------------------------------------
    try:
        #                                                              `states`
        #----------------------------------------------------------------------
        errmsg = "Error when inputting branches/states/times cards.\nPlease "\
        "check that these cards are properly defined.\n"
        states = _PopulateStates(sd)
        #                                                   `Serpent` .coe data
        #----------------------------------------------------------------------
        errmsg = "Serpent .coe data"
        card = "serpent"
        multisets, serpentSets =\
            _PopulateSerpentSets(rc, states, serpent, labels, serpentId,
                                 serpentSets)
        #                                                           `Data` sets
        #----------------------------------------------------------------------
        errmsg = "Data Sets"
        card = "data"
        multisets = _PopulateDataSets(rc, states, singlesets, multisets)
        #                                                     `Manipulate` data
        #----------------------------------------------------------------------
        errmsg = "Energy condensation and operations"
        card = "Manipulate"
        multisets, rc =\
            _PopulateManipulations(rc, multisets, cutoffE, manipData)
        #                                                     `Manipulate` data
        #----------------------------------------------------------------------
        errmsg = "States and data filtering"
        card = "filter"
        _CheckFilters(multisets, filterData)

    except TypeError as detail:
        raise InputGeneralError("{}\nInternal Error:{}\n"
                                .format(errmsg, detail))         
    except ValueError as detail:
        raise InputGeneralError("{}\nInternal Error:{}\n"
                                .format(errmsg, detail))  
    except KeyError as detail:
        raise InputGeneralError("{}\nInternal Error:{}\n"
                                .format(errmsg, detail))  
        
    return rc, states, multisets, serpentSets


# -----------------------------------------------------------------------------
#                  Populate Data/Storage Containers
# -----------------------------------------------------------------------------
def _PopulateStates(sd):
    """"populate the states container"""
    
    branches = None
    histories = None

    # Reset container    
    if sd["branches"] is not None:
        branches = list(sd["branches"].keys())
    if sd["histories"] is not None:
        histories = list(sd["histories"].keys())        
 
    
    states = Perturbations(sd["brN"], branches, sd["histN"], histories,
                           sd["times"], sd["units"])

    # Add data
    if sd["branches"] is not None:
        states.AddBranches(**sd["branches"])
    if sd["histories"] is not None:
        states.AddHistories(**sd["histories"])

    states._proofTest()
    return states


def _PopulateDataSets(rc, states, sss, ms=None):
    """"populate the multi sets container"""
    
    # reset the multi-sets object
    if ms is None:
        ms = MultipleSets(states, **rc.dataFlags)

    for data in sss.values():
        # reset a SingleSet object
        ene = np.array(data[2], dtype=float)
        ss = SingleSet(rc, states, fluxName=data[1], energyStruct=ene)
        for key, values in data[0].items():
            if key == 'state':
                ss.AddState(**values)
            else:
                ss.AddData(key, **values)
        # add the single set to multi sets
        ms.Add(ss)
    return ms


def _PopulateSerpentSets(rc, states, serpent, labels, serpId, serpentData):
    """"populate the multi sets container by reading serpent .coe files"""
    
    if serpent["files"] is not None and serpId is None:
        raise InputCardError("Name of serpent files provided \n<{}>.\nBut "
                             "serpent Id in the control files not provided."
                             .format(serpent["files"]), INPUT_CARDS, "serpent")
    elif serpId is not None and serpent["files"] is None:
        raise InputCardError("serpent Id in the control files provided.\n<{}>"
                             "Name of serpent files not provided. "
                             .format(serpId), INPUT_CARDS, "serpent")
    if serpId is None:
        ms = None
        return ms, serpentData
    
    # read serpent .coe only once
    if serpentData == {}:

        fnames = {'': serpent["files"]}
        attrs = rc.macro + rc.micro + rc.meta + rc.kinetics
    
        if serpent['time']:
            serpentData, timepoints =\
                ReadSerpent(fnames, labels, states.branches, attrs,
                            times=states.time['values'])
        else:
            serpentData, timepoints =\
                ReadSerpent(fnames, labels, states.branches, attrs,
                            burnup=states.time['values'])

    
    try:
        data = serpentData[serpId]
    
    except KeyError:
        errserp = "<set serpent> is not defined properly.\nSubsequent lines "\
        "must contain:\n<univ name> <universe Ids in the serpent file>"
        raise ControlFileError(
            "Serpent universe=<{}> does not exist\n{}."
            .format(serpId, errserp)) 
    
    # populate the single container
    ms = MultipleSets(states, **rc.dataFlags, overWrite=True)
    for histId in data:
        for timeId in data[histId]:
            for branchId in data[histId][timeId]:
                # store data for this specific state
                ss = SingleSet(rc, states, fluxName=serpent['flx'],
                               energyStruct=serpent['energy'])
                ss.AddState(branch=np.array(branchId), history=histId,
                            time=timepoints[timeId])
                for attr in data[histId][timeId][branchId]:
                    key = None
                    if attr in rc.macro:
                        key='macro'
                    elif attr in rc.micro:
                        key='micro'
                    elif attr in rc.kinetics:
                        key='kinetics'
                    else:
                        key='meta'
                    ss.AddData(key, **{attr:
                                       data[histId][timeId][branchId][attr]})

                # add the single set to multi sets
                ms.Add(ss)
        
    return ms, serpentData
    

def _PopulateManipulations(rc, ms, cutoffE, manipData):
    """"populate the multi sets container"""
    
    if cutoffE is not None:
        ms, ng = ms.Condense(cutoffE)
        rc.ng = ng
    if manipData != {}:
        attrs = list(manipData.keys())
        attrN = len(attrs)
        vals = list(manipData.values())  # [attr1, attr2, operation]
        
        # define empty lists
        attrs1 = [None]*attrN
        attrs2 = [None]*attrN
        modes = [None]*attrN
        
        for idx in range(attrN):
            attrs1[idx] = vals[idx][0]
            attrs2[idx] = vals[idx][1]
            modes[idx] = vals[idx][2]
        
        ms, macroFlags = ms.Manipulate(modes, attrs, attrs1, attrs2)
        
        # Add the new variable into the macro or micro settings
        for idx, macroFlag in enumerate(macroFlags):
            if macroFlag and attrs[idx] not in rc.macro:
                rc.macro.append(attrs[idx])
            if not macroFlag and attrs[idx] not in rc.micro:
                rc.micro.append(attrs[idx])
        
    return ms, rc


def _CheckFilters(ms, fltrData):
    """"check that filter data is properly defined"""
    
    # if no filter data is defined
    if fltrData == {}:
        ms.CheckFilters()
    else:
        ms.CheckFilters(fltrData['branches'], fltrData['histories'],
                        fltrData['times'], fltrData['attrs'])

# -----------------------------------------------------------------------------
#                  Settings
# -----------------------------------------------------------------------------

def _ImportSettings(setLine, tlines):
    """import settings from the input"""

    # Requirements
    # -------------------------------------------------------------------------
    expinputs = ['<NG>', '<DN>']
    expvals = [2, 2]  # range of the number of expected values
    card = "settings"  # set card name
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    setValues = np.array(setValues, dtype=int)
    NG = int(setValues[0])
    DN = int(setValues[1])

    # Process the set card values
    # -------------------------------------------------------------------------
    expinputs = ['macro', 'micro', 'kinetics', 'meta', 'isotopes', 'nuclides']
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # all cards and corresponding values are placed in a dictionary
    dvals0 = _CardDataDict(tlines, card, errmsg)
    
    dvals = {}
    for key in expinputs:
        if key in dvals0:
            dvals[key] = dvals0[key]
        else:
            dvals[key] = None
    
    # Data manipulation
    # -------------------------------------------------------------------------
    flags = {"macro": False, "micro": False, "kinetics": False, "meta": False}
    for k in flags:
        flags[k] = True if dvals.get(k) is not None else False

    if dvals["isotopes"] is not None:
        dvals["isotopes"] = np.array(dvals["isotopes"])

    # Assign data to designated container
    # -------------------------------------------------------------------------
    try:
        if dvals["nuclides"] is not None:
            nuclides = dvals["nuclides"][0]
        else:
            nuclides = None
        rc = DataSettings(NG, DN, flags["macro"], flags["micro"],
                          flags["kinetics"], flags["meta"], dvals["isotopes"],
                          nuclides)
        if flags["macro"]:
            rc.AddData("macro", dvals["macro"])
        if flags["micro"]:
            rc.AddData("micro", dvals["micro"])
        if flags["kinetics"]:
            rc.AddData("kinetics", dvals["kinetics"])
        if flags["meta"]:
            rc.AddData("meta", dvals["meta"])
    except (ValueError or TypeError or KeyError) as detail:
        raise InputCardError("{}\n{}\n".format(detail, errmsg),
                             INPUT_CARDS, "settings")        

    return rc

# -----------------------------------------------------------------------------
#                  Perturbations
# -----------------------------------------------------------------------------

def _ImportBranches(setLine, tlines):
    """import branches definitions from the input"""

    # Requirements
    # -------------------------------------------------------------------------
    card = "branches" 
    expinputs = ['<N>']
    expvals = [1, 100000]
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    setValues = np.array(setValues, dtype=int)
    N = int(setValues[0])
    
    if len(setValues) > 1:
        pass
        # branchUnits = setValues[1:]  # units of different branches (not used)

    # Process the set card values
    # -------------------------------------------------------------------------
    errmsg = "<set {}>.\n".format(card)
    data = _CardDataDict(tlines, card, errmsg)

    # Error Checking
    # -------------------------------------------------------------------------
    # N/A

    # Data manipulation
    # -------------------------------------------------------------------------       
    for item, value in data.items():
        data[item] = np.array(value, dtype=float)
        if value == [] or value is None:
            raise InputCardError("No data provided for branch <{}>.\n{}"
                                 .format(item, errmsg), INPUT_CARDS, card)

    return N, data


def _ImportHistories(setLine, tlines):
    """import branches definitions from the input"""

    # Requirements
    # -------------------------------------------------------------------------
    card = "histories" 
    expinputs = ['<N>']
    expvals = [1, 1]
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    setValues = np.array(setValues, dtype=int)
    N = int(setValues[0])

    # Process the set card values
    # -------------------------------------------------------------------------
    errmsg = "<set {}>.\n".format(card)
    data = _CardDataDict(tlines, card, errmsg)

    # Error Checking
    # -------------------------------------------------------------------------
    # N/A

    # Data manipulation
    # -------------------------------------------------------------------------       
    for item, value in data.items():
        data[item] = np.array(value, dtype=float)
        if value == [] or value is None:
            raise InputCardError("No data provided for history <{}>.\n{}"
                                 .format(item, errmsg), INPUT_CARDS, card)
    return N, data


def _ImportTimes(setLine, tlines):
    """import branches definitions from the input"""

    # Requirements
    # -------------------------------------------------------------------------
    card = "times" 
    expinputs = ['<UNITS>']
    expvals = [0, 1]
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    if setValues != []:
        units = setValues[0]
    else:
        units = 'n/a'

    # Process the set card values
    # -------------------------------------------------------------------------
    errmsg = "<set {}>.\n".format(card)
    data = _CardDataList(tlines, card, errmsg)

    # Error Checking
    # -------------------------------------------------------------------------
    # N/A

    # Data manipulation
    # -------------------------------------------------------------------------       
    data = np.array(data, dtype=float)

    return units, data


def _ImportLabels(setLine, tlines):
    """import labels definitions from the input"""

    # Requirements
    # -------------------------------------------------------------------------
    card = "labels" 
    expinputs = ['<N>']
    expvals = [1, 1]
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    N = int(setValues[0])

    # Process the set card values
    # -------------------------------------------------------------------------
    errmsg = "<set {}>.\n".format(card)
    data = _CardDataDict(tlines, card, errmsg)

    # Error Checking
    # -------------------------------------------------------------------------
    if N != len(data):
        raise InputCardError("Expected num. of labels=<{}>; provided=<{}>.\n{}"
                             .format(N, len(data), errmsg), INPUT_CARDS, card)  

    for item, value in data.items():
        if value == [] or value is None:
            raise InputCardError("No data provided for label <{}>.\n{}"
                                 .format(item, errmsg), INPUT_CARDS, card)

    # Data manipulation
    # -------------------------------------------------------------------------    
    # N/A

    return data


def _ImportManipulations(setLine, tlines):
    """import manipulation operation definitions from the input"""

    # Requirements
    # -------------------------------------------------------------------------
    card = "manipulate" 
    expinputs = ['<cond_E_cutoffs>']
    expvals = [1, 100000]
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    cutoffE = np.array(setValues, dtype=float)

    # Process the set card values
    # -------------------------------------------------------------------------
    errmsg = "<set {}>.\n".format(card)
    data = _CardDataDict(tlines, card, errmsg)

    # Error Checking
    # -------------------------------------------------------------------------
    # N/A

    # Data manipulation
    # -------------------------------------------------------------------------       
    if data != {}:  # manipulation is not mandatory
        for item, value in data.items():
            if len(value) != 3:
                raise InputCardError("Three entries [attrIn1, attrIn2, operati"
                                     "on] are expected for attrOut=<{}>.\n{}"
                                     .format(item, errmsg), INPUT_CARDS, card)

    return cutoffE, data


def _ImportFilter(setLine, tlines):
    """import filter definitions from the input"""

    # Store data under a single dictionary
    data = {'branches': None, 'histories': [None], 'times': [None],
            'attrs': None}

    # Requirements
    # -------------------------------------------------------------------------
    card = "filter" 
    expinputs = ['<N-branches>', '<history>', '<time>', '<attrs>']
    expvals = [4, 4]
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    setValues = np.array(setValues, dtype=int)
    _isnonNegativeArray(setValues, setLine)
    
    nBranches = setValues[0]
    if nBranches == 0:
        raise InputCardError(
            "Number of branches cannot be zero.\n{}"
            .format(setLine), INPUT_CARDS, card)          
    historyFlag = 1 if setValues[1] > 0 else 0
    timeFlag = 1 if setValues[2] > 0 else 0
    attrsFlag = 1 if setValues[3] > 0 else 0
    
    if (len(tlines) != nBranches + historyFlag + timeFlag + attrsFlag):
        raise InputCardError(
            "Number of lines in \n{}\n is not alligned with the parameters "
            "defined in: {}".format(tlines, setLine), INPUT_CARDS, card)  
    
    # Process the set card values
    # -------------------------------------------------------------------------
    errmsg = "<set {}>.\n".format(card)
    dataBranches = _CardDataDict(tlines[0:nBranches], card, errmsg)
    for key, vals in dataBranches.items():
        dataBranches[key] = np.array(vals, dtype=float)
    data['branches'] = dataBranches
    if historyFlag:
        idx0 = nBranches
        data['histories'] = _CardDataList(tlines[idx0:idx0+1], card, errmsg)
    if timeFlag:
        idx0 = nBranches+historyFlag
        dataTimes = _CardDataList(tlines[idx0:idx0+1], card, errmsg)
        data['times'] = np.array(dataTimes, dtype=float)
    if attrsFlag:
        idx0 = nBranches+historyFlag+timeFlag
        data['attrs'] = _CardDataList(tlines[idx0:idx0+1], card, errmsg)    

    # Error Checking
    # -------------------------------------------------------------------------
    # N/A

    # Data manipulation
    # -------------------------------------------------------------------------

    return data


def _ImportData(setLine, tlines):
    """import branches definitions from the input"""

    # Requirements
    # -------------------------------------------------------------------------
    card = "data" 
    expinputs = ['<FLUX>', '<ENE>']
    expvals = [2, 100000]  # at least two values must be provided
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    # idxData = setValues[0]  # index of the data set
    flxName = setValues[1]
    eneStruct = setValues[2:]  # must be in descending order

    # Separate between the different blocks
    dataBlocks = _SeparateBlock(card, tlines)
    expblocks = ['state', 'macro', 'micro', 'kinetics', 'meta']
    
    blksdata = {}
    for blkname, blklines in dataBlocks.items():

        if blkname not in expblocks:
            raise InputCardError(
                "Following blocks <{}> are expected.\n"
                .format(expblocks), INPUT_CARDS, card)    
        
        # Process the block card values
        # ---------------------------------------------------------------------
        errmsg = "<set {}; block {}>.\n".format(card, blkname)

        if blkname == 'micro':
            data = _BlockMicroDict(blklines, card, errmsg)
            blksdata[blkname] = data
            continue
            
        data = _CardDataDict(blklines, card, errmsg)
    
        # Data manipulation
        # -------------------------------------------------------------------------       
        for item, value in data.items():
            try:
                data[item] = np.array(value, dtype=float)
            except ValueError:
                data[item] = str(value[0])


        # Data manipulation
        # -------------------------------------------------------------------------       
        blksdata[blkname] = data

    return blksdata, flxName, eneStruct


def _ImportSerpentFiles(setLine, tlines):
    """import names of Serpent .coe files"""

    # Requirements
    # -------------------------------------------------------------------------
    card = "serpent" 
    expinputs = ['<N>', '<TIME>', '<FLUX>', '<ENE>']
    expvals = [4, 100000]  # at least three values must be provided
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    N = int(setValues[0])
    timeFlag = True
    if float(setValues[0]) < 0:
        timeFlag = False    
    flxName = setValues[2]
    eneStruct = np.array(setValues[3:], dtype=float)  # in descending order

    # Process the set card values
    # -------------------------------------------------------------------------
    errmsg = "<set {}>.\n".format(card)
    
    data = {}  # dictionary to store history .coe files
    # loop over all the data lines (with file names)
    for tline in tlines:
        tline = tline.replace('=', '')  # remove "=" signs
        
        idx = FIRSTWORD_REGEX.search(tline).span()
        name = tline[idx[0]:idx[1]]
        coefile = tline[idx[1]:]

        # remove redundant spaces at both ends of the file string
        coefile = coefile.rstrip()
        coefile = coefile.lstrip()
        
        data[name] = coefile
           

    # Error Checking
    # -------------------------------------------------------------------------
    # N/A

    # Data manipulation
    # -------------------------------------------------------------------------       
    for item, value in data.items():
        if value == '' or value == None:
            raise InputCardError("No data provided for serpent <{}>.\n{}"
                                 .format(item, errmsg), INPUT_CARDS, card)
            
    if N != len(data):
        raise InputCardError("Expected num. of files=<{}>; provided=<{}>.\n{}"
                             .format(N, len(data), errmsg), INPUT_CARDS, card)        

    return data, timeFlag, flxName, eneStruct


# -----------------------------------------------------------------------------
#                  Supplementary Functions
# -----------------------------------------------------------------------------
def _CleanFile(dataFile):
    """Remove comments and empty lines."""
    # a dictionary to separate between the different set cards
    # keys are the lines with the `set` cards
    # values represent the input values
    dataSets = {}
    currKey = []
    idata = 0
    for tline in dataFile:
        if tline.strip() != '':  # empty line?
            tline = _StripLine(tline)
            if tline.strip() == '':
                continue
            tline = _ApplyRepetition(tline)
        else:
            continue
        # no comment or empty line exist at this stage
        setMatch = SET_REGEX.search(tline)
        tline = tline.lower()  # case insensitive

        if setMatch is not None:
            currKey = tline
            # <set data> card can be defined multiple times
            if CARD_REGEX["data"].search(currKey) is not None:
                # add index to data
                currKey = tline.replace('data', 'data{:d}'.format(idata))
                idata += 1            
            dataSets[currKey] = []
        elif dataSets != {} and currKey in dataSets.keys():
            dataSets[currKey].append(tline)
        else:
            raise NonInputError("\nThe following line:\n<{}>\nis not "
                                   "associated to any card.\n".format(tline))
    return dataSets


def _SeparateBlock(card, data):
    """Remove comments and empty lines."""
    # a dictionary to separate between the different block cards
    # keys are the `block` cards
    # values represent the different variable names and values
    # card:: name of the card in which the block is defined
    # data:: data associated with this card (all the txt lines) 
    dataBlocks = {}
    currKey = []
    for tline in data:
        blockMatch = BLOCK_REGEX.search(tline)
        if blockMatch is not None:
            currKey = tline.split()
            nvalsBlk = len(currKey)
            if nvalsBlk != 2:
                raise NonInputError(
                    "\nThe following line:\n<{}>\nin card {}\n is not valid, "
                    "should contain `block <name>`\n".format(tline, card))    
            else:
                blkKey = currKey[1]

            dataBlocks[blkKey] = []
        elif dataBlocks != {} and blkKey in dataBlocks.keys():
            dataBlocks[blkKey].append(tline)
        else:
            raise NonInputError(
                "\nThe following line:\n<{}>\n is not associated to any block "
                "in card <{}>.\n".format(tline, card))
    if dataBlocks == {}:
        raise NonInputError(
            "\nNo data blocks are found in card <{}>\n".format(card))        
    
    return dataBlocks


def _ProcessSetLine(tline, expvals, card, errmsg):
    """process the line and obtain the cards names and values"""
    # tline:: is the text line to be processed
    # expvals:: is the range [a,b] of expected values
    # card:: name of the card
    # errmsg:: additional error message added to InputCardError
    
    tline = tline.split()
    
    values = []
    if (int(expvals[0]) <= len(tline) <= int(expvals[1])):
        values = [val for val in tline]
    else:
        raise InputCardError(
            "Range of [{},{}] values are expected.\n{}\n"
            .format(expvals[0], expvals[1], errmsg), INPUT_CARDS, card)        
    
    return values



def _CardDataDict(tlines, setcard, errmsg):
    """process card's data that do not include naming of variables"""
    # tlines are the text lines to be processed
    # set card name, e.g., 'settings'
    # errmsg, error message to be presented
    
    # store results in a dictionary
    
    cardData = {}  # reset the dictionary with all expected keys
   
    # loop over all the data lines
    for tline in tlines:
        tline = tline.replace('=', '')  # remove "=" signs
        
        idx = FIRSTWORD_REGEX.search(tline).span()
        name = tline[idx[0]:idx[1]]
        vals = tline[idx[1]:]
        # convert to an array of strings from a text line
        values = vals.split()
        cardData[name] = values
        
    # check that not all keys are empty
    if not any(cardData.values()):
        raise InputCardError("No data provided.\n{}\n".format(errmsg),
                             INPUT_CARDS, setcard)

    return cardData


def _CardDataList(tlines, setcard, errmsg):
    """process card's data that do not include naming of variables"""
    # tlines are the text lines to be processed
    # set card name, e.g., 'settings'
    # errmsg, error message to be presented
        
    cardData = []  # reset the list
    
    # loop over all the data lines
    for tline in tlines:       
        cardData = cardData + tline.split()
        
    # check that not all keys are empty
    if cardData == []:
        raise InputCardError("No data provided.\n{}\n".format(errmsg),
                             INPUT_CARDS, setcard)

    return cardData


def _BlockMicroDict(tlines, setcard, errmsg):
    """process the micro block"""
    # tlines are the text lines to be processed (include variable names)
    # set card name, e.g., 'settings'
    # errmsg, error message to be presented
    
    # store results in a dictionary
    
    cardData = {}  # reset the dictionary with all expected keys
    name = None
    values = []
    # loop over all the data lines
    for tline in tlines:
        tline = tline.replace('=', '')  # remove "=" signs
        # check if the line contains numeric values or not
        flagNum = True
        try:
            values = np.array(tline.split(), dtype=float)
            flagNum = True
        except ValueError:
            flagNum = False
        
        if flagNum:  # line with numbers
            if (name is None) or (name not in cardData):
                raise NonInputError(
                    "\nThe following line:\n<{}>\n is not associated to any "
                    "input in block <{}>.\n".format(tline, setcard))
            else:
                pvals = cardData[name]
                if pvals.size == 0:  # new data
                    cardData[name] = np.array([values])
                else:
                    try:  # append to existing data
                        cardData[name] = np.append(pvals, [values], axis=0)
                    except ValueError:
                        raise InputCardError(
                            "{}\nNumber of entries in line: \n<{}>\nnot "
                            "consistent with previous lines\n"
                            .format(errmsg, tline), INPUT_CARDS, setcard)                        
    
        else:  # line with the variable name
            idx = FIRSTWORD_REGEX.search(tline).span()
            name = tline[idx[0]:idx[1]]
            cardData[name] = np.array([[]])  # define an empty array
            
    # check that the dict is not empty
    if cardData == {}:
        raise InputCardError("No data provided.\n{}\n".format(errmsg),
                             INPUT_CARDS, setcard)

    return cardData

# -----------------------------------------------------------------------------
#                   DATA MANIPULATION FUNCTIONS
# -----------------------------------------------------------------------------

def _StripLine(tline):
    """Strip new line, tabs, spaces, comments"""
    tline = tline.replace("\n", '')  # remove new line
    tline = tline.replace("\t", ' ')  # remove tabs
    tline = tline.replace(',', ' ')  # remove commas
    commentMatch = COMMENT_REGEX.search(tline)
    if commentMatch is not None:
        tline = tline[0:commentMatch.span()[0]]
    if PUNCT_MARKS_REGEX.search(tline) is not None:  # this is not a file
        matchSpecialChar = SPECIAL_CHAR.search(tline)
        if matchSpecialChar is not None:
            raise NonInputError("\nSpecial chars {} not allowed:\n"
                                .format(tline))
    return tline


def _ApplyRepetition(tline):
    """modify the line and apply repetition"""
    # converts FE*3 --> FE FE FE
    starstr = REPETITION_REGEX.findall(tline)  # list with stars + numbers
    wordsrep = REPETITION_REGEX.split(tline)  # strings to be repeated

    if starstr == []:
        return tline  # the line does not contain stars

    # remove empty components from the lists
    for val in starstr:
        if val.isspace() or val == '':
            starstr.remove(val)
    for val in wordsrep:
        if val.isspace() or val == '':
            wordsrep.remove(val)

    if len(starstr) != len(wordsrep):
        raise InputGeneralError(
            "Number of repetition strings {} \nnot consistent with number of *"
            "{} in line:\n{}.\nIf the * star sign is used it must be used for "
            "all entries, even the single ones, e.g. ME*23 FE*1"
            .format(wordsrep, starstr, tline))

    # change the line
    tlineNew = ''
    for idx, rep in enumerate(starstr):
        numStr = rep.replace("*", '')  # remove the star and leave the number
        try:
            num = int(numStr)
        except ValueError:
            raise InputGeneralError(
                "Cannot convert the string {} after the {}* to a number.\n"
                "Line: {}".format(numStr, wordsrep[idx], tline))
        for nrep in range(num):
            tlineNew += ' ' + wordsrep[idx]
    return tlineNew


