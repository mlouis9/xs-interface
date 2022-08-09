"""readcontroldict.py

This is a control dictionary interface that describes what files and templates
should be read. It also specifies the format that wil be used to output
the required information.

Created on Tue July 19 13:35:00 2022 @author: Dan Kotlyar
Last updated on Fri Aug 05 13:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Read - 07/19/2022 - DK

"""

from pathlib import Path
from re import compile, IGNORECASE
import copy

from xsInterface.errors.checkerrors import _isstr
from xsInterface.errors.customerrors import NonInputError, ControlFileError

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

# default formats for outputting data
STATE_FRMT = "{:5.3f}"
VAR_FRMT = "{:d}"
ATTR_FRMT = "{:5.5e}"
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
    serpent : dict
        keys are the names of the universes Ids and values are the Ids in the
        serpent files. None values are used for universes for which data is not
        read from serpent.

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
    universes, outputs, templates, links, formats, serpent =\
        _ProcessCards(data)
    
    return universes, outputs, templates, links, formats, serpent
    
    

def _ProcessCards(data):
    """Process the set lines and corresponding data"""

    # -------------------------------------------------------------------------  
    # Reset all dictionaries to store data
    # -------------------------------------------------------------------------    
    serpent = {}
    universes = {}
    templates = {}
    outputs = {}
    univlinks = {}
    formats = {"state": STATE_FRMT, "var": VAR_FRMT, "attr": ATTR_FRMT,
               "nrow": ROW_VALS_N, "postfix": POST_PRFX}

    # -------------------------------------------------------------------------   
    #                              Error messages
    # -------------------------------------------------------------------------
    erruniv = "<set universes> is not properly defined.\nSubsequent lines must"
    " contain:\n<univ name> <corresponding universe file input>"
    errtmpl = "<set templates> is not defined properly.\nSubsequent lines must"
    " contain:\n<template name> <corresponding template file input>"
    erroutp = "<set outputs> is not defined properly.\nSubsequent lines must"
    " contain:\n<template name> <corresponding output file>"
    errlink = "<set links> is not defined properly.\nSubsequent lines must"
    " contain:\n<template name> <corresponding universes Ids>"
    errserp = "<set serpent> is not defined properly.\nSubsequent lines must"
    " contain:\n<univ name> <universe Id in the serpent file>"

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
    #                           Serpent Files
    # -------------------------------------------------------------------------   
    for cardKey, cardData in data.items():
        if SERPT_REGX.search(cardKey):
            serpent = _CardDict(cardData)
    if serpent != {}:
        for serpId in serpent:
            if serpId not in universes:
                raise ControlFileError(
                    "{}\nUniverses names must be consistent with <set "
                    "universes> card".format(errserp))
    for key in universes:
        if key not in serpent:
            serpent[key] = [None]

    # Return values
    return universes, outputs, templates, univlinks, formats, serpent



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
        
        outputsIds[key] = outfile

    return outputsIds


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
        else:
            continue
        # no comment or empty line exist at this stage
        setMatch = SET_REGEX.search(tline)
        tline = tline.lower()  # case insensitive

        if setMatch is not None:
            currKey = tline         
            dataSets[currKey] = []
        elif dataSets != {} and currKey in dataSets.keys():
            dataSets[currKey].append(tline)
        else:
            raise NonInputError("\nThe following line:\n<{}>\nis not "
                                   "associated to any card.\n".format(tline))
    return dataSets



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
        cardData[name] = vals
        
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
        cardData[name] = vals
        
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

