"""readcontroldict.py

This is a control dictionary interface that describes what files and templates
should be read. It also specifies the format that wil be used to output
the required information.

Created on Tue July 19 13:35:00 2022 @author: Dan Kotlyar
Last updated on Tue May 02 13:30:00 2023 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Read - 07/19/2022 - DK
serpent card - 08/09/2022 - DK
shift card - 09/13/2022 - DK
Radial map and channels - 05/02/2023 - DK

"""

from pathlib import Path
from re import compile, IGNORECASE
import copy

import numpy as np

from xsInterface.errors.checkerrors import _isstr, _compare2lists
from xsInterface.errors.customerrors import NonInputError, ControlFileError
from xsInterface.containers.mapping import Map

# General regular expressions needed for processing data
SPECIAL_CHAR = compile(r'[\?\$\&\~\<\>\`]')  # special character
SET_REGEX = compile(r'\s*(set\s+)', IGNORECASE)
COMMENT_REGEX = compile(r'[\%\#]')  # a comment in a line
EQUAL_REGEX = compile(r'\s*\w+\s*\=\s*', IGNORECASE)
PUNCT_MARKS_REGEX = compile(r'\"[^\"]+\"')  # everything in punctuation marks
FIRSTWORD_REGEX = compile(r'\w+[_-]\w+|\w+')  # 1st word (e.g., dim_mac or mac)
SECONDWORD_REGEX = compile(r'\s*(set\s+)(\w+[_-]\w+)')  # 2nd word
NUM_REGEX = compile(r'[0-9+-eE]*', IGNORECASE)
# Regular expressions for all set cards
UNIVS_REGX = compile(r'\s*(set\s+)(universes)', IGNORECASE)
TMPLT_REGX = compile(r'\s*(set\s+)(templates)', IGNORECASE)
FORMT_REGX = compile(r'\s*(set\s+)(formats)', IGNORECASE)
OUTPT_REGX = compile(r'\s*(set\s+)(outputs)', IGNORECASE)
LINKS_REGX = compile(r'\s*(set\s+)(links)', IGNORECASE)
SERPT_REGX = compile(r'\s*(set\s+)(serpent)', IGNORECASE)
SHIFT_REGX = compile(r'\s*(set\s+)(shift)', IGNORECASE)
CHANNELS_REGX = compile(r'\s*(set\s+)(channels)', IGNORECASE)
VOLUMES_REGX = compile(r'\s*(set\s+)(volumes)', IGNORECASE)
MAP_REGX = compile(r'\s*(set\s+)(map)', IGNORECASE)
IDX_REGEX = compile(r'\*\d+\[(.*?)\]')  # index inside parentheses
MAGIC_REGEX = compile(r'\*\s*\d+')  # index inside parentheses

# default formats for outputting data
STATE_FRMT = "{:5.3f}"
VAR_FRMT = "{:d}"
ATTR_FRMT = "{:5.5e}"
DELIM_FRMT = " "
ROW_VALS_N = 5  # maximum number of values printed in a line
POST_PRFX = ''

def Read(inputFile):
    """Read the input file defined by the user

    This function reads the input defined by the user and populates the
    corresponding required containers with settings, perturbations, and data.

    Parameters
    ----------
    inputFile : str
        file directory path + file name.

    Returns
    -------
    universes : dict
        keys represent universe Ids; values the correposnding input files.
    templates : dict
        keys represent template Ids; values the correposnding template files.
    outputs : dict
        keys represent template Ids; values the correposnding output files.
    links : dict
        keys represent template Ids; values the universes Ids linked to these.
    formats: dict
        formats used for printing variables, states, attributes.
    external : dict
        keys are the names of the universes Ids and values are the Ids in the
        external codes (e.g., serpent) files.
        None values are used for universes for which data is not read from
        the external code.

    
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

    """


    print("... Reading control dict ...\n<{}>\n".format(inputFile))        

    # check that `inputFile` variable is a string
    _isstr(inputFile, "Input file")

    # read the file and return its content
    filePath = Path(inputFile)
    if not filePath.is_file():
        raise OSError("The control file {} does not exist.".format(inputFile))

    with open(inputFile, 'r') as fObject:
        dataFile = fObject.readlines()
        
    # strip comments and empty lines
    data = _CleanFile(dataFile)
    
    # Process data
    universes, outputs, templates, links, formats, external, core =\
        _ProcessCards(data)
    
    return universes, outputs, templates, links, formats, external, core
    
    

