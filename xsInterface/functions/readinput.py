"""readinput.py

Serves as an user-friendly input interface.
Read the user-based input file.
All the input data are provided via the use of input cards.

Created on Mon May 06 12:10:00 2022 @author: Dan Kotlyar
Last updated on Mon May 06 12:10:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Clean the inpit file from comments  - 05/06/2022 - DK
Error checking - 04/11/2022 - DK



"""

from pathlib import Path
import copy
from re import compile, IGNORECASE

import numpy as np

from xsInterface.containers.container_header import DataSettingsCard,\
    BranchCard, HistoryCard
from xsInterface.containers.datasettings import DataSettings
from xsInterface.errors.checkerrors import _isstr, _compare2lists
from xsInterface.errors.customerrors import NonInputError, InputGeneralError,\
    InputCardError

# General regular expressions needed for processing data
SPECIAL_CHAR = compile(r'[\?\$\&\@\~\<\>\`]')  # special character
REPETITION_REGEX = compile(r'\*\s*[\d\.]+')
SET_REGEX = compile(r'\s*(set\s+)', IGNORECASE)
COMMENT_REGEX = compile(r'[\%\#]')  # a comment in a line
EQUAL_REGEX = compile(r'\s*\w+\s*\=\s*', IGNORECASE)
PUNCT_MARKS_REGEX = compile(r'\"[^\"]+\"')  # everything in punctuation marks
FIRSTWORD_REGEX = compile(r'\w+[_-]\w+|\w+')  # 1st word (e.g., dim_mac or mac)

# Regular expressions for all set cards
CARD_REGEX = {
    "settings": compile(r'\s*(set\s+)(settings)', IGNORECASE),
    "branches": compile(r'\s*(set\s+)(branches)', IGNORECASE),
    "histories": compile(r'\s*(set\s+)(histories)', IGNORECASE),
    "times": compile(r'\s*(set\s+)(times)', IGNORECASE), }

INPUT_CARDS =\
    {'settings': DataSettingsCard,
     'branches': BranchCard,
     'histories': HistoryCard}



