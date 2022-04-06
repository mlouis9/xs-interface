# -*- coding: utf-8 -*-
"""customerror

Specific errors raised when an error occurs in a specific state
of the execution.

Created on Wed Apr 06 09:45:00 2022 @author: Dan Kotlyar
Last updated on Wed Apr 06 14:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""

from xsInterface.functions.header import INPUT_CARDS

class DataSettingsError(Exception):
    def __init__(self, message):
        str1 = "The following entries are expected: \n"
        str1 += "---------------------------------------------------------- \n"
        for istr in INPUT_CARDS["DataSettings"].keys():
            str1 += istr + "\n\t{}\n".format(INPUT_CARDS["region"][istr])
        super().__init__(message+"\n"+str1)