def _ProcessCards(data):
    """Process the set lines and corresponding data"""

    # -------------------------------------------------------------------------  
    # Reset all dictionaries to store data
    # -------------------------------------------------------------------------    
    serpent = {}
    shift = {}
    universes = {}
    templates = {}
    outputs = {}
    univlinks = {}
    
    # data provided for channels and maps (not mandatory)
    coreChnls = None  # channels Ids
    coreVols = None   # channels volumes
    coreMap = None   # core map
    coreIdx = None  # core index bounds
    core = None  #  core object
    formats = {"state": STATE_FRMT, "var": VAR_FRMT, "attr": ATTR_FRMT,
               "nrow": ROW_VALS_N, "postfix": POST_PRFX,
               "delimiter": DELIM_FRMT}

    # -------------------------------------------------------------------------   
    #                              Error messages
    # -------------------------------------------------------------------------
    erruniv = "<set universes> is not properly defined.\nSubsequent lines "\
    "must contain:\n<univ name> <corresponding universe file input>"
    errtmpl = "<set templates> is not defined properly.\nSubsequent lines "\
    "must contain:\n<template name> <corresponding template file input>"
    erroutp = "<set outputs> is not defined properly.\nSubsequent lines "\
    "must contain:\n<template name> <corresponding output file>"
    errlink = "<set links> is not defined properly.\nSubsequent lines must"\
    " contain:\n<template name> <corresponding universes Ids>"
    errserp = "<set serpent> is not defined properly.\nSubsequent lines must"\
    " contain:\n<univ name> <corresponding serpent Ids>"
    errshft = "<set shift> is not defined properly.\nSubsequent lines must"\
    " contain:\n<univ name> <corresponding shift Ids>"
    
    # -------------------------------------------------------------------------   
    #                              Universes
    # -------------------------------------------------------------------------   
    for cardKey, cardData in data.items():
        if UNIVS_REGX.search(cardKey):
            universes = _ImportFiles(cardData, erruniv)
    if universes == {}:
        raise ControlFileError("<set universes> was not properly defined.")

       
    # -------------------------------------------------------------------------   
    #                              Templates
    # -------------------------------------------------------------------------   
    for cardKey, cardData in data.items():
        if TMPLT_REGX.search(cardKey):
            templates = _ImportFiles(cardData, errtmpl)
    if templates == {}:
        raise ControlFileError("<set templates> was not defined properly.")

    # -------------------------------------------------------------------------   
    #                              Outputs
    # -------------------------------------------------------------------------   
    for cardKey, cardData in data.items():
        if OUTPT_REGX.search(cardKey):
            outputs = _ImportFiles(cardData, erroutp)
    if outputs == {}:
        raise ControlFileError("<set outputs> was not defined properly.")

    for key in outputs:
        if key not in templates:
            raise ControlFileError(
                "Template Id <{}> defined in <set outputs> is not defined in "
                "<set templates>".format(key))


    # -------------------------------------------------------------------------   
    #                         Files-Universes Links
    # -------------------------------------------------------------------------   
    
    for cardKey, cardData in data.items():
        if LINKS_REGX.search(cardKey):
            links0 = _ImportFiles(cardData, errlink)
            for key, univstr in links0.items():
                univlinks[key] = [val for val in univstr.split()]
                if key not in templates:
                    raise ControlFileError(
                        "Template Id <{}> defined in <set links> is not "
                        "defined in <set templates>".format(key))
                

    # -------------------------------------------------------------------------   
    #                              Formats
    # -------------------------------------------------------------------------   
    for cardKey, cardData in data.items():
        if FORMT_REGX.search(cardKey):
            setLine =  cardKey[FORMT_REGX.search(cardKey).span()[1]:]
            formats = _ImportFormats(setLine, cardData, formats)
    if formats == {}:
        raise ControlFileError("<set formats> is not defined properly.")


    # -------------------------------------------------------------------------   
    #                 Channels, volumes, and map Data
    # -------------------------------------------------------------------------   
    for cardKey, cardData in data.items():
        if CHANNELS_REGX.search(cardKey):
            coreChnls = _CardDict(cardData)  # core channels
        if VOLUMES_REGX.search(cardKey):
            coreVols = _CardDict(cardData)  # core channels
        if MAP_REGX.search(cardKey):
            setLine =  cardKey[MAP_REGX.search(cardKey).span()[1]:]
            coreMap, coreIdx = _RadialMap(setLine, cardData)  # core map
    # create a core MAP object
    core = _Map(coreIdx, coreMap, coreChnls, coreVols)        

    # -------------------------------------------------------------------------   
    #                 External codes' (e.g., Serpent) Files
    # -------------------------------------------------------------------------   
    for cardKey, cardData in data.items():
        if SERPT_REGX.search(cardKey):
            serpent0 = _ImportFiles(cardData, errserp)
            for key, vals in serpent0.items():
                serpent[key] = [val for val in vals.split()]

    for cardKey, cardData in data.items():
        if SHIFT_REGX.search(cardKey):
            shift0 = _ImportFiles(cardData, errshft)
            for key, vals in shift0.items():
                shift[key] = [val for val in vals.split()]


    if shift != {} and serpent != {}:
        raise ControlFileError(
            "shift and serpent cards can not be provided together. \nEither "
            "serpent or shift only.")
    external = {}
    if serpent != {}:
        external = serpent
        errextr = "<set serpent> is not defined properly.\nSubsequent lines "\
            "must contain:\n<univ name> <universe Ids in the serpent file>"
    elif shift != {}:
        external = shift
        errextr = "<set serpent> is not defined properly.\nSubsequent lines "\
            "must contain:\n<univ name> <universe Ids in the serpent file>"

    if external != {}:
        for externalId in external:
            if externalId not in universes:
                raise ControlFileError(
                    "{}\nUniverses names must be consistent with <set "
                    "universes> card".format(errextr))
    for key in universes:
        if key not in external:
            external[key] = [None]

    univIds = []  # list to store all the Ids after joining the serpent Id    
    for univId, externalIds in external.items():
        for externalId in externalIds:
            if externalId is None:
                univIds.append(univId)
            else:
                univIds.append(univId+externalId)
    if univlinks != {}:
        for key in univlinks:
            for univId in univlinks[key]:
                if univId not in univIds:
                    raise ControlFileError(
                        "Universe <{}> in <set links> card is not consistent "
                        "with the allowed universes:\n{}"
                        .format(univId, univIds))                
    
    
    # Return values
    return universes, outputs, templates, univlinks, formats, external, core


