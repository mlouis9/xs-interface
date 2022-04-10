# -*- coding: utf-8 -*-
"""customerror

Specific errors raised when an error occurs in a specific state
of the execution.

Created on Wed Apr 06 09:45:00 2022 @author: Dan Kotlyar
Last updated on Wed Apr 06 14:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""

from xsInterface.errors.error_header import DataSettingsCard, SingleSetCard


class DataSettingsError(Exception):
    def __init__(self, message, method):
        str1 = "The following entries are expected: \n"
        str1 += "---------------------------------------------------------- \n"
        for istr in DataSettingsCard[method].keys():
            str1 += istr + "\n\t{}\n".format(DataSettingsCard[method][istr])
        super().__init__(message+"\n"+str1)


class SingleSetError(Exception):
    def __init__(self, message, method):
        str1 = "The following entries are expected: \n"
        str1 += "---------------------------------------------------------- \n"
        for istr in SingleSetCard[method].keys():
            str1 += istr + "\n\t{}\n".format(SingleSetCard[method][istr])
        super().__init__(message+"\n"+str1)
