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
    "adddata":
        {"dataType": "select from macro / micro / kinetics / meta",
         "attributes": "user-defined names for the provided data type",
         "frmt": "select  array or dict", }
        }
