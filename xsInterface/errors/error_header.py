"""error_header

File to define basic parameters shared within the package.
Defines:
    - input paremeters for each function
    - cross sections
    - priniting options

Created on Wed Apr 06 09:45:00 2022 @author: Dan Kotlyar
Last updated on Wed Apr 06 09:45:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

"""


# -----------------------------------------------------------------------------
#                      INPUT CARDS
# -----------------------------------------------------------------------------

DataSettingsCard = {
    "init":
        {"NG": "number of energy groups for multi-group parameters",
         "DN": "number of delayed neutron groups for kinetic parameters",
         "macro": "macro data",
         "micro": "micro data",
         "kinetics": "kinetic data",
         "meta": "metadata/general data",
         "isotopes": "ZZAAA0/1 for all the isotopes"},
    "AddData":
        {"dataType": "select from macro / micro / kinetics / meta",
         "attributes": "user-defined names for the provided data type",
         "frmt": "select  array or dict", }
        }

SingleSetCard = {
    "init":
        {"dataSetup":
            "an object that defines the data (and type) to be collected",
         "statesSetup":
            "an object to store the perturbation states",
         "fluxName":
            "name of the flux variable on the ``datasets`` object",
         "energyStruct":
             "sorted energy structure array (excluding lowest energy)",
         "relPrecision":
             "relative precision used to find a close perturbation"},
    "AddState":
        {"branch": "set of values to describe a specific branch-off",
         "history": "the name of the history",
         "timeIdx": "time index",
         "timePoint": "existing time point"},
    "AddData":
        {"dtype": "a string from: [`macro`, `micro`, `kinetics`, `meta`]",
         "kwargs": "named arguments: data names and values. abs=[1, 2]"}
        }
