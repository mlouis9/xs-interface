# -*- coding: utf-8 -*-
"""test_datasettings.py

py Test:
The user needs to define the required data to be stored on the containers.
This container stores all the attributes and settings for the required data.


Created on Fri Apr 01 11:30:00 2022 @author: Dan Kotlyar
Last updated on Sat Apr 02 07:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import pytest

from xsInterface.containers.datasettings import DataSettings

# Reset the container with expected values
# -----------------------------------------------------------------------------
rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=True,
                  meta=False, isotopes=None)

# Feed in Macroscopic parameters
# -----------------------------------------------------------------------------
rc.AddData("macro", ["abs", "nsf", "sct"], "array")

# Feed in kinetics parameters
# -----------------------------------------------------------------------------
rc.AddData("kinetics", ["beta", "decay"], "array")


def test_badReset():
    """Errors when reseting the settings"""

    with pytest.raises(TypeError, match="number of energy groups*"):
        DataSettings(NG="a", DN=7, macro=True, micro=False, kinetics=True,
                     meta=False, isotopes=None)

    with pytest.raises(TypeError, match="number of delayed neutron groups*"):
        DataSettings(NG=2, DN="BAD_DN", macro=True, micro=False, kinetics=True,
                     meta=False, isotopes=None)

    with pytest.raises(TypeError, match="macro data*"):
        DataSettings(NG=2, DN=8, macro=7, micro=False, kinetics=True,
                     meta=False, isotopes=None)

    with pytest.raises(ValueError, match="number of energy groups*"):
        DataSettings(NG=-3, DN=7, macro=True, micro=False, kinetics=True,
                     meta=False, isotopes=None)

    with pytest.raises(ValueError, match="number of delayed neutron groups*"):
        DataSettings(NG=4, DN=0, macro=True, micro=False, kinetics=True,
                     meta=False, isotopes=None)

    with pytest.raises(ValueError, match="<isotopes> list/array must be*"):
        DataSettings(NG=4, DN=1, macro=True, micro=True, kinetics=True,
                     meta=False, isotopes=None)


def test_adddata():
    """Errors for the adddata method"""

    rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=True,
                      meta=False, isotopes=None)

    with pytest.raises(TypeError, match="data types*"):
        rc.AddData(10, ["abs", "nsf", "sct"], "array")

    with pytest.raises(TypeError, match="names of"):
        rc.AddData("macro", "BAD_ATTR", "array")

    with pytest.raises(KeyError, match="data type*"):
        rc.AddData("BAD_DATA_TYPE", ["abs", "nsf", "sct"], "array")

    with pytest.raises(KeyError, match="macro*"):
        rc.AddData("macro", ["abs", "nsf", "sct"], "BAD_FORMAT")


def test_proofTest():
    """Errors for the adddata method"""

    rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                      meta=False, isotopes=[92, 94, 95])
    rc.AddData("kinetics", ["beta", "decay"], "array")
    rc.AddData("macro", ["abs", "nsf", "sct"], "array")

    with pytest.raises(ValueError, match="micro*"):
        rc._proofTest()
