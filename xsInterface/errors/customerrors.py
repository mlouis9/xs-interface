# -*- coding: utf-8 -*-
"""customerror

Specific errors raised when an error occurs in a specific state
of the execution.

Created on Wed Apr 06 09:45:00 2022 @author: Dan Kotlyar
Last updated on Wed Apr 06 14:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""

from xsInterface.containers.container_header import DataSettingsCard


class DataSettingsError(Exception):
    def __init__(self, message, method):
        str1 = "The following entries are expected: \n"
        str1 += "---------------------------------------------------------- \n"
        for istr in DataSettingsCard[method].keys():
            str1 += istr + "\n\t{}\n".format(DataSettingsCard[method][istr])
        super().__init__(message+"\n"+str1)

# -----------------------------------------------------------------------------
# USER-INPUT ERRORS
# -----------------------------------------------------------------------------

class NonInputError(Exception):
    def __init__(self, message):
        str1 = "Data can only be defined after data is set: "\
            "\"set <card> <data>\"\n"\
            "e.g. \"set settings\" \n"
        super().__init__("!!!\n"+message+"\n"+str1)


class InputGeneralError(Exception):
    def __init__(self, message):
        str1 = "\nGeneral Error with:\n"
        str1 += "------------------------------------ "
        super().__init__("!!!\n"+str1+"\n"+message)


class InputCardError(Exception):
    def __init__(self, message, INPUT_CARDS, card):
        str1 = "The following <{}> entries are expected: \n".format(card)
        str1 += "---------------------------------------------------------- \n"
        for istr in INPUT_CARDS[card].keys():
            str1 += istr + "\n\t{}\n".format(INPUT_CARDS[card][istr])
        super().__init__("!!!\n"+message+"\n"+str1)

class TemplateFileError(Exception):
    def __init__(self, message):
        str1 = "------------------------------------ "
        super().__init__("!!!\n"+str1+"\n"+message)
        
class ControlFileError(Exception):
    def __init__(self, message):
        str1 = "Input Error with:\n"
        str1 += "------------------------------------ "
        super().__init__("!!!\n"+str1+"\n"+message)
