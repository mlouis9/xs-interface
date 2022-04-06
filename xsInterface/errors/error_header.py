"""header

File to define basic parameters shared within the package.
Defines:
    - input paremeters for each function
    - cross sections
    - priniting options

Created on Wed Apr 06 09:45:00 2022 @author: Dan Kotlyar
Last updated on Wed Apr 06 09:45:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Expand the cross section dictionary ``IDX_XS`` - 02/26/2022 - DK



"""


# -----------------------------------------------------------------------------
#                      INPUT CARDS
# -----------------------------------------------------------------------------
# Attributes that must exist for transmutation and decay calculations
DataSettingsCard = {
"init":
    {"NG" : "number of energy groups for multi-group parameters", 
    "DN" : "number of delayed neutron groups for kinetic parameters",
    "macro" : "macro data",
    "micro" : "micro data",
    "kinetics" : "kinetic data",
    "meta" : "metadata/general data",
    "isotopes" : "ZZAAA0/1 for all the isotopes"},
"adddata":
    {"dataType" : "select from macro / micro / kinetics / meta", 
    "attributes" : "ser-defined names for the provided data type (e.g., ``abs``)",
    "frmt" : "select  array or dict", }
    }