def ReadInput(inputFile):
    """Read the input file defined by the user

    This function reads the input defined by the user and populates the
    corresponding required containers with settings, perturbations, and data.

    Parameters
    ----------
    inputFile : file path
        the full directory + file name path

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
    
    # Process all cards
    setLineData, states = _ProcessCards(data)
    
    return setLineData, states


def _ProcessCards(data):
    """Process the set lines and corresponding data"""

    # Reset all values    
    setLine = []
    states = {"branches": None, "histories": None, "times": None}

    for cardKey, cardData in data.items(): 
    
        settingsFound = CARD_REGEX["settings"].search(cardKey)  
        branchesFound = CARD_REGEX["branches"].search(cardKey)  
        historiesFound = CARD_REGEX["histories"].search(cardKey)  

        # settings
        if settingsFound is not None:
            # strip the ``set <card>`` from data
            setLine = cardKey[settingsFound.span()[1]:]
            # return container with settings
            rc = _ImportSettings(setLine, cardData)
        elif branchesFound is not None:
            setLine = cardKey[branchesFound.span()[1]:]
            states["branches"] = _ImportBranches(setLine, cardData) 
        elif historiesFound is not None:
            setLine = cardKey[historiesFound.span()[1]:]
            states["histories"] = _ImportHistories(setLine, cardData) 
            
    return rc, states


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
            tline = _ApplyRepetition(tline)
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


# -----------------------------------------------------------------------------
#                  Settings
# -----------------------------------------------------------------------------

def _ImportSettings(setLine, tlines):
    """import settings from the input"""

    expinputs = ['ng', 'dn']  # expected entries
    expvals = [2, 2]  # range of the number of expected values
    card = "settings"  # set card name
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)

    # Process the set line values
    # -------------------------------------------------------------------------
    setNames, setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    
    setValues = np.array(setValues, dtype=int)
    
    if setNames == []:  # card names not provided
        NG = int(setValues[0])
        DN = int(setValues[1])
    else:
        try:
            _compare2lists(expinputs, copy.deepcopy(setNames),
                           "Expected inputs", "User inputs")
        except ValueError as detail:
            raise InputCardError("{}\n{}\n".format(detail, errmsg),
                                 INPUT_CARDS, "settings")
        NG = int(setValues[setNames.index('ng')])
        DN = int(setValues[setNames.index('dn')])
        
        
    # Process the set card values
    # -------------------------------------------------------------------------
    expinps = ['macro', 'micro', 'kinetics', 'meta', 'isotopes', 'dim_macro',
               'dim_micro', 'dim_kinetics', 'dim_meta']
    errmsg = "{} must be provided in <set {}>.\n".format(expinps, card)

    # all cards and corresponding values are placed in a dictionary
    dvals = _ProcessCardData(tlines, expinps, card, errmsg)
    # identify what data is defines and what not
    flags = {"macro": False, "micro": False, "kinetics": False, "meta": False}
    for k in flags:
        flags[k] = True if dvals.get(k) is not None else False

    if dvals["isotopes"] is not None:
        dvals["isotopes"] = np.array(dvals["isotopes"])

    # Assign data to container:
    # -------------------------------------------------------------------------
    rc = DataSettings(NG, DN, flags["macro"], flags["micro"],
                      flags["kinetics"], flags["meta"], dvals["isotopes"])


    try:
        if flags["macro"]:
            rc.AddData("macro", dvals["macro"], dvals["dim_macro"])
        if flags["micro"]:
            rc.AddData("micro", dvals["micro"], dvals["dim_micro"])
        if flags["kinetics"]:
            rc.AddData("kinetics", dvals["kinetics"], dvals["dim_kinetics"])
        if flags["meta"]:
            rc.AddData("meta", dvals["meta"], dvals["dim_meta"])
    except (ValueError or TypeError or KeyError) as detail:
        raise InputCardError("{}\n{}\n".format(detail, errmsg),
                             INPUT_CARDS, "settings")        

    return rc


# -----------------------------------------------------------------------------
#                  Perturbations
# -----------------------------------------------------------------------------

def _ImportWhat(setLine, tlines, card, expinputs, expvals, dtype):
    """import card-values from the input"""
    # setLine :: the line of the set card
    # tlines :: data/lines following the set line
    # card :: name of the card
    # expinputs :: expected names of the cards to be provided
    # expvals :: expected number of values to be provided in the set line
    # dtype :: convert to data to this type

    # Process the set line values
    # -------------------------------------------------------------------------
    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)
    setNames, setValues = _ProcessSetLine(setLine, expvals, card, errmsg)
    
    setValues = np.array(setValues, dtype=int)
    
    if setNames == []:  # card names not provided
        N = int(setValues[0])
    else:
        try:
            _compare2lists(expinputs, copy.deepcopy(setNames),
                           "Expected inputs", "User inputs")
        except ValueError as detail:
            raise InputCardError("{}\n{}\n".format(detail, errmsg),
                                 INPUT_CARDS, card)
        N = int(setValues[setNames.index('n')])

    # all cards and corresponding values are placed in a dictionary
    errmsg = "<set {}>.\n".format(card)
    data = _GetCardData(tlines, card, errmsg)
    
    for item, value in data.items():
        data[item] = np.array(value, dtype=dtype)
    
    if N != len(data):
        raise InputCardError(
            "<{}> expected {}.\n<{}> {}: {} are provided\n".format(
                N, card, len(data), card,
                list(data.keys())), INPUT_CARDS, card)        
    
    return data


def _ImportBranches(setLine, tlines):
    """import branches definitions from the input"""

    card = "branches"  # set card name     
    expinputs = ['N']  # expected entries
    expvals = [1, 1]  # range of the number of expected values
    dtype= float
    branches = _ImportWhat(setLine, tlines, card, expinputs, expvals, dtype)    
    return branches


def _ImportHistories(setLine, tlines):
    """import branches definitions from the input"""

    card = "histories"  # set card name     
    expinputs = ['N']  # expected entries
    expvals = [1, 1]  # range of the number of expected values
    dtype= float
    histories = _ImportWhat(setLine, tlines, card, expinputs, expvals, dtype)    
    return histories


def _ImportTimes(setLine, tlines):
    """import branches definitions from the input"""

    card = "times"  # set card name     
    expinputs = ['units']  # expected entries
    expvals = [1, 1]  # range of the number of expected values
    dtype= float

    errmsg = "{} must be provided in <set {}>.\n".format(expinputs, card)
    


# -----------------------------------------------------------------------------
#                  Supplementary Functions
# -----------------------------------------------------------------------------

def _ProcessSetLine(tline, expvals, card, errmsg):
    """process the line and obtain the cards names and values"""
    # tline is the text line to be processed
    # expvals is the range [a,b] of expected values
    
    tline = tline.replace('=', '')  # remove "=" signs
    tline = tline.split()
    
    names = []
    values = []
    
    # check if card names are provided
    if (int(2*expvals[0]) <= len(tline) <= int(2*expvals[1])):
        names = [name for name in tline[0::2]]
        values = [val for val in tline[1::2]]
    # only values provided
    elif (int(expvals[0]) <= len(tline) <= int(expvals[1])):
        values = [val for val in tline]
    else:
        raise InputCardError(
            "Error in card <{}>. Range of [{},{}] values are expected.\n{}\n"
            .format(card, expvals[0], expvals[1], errmsg), INPUT_CARDS, card)        
    
    return names, values


def _GetCardData(tlines, setcard, errmsg):
    """process card's sublines and data"""
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
        raise InputCardError("!!!\nNo data is provided.\n{}\n".format(errmsg),
                             INPUT_CARDS, setcard)

    return cardData