# -----------------------------------------------------------------------------
#                  Output formatting
# -----------------------------------------------------------------------------

def _ImportFormats(setline, tlines, defltDict):
    """import output formatting"""

    frmtDict = copy.deepcopy(defltDict)

    # process the set line    
    values = []
    values = [val for val in setline.split()]
    
    if values != [] and len(values) > 2 :
        raise ControlFileError(
            "<set formats> is not defined properly.\Only a single integer "
            "value is allowed in set line, and not <{}>".format(values))
    else:
        try:
            frmtDict["nrow"] = int(values[0])
            if len(values) == 2:
                frmtDict["postfix"] = values[1]
        except:
            raise ControlFileError(
                "<set formats> is not defined properly.\nCorrect format "
                "<N> <postfox>, and not <{}>".format(values))
    if frmtDict["nrow"] < 1:
            raise ControlFileError(
                "<set formats> is not defined properly.\Only a single integer "
                "value (1 and above) is allowed in set line, and not <{}>"
                .format(values[0]))        

    # all cards and corresponding values are placed in a dictionary
    dvals0 = _CardDataDict(tlines)
    
    if dvals0 == {}:
        return defltDict
    
    for key in dvals0:
        if key in frmtDict:
            frmt = dvals0[key]
            frmt = frmt.rstrip()
            frmt = frmt.lstrip()
            frmt1 = "{:"+frmt+"}"
            try:
                frmt1.format(444)
                frmtDict[key] = frmt1
            except:
                raise ControlFileError(
                    "<set formats> is not defined properly.\Format {} is not "
                    "allowed.\nUse standard notation, such as: "\
                    "\n<4.3f>, <d>, <5.5e>.".format(frmt)) 
                
        else:
            raise ControlFileError(
                "<set formats> is not defined properly.\nKeyword {} not "
                "recognized.\nOnly the following keywords are allowed: "\
                "\n<state>, <attr>, <var>, <nrow>, <postfix>.".format(key))

    return frmtDict


