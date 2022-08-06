"""container_header

File to define basic parameters shared within the container folder.
e.g.,:
    - default values

Created on Sat Apr 09 06:45:00 2022 @author: Dan Kotlyar
Last updated on Aat Apr 09 06:45:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

"""


# -----------------------------------------------------------------------------
#                      DEFAULT_VALUES
# -----------------------------------------------------------------------------

DATA_TYPES = ["macro", "micro", "kinetics", "meta"]
REL_PRECISION = 0.00001  # 0.001% - used to find indices in arrays

DataSettingsCard = {
    "NG": "number of energy groups for multi-group parameters",
    "DN": "number of delayed neutron groups for kinetic parameters",
    "macro": "macro data",
    "micro": "micro data",
    "kinetics": "kinetic data",
    "meta": "metadata/general data",
    "isotopes": "ZZAAA0/1 for all the isotopes",
    }

BranchCard = {
    "N": "number of branches",
    }

HistoryCard = {
    "N": "number of histories",
    }

TimeCard = {
    "UNITS": "time/burnup units",
    }

DataCard = {
    "FLUX": "name of the flux variable",
    "ENE": " energy structure in descending order. with Upper, lower bounds",
    "state": "state parameters (e.g., branch, time, history)",
    "macro": "macro data block",
    "micro": "micro data block",
    "kinetics": "kinetic data block",
    "meta": "metadata/general data block",
    }

ManipulateCard = {
    "condEcutoffs": "condensed energy cutoffs in descending order",
    "attrOut": " energy structure in descending order. with Upper, lower bounds",
    "attrIn1": "state parameters (e.g., branch, time, history)",
    "attrIn2": "macro data block",
    "operation": "mode of the operation"
    }

FilterCard = {
    "branches": "Number of branches",
    "histories": "Number of histories",
    "times": "Boolean flag to indicate what time-points are included",
    "attributes": "Attributes to be included"
    }

SerpentCard = {
    "N": "number of branches",
    "history name": "corresponding .coe file"
    }

