"""stringsconversion.py

Functionality to convert strings to vectors, lists, arrays.

Created on Sat May 07 12:50:00 2022 @author: Dan Kotlyar
Last updated on Sat May 07 18:50:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
str2array  - 05/07/2022 - DK



"""

import numpy as np


def str2array(strLine, dtype=float):
    """converts a line string to a numpy array or list

    Parameters
    ----------
    strLine : str
        string line that contains values suitable for array, e.g. '1 2 3 4'
    dtype : variable type
        float, int, str

    Raises
    ------
    TypeError
        If ``dtype`` is not str, int, float.

    """    
    
    if dtype not in (str, int, float):
        raise TypeError("Data Type must be float/int/str and not {}".format(dtype))
        # raise InputGeneralError("{}\nstr-to-array conversion issue."
        #                         .format(str0))
    separate_str = strLine.split()
    vals = np.array(separate_str, dtype=dtype)
    
    if dtype == str:
        vals = list(vals)
        
    return vals