# -----------------------------------------------------------------------------
#                  Files (templates, universes, outputs)
# -----------------------------------------------------------------------------
def _ImportFiles(tlines, errmsg):
    """Import data related to files definitions"""

    # all cards and corresponding values are placed in a dictionary
    dvals0 = _CardDataDict(tlines)
    
    if dvals0 == {}:
        raise ControlFileError(errmsg)

    outputsIds = {}
    for key in dvals0:
        # remove the spaces at the end of the string
        outfile = dvals0[key]
        outfile = outfile.rstrip()
        outfile = outfile.lstrip()
        if len(outfile) == 0:  # empty string
            raise ControlFileError(errmsg+
                                   "\nEmpty string for entry <{}>".format(key)) 
        
        if key not in outputsIds:
            outputsIds[key] = outfile
        else:
            outputsIds[key] += outfile

    return outputsIds


# -----------------------------------------------------------------------------
#                  Process Radial map distribution
# -----------------------------------------------------------------------------
def _RadialMap(setline, cdata):
    """Process radial map distribution with channels"""
    msgMap = "Entries' number for map indices {}\n not matching the data {}\n"\
        .format(setline, cdata)
    coreMap = []
    coreIdx = []

    if len(cdata) > 1:
        try:
            idxMap = _str2vec(setline, dtype=int)
        except ValueError:
            raise ControlFileError("set <map>:\n{}".format(cdata))
        if len(idxMap) != len(cdata):
            raise ControlFileError(msgMap)
    else:  # set default indices to zero
        idxMap = [0]*len(cdata)
    # Loop over the map layout for each row
    for rowIdx, rowData in enumerate(cdata):
        try:
            currRow = _str2vec(rowData, dtype=str)
            coreMap.append(currRow)
            coreIdx.append([idxMap[rowIdx],
                            idxMap[rowIdx] + len(currRow)-1])
        except ValueError:
            raise ControlFileError("set <map>:\n{}".format(currRow))

    return coreMap, coreIdx


def _Map(coreIdx, coreMap, channels, volumes):
    """create a Map object with radial channels and axial universes"""

    if (coreMap is None) and (channels is None):
            return None
    elif (coreMap is None):
        raise ControlFileError("set <map>\n{}\n"
                               "must be defined together with set <channels>"
                               .format(coreMap))
    elif (channels is None):
        raise ControlFileError("set <channels>\n{}\n"
                               "must be defined together set <map>"
                               .format(channels))
    # Check for potential errors
    if volumes is not None:
        chnames1 = list(channels.keys())
        chnames2 = list(volumes.keys())
        _compare2lists(chnames1, chnames2, "Channel names in <channels>", 
                       "Channel names in <volumes>")

    # Reset the container
    core = Map(coreMap, coreIdx)
    
    # loop over all the channels and add them to the object
    if volumes is None:
        for ch, universes in channels.items():
            core.Channel(ch, universes)
    else:
        for ch, universes in channels.items():
            vols = np.array(volumes[ch], dtype=float)
            core.Channel(ch, universes, vols)    

    # check that all channels were provided
    core.Validate()

    return core


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
    for tline in dataFile:
        if tline.strip() != '':  # empty line?
            tline = _StripLine(tline)
            if tline.strip() == '':
                continue
            tline = _repetitionIndexStar(tline)  # repetition of str*N1[N2, N3]
            tline = _repetitionStar(tline)  # repetition of str*N
        else:
            continue
        # no comment or empty line exist at this stage
        setMatch = SET_REGEX.search(tline)
        # tline = tline.lower()  # case insensitive

        if setMatch is not None:
            currKey = tline         
            dataSets[currKey] = []
        elif dataSets != {} and currKey in dataSets.keys():
            dataSets[currKey].append(tline)
        else:
            raise NonInputError("\nThe following line:\n<{}>\nis not "
                                   "associated to any card.\n".format(tline))
    return dataSets


