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
    "dim_*": "dimensions for attribute * (0=scalar, arrays are for dim > 0)",
    }

BranchCard = {
    "N": "number of branches",
    }

HistoryCard = {
    "N": "number of histories",
    }