def _ProcessCardData(tlines, expinputs, setcard, errmsg):
    """process card's sublines and data"""
    # tlines are the text lines to be processed
    # expinputs is a list of variables allowed
    # set card name, e.g., 'settings'
    # errmsg, error message to be presented
    
    # store results in a dictionary
    
    cardData = {}  # reset the dictionary with all expected keys
    for expinp in expinputs:
        cardData[expinp] = None
    
    # loop over all the data lines
    for tline in tlines:
        tline = tline.replace('=', '')  # remove "=" signs
        
        idx = FIRSTWORD_REGEX.search(tline).span()
        name = tline[idx[0]:idx[1]]
        vals = tline[idx[1]:]
        # convert to an array of strings from a text line
        values = vals.split()
        
        if name in expinputs:
            if cardData[name] is None:
                cardData[name] = values
            else:
                cardData[name] = cardData[name] + values  # concat data
        else:
            raise InputCardError("{}\n".format(errmsg), INPUT_CARDS, setcard)

    # check that not all keys are empty
    if not any(cardData.values()):
        raise InputCardError("No data is provided.\n{}\n".format(errmsg),
                             INPUT_CARDS, setcard)

    return cardData


def _CardsNames(tline):
    """obtain the names of all the cards in the line"""
    cards0 = EQUAL_REGEX.findall(tline)  # obtain ``cards = `` patterns
    if cards0 is not None:
        cards1 = []  # remove the `=` and spaces from the strings
        for card in cards0:
            card = card.replace("=", '')  # remove `=` signs
            card = card.replace(' ', '')  # remove spaces
            cards1.append(card)
    return cards1


def _CardsValues(tline):
    """obtain the values of all the cards in the line"""
    vals0 = EQUAL_REGEX.split(tline)  # obtain the values for the cards
    # remove empty components within the list ['', 'mat1'] --> ['mat1']
    for val in range(vals0.count('')):
        vals0.remove('')
    # no cards values are provided
    if len(vals0) < 1:
        raise InputGeneralError("\n{}\nMissing cards\' values.".format(tline))
    return vals0


def _CompareCardsValues(cards, vals, tline):
    """compare the number of cards and corresponding values"""
    if cards == []:
        pass
    elif len(cards) != len(vals):
        raise InputGeneralError("\nNumber of cards {} is not matching\n"
                                "number of values {}.\nLine:{}"
                                .format(cards, vals, tline))

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