def _repetitionIndexStar(tline):
    """modify the line and apply repetition"""
    # converts FE*3[1, 2] ME*2[4, 3]--> FE1 FE3 FE5 ME4 ME7

    msg0 ='Error when using the magic repetition star. Use integers & follow'\
        'the format: *N1[N2, N3]\n.'\

    FlagParen = False  # flag to indicate if parenthesis exist in line
    if IDX_REGEX.search(tline) is not None:
        FlagParen = True
    else:
        return tline  # return the original sentence without any modifications

    tline1 = ''  # tline decomposed into multiple line inserted into a list
    while FlagParen:

        # Loop over the entire line to identify repetitions
        idxcond = IDX_REGEX.search(tline)

        # process the following section in tline 'template univ*5[2, 3]'
        procsLine = tline[0:idxcond.span()[1]]

        # only the magic section '*5[2, 3]'
        magicSection = tline[idxcond.span()[0]:idxcond.span()[1]]
        
        # Repeat the following section without the magic card
        repeatLine = procsLine[0:idxcond.span()[0]]
        
        # Obtain the repeat word if exists
        
        allWords = _str2vec(repeatLine, dtype=str)
        if allWords == []:
            raise ControlFileError("Error in line {}\n with the string "
                              "<{}>.\n{}".format(tline, repeatLine, msg0))

        repeatWord = allWords[-1]  # only this str is repeated
        fixedStr = ' '
        if len(allWords) > 1:
            for val in allWords[0:-1]:
                fixedStr = fixedStr + ' ' + val  # str not be repeated
            

        idxSqL = magicSection.find('[')  # find left & right indices of [...]
        idxSqR = magicSection.find(']')
        
        try:
            # indices to access the data 
            indicesStr = magicSection[idxSqL+1: idxSqR]
            indices = _str2vec(indicesStr, int)
            if len(indices) != 2:
                raise ValueError()
        except:
            raise ControlFileError("Error in line {}\n with assessing indices "
                              "<{}>.\n{}".format(tline, magicSection, msg0))            
        
        try:
            numRepeat = int(magicSection[1: idxSqL])
        except:
            raise ControlFileError("Error in line {}\n with number of repeats "
                              "<{}>.\n{}".format(tline, magicSection, msg0)) 

        repeatSection = ' '
        currIdx = indices[0]
        incrStep = indices[1]
        for j in range(numRepeat):
            repeatSection = repeatSection + repeatWord + str(currIdx)+ ' '
            currIdx += incrStep
            if currIdx < 0:
                raise ControlFileError("Error in line \n{}\n"
                    "The defined step N3=<{}> results in negative index {}.\n"
                    "Change the step (N3) in the format *N1[N2, N3]"
                    .format(tline, incrStep, currIdx))                 
        
        tline1 = tline1 + fixedStr + repeatSection
        
        # remaining of the sentence
        try:
            remainLine = tline[idxcond.span()[1]:]
        except:
            return tline1
        
        # flag to indicate if parenthesis exist in line
        FlagParen = False  
        if IDX_REGEX.search(remainLine) is not None:
            FlagParen = True
        else:
            tline1 = tline1 + ' ' + remainLine
            return tline1

        tline = remainLine


