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

from re import compile, IGNORECASE

from xsInterface.errors.checkerrors import _isstr
from xsInterface.errors.error_header import DataSettingsCard
from xsInterface.errors.customerrors import NonInputError, InputGeneralError,\
    InputCardError

# General regular expressions needed for processing data
SPECIAL_CHAR = compile(r'[\?\$\&\@\~\<\>\`]')  # special character
REPETITION_REGEX = compile(r'\*\s*[\d\.]+')
SET_REGEX = compile(r'\s*(set\s+)', IGNORECASE)
COMMENT_REGEX = compile(r'[\%\#]')  # a comment in a line
EQUAL_REGEX = compile(r'\s*\w+\s*\=\s*', IGNORECASE)
PUNCT_MARKS_REGEX = compile(r'\"[^\"]+\"')  # everything in punctuation marks
# Regular expressions for all set cards
CARD_REGEX = {
    "settings": compile(r'\s*(set\s+)(settings\s+)', IGNORECASE),
    "perturbations": compile(r'\s*(set\s+)(perturbations\s+)', IGNORECASE), }

INPUT_CARDS =\
    {'settings': DataSettingsCard}



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
    setLineData = _ProcessCards(data)
    
    return setLineData


def _ProcessCards(data):
    """Process the set lines and corresponding data"""
    
    setLineData = []

    for cardKey, cardData in data.items(): 
    
        settingsFound = CARD_REGEX["settings"].search(cardKey)  
    
        if settingsFound is not None:
            # strip the ``set <card>`` from data
            setLineData = cardKey[settingsFound.span()[1]:].split()
            
    return setLineData, cardData


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

        if setMatch is not None:
            currKey = tline
            dataSets[currKey] = []
        elif dataSets != {} and currKey in dataSets.keys():
            dataSets[currKey].append(tline)
        else:
            raise NonInputError("\nThe following line:\n<{}>\nis not "
                                   "associated to any card.\n".format(tline))
    return dataSets


# ----------------------------------------------------------------------------
#                  Supplementary Functions
# -----------------------------------------------------------------------------


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