def _repetitionStar(tline):
    """modify the line and apply repetition"""
    # converts FE*3 --> FE FE FE

    msg0 ='Error when using the magic repetition star. \n'\
        'The format is: str*N\n.'\

    FlagParen = False  # flag to indicate if magic star exist in line
    if MAGIC_REGEX.search(tline) is not None:
        FlagParen = True
    else:
        return tline  # return the original sentence without any modifications

    tline1 = ''  # tline decomposed into multiple line inserted into a list
    # Loop over the entire line to identify all repetitions
    while FlagParen:

        idxcond = MAGIC_REGEX.search(tline)

        # process the following section in tline 'template univ*3'
        procsLine = tline[0:idxcond.span()[1]]

        # only the magic section '*3'
        magicSection = tline[idxcond.span()[0]:idxcond.span()[1]]
        
        # Repeat the following section without the magic card
        repeatLine = procsLine[0:idxcond.span()[0]]
        
        # Obtain the repeat word if exists
        allWords = _str2vec(repeatLine, dtype=str)
        if allWords == []:
            raise ControlFileError("Error in line {}\n with the string "
                              "<{}>.\n{}".format(tline, repeatLine, msg0))

        repeatWord = allWords[-1]  # only this str is repeated
        fixedStr = ' '
        if len(allWords) > 1:
            for val in allWords[0:-1]:
                fixedStr = fixedStr + ' ' + val  # str not be repeated
            
        # convert the number of repetitions to integer from string    
        try:
            numRepeat = int(magicSection[1:])
        except:
            raise ControlFileError("Error in line {}\n with number of repeats "
                              "<{}>.\n{}".format(tline, magicSection, msg0)) 

        repeatSection = ' '
        for j in range(numRepeat):
            repeatSection = repeatSection + repeatWord + ' '
                    
        tline1 = tline1 + fixedStr + repeatSection
        
        # remaining of the sentence
        try:
            remainLine = tline[idxcond.span()[1]:]
        except:
            return tline1
        
        # flag to indicate if magic star exist in line
        FlagParen = False  
        if MAGIC_REGEX.search(remainLine) is not None:
            FlagParen = True
        else:
            tline1 = tline1 + ' ' + remainLine
            return tline1

        tline = remainLine


def _ProcessSetLine(tline):
    """process the line and obtain the cards names and values"""
    # tline:: is the text line to be processed
    # expvals:: number of expected values
    # errmsg:: additional error message added to InputCardError
    
    tline = tline.split()
    
    values = []
    values = [val for val in tline]
         
    return values



def _CardDataDict(tlines):
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
        if name not in cardData:
            cardData[name] = vals
        else:
            cardData[name] += ' {}'.format(vals)
        
    return cardData


def _CardDict(tlines):
    """first word as key and corresponding values"""
    
    cardData = {}  # reset the dictionary with all expected keys
   
    # loop over all the data lines
    for tline in tlines:
        tline = tline.replace('=', '')  # remove "=" signs
        strList = tline.split()
        if len(strList) < 2:
            raise ControlFileError("\nAt least two values must be inputted in"
                                   " line:\n{}".format(tline))            
        name = strList[0]
        vals = strList[1:]
        if name not in cardData:
            cardData[name] = vals
        else:
            cardData[name] = cardData[name] + vals
        
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
            raise ControlFileError("\nSpecial chars {} not allowed:\n"
                                .format(tline))
    return tline



def _str2vec(tline, dtype=float):
    """convert a line into a vector/ndarray"""
    if dtype is not str and dtype is not int and dtype is not float:
        raise ControlFileError("This line: \n{}\n Cannot be converted from "
                               "str to values".format(tline))
    strVals = tline.split()
    if dtype is str:
        return strVals
    vals = []
    for idx, val in enumerate(strVals):
        val = int(val) if dtype is int else float(val)
        vals.append(val)
    return np.array(strVals, dtype)


