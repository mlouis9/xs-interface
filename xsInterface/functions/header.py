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
#                      CONSTANTS
# -----------------------------------------------------------------------------

NAVO = 0.602214199             # avogadro number
JOULE_2MEV = 6.241507649e+12   # conversion from Joule to MeV
BARN_2_CM2 = 1E-24             # Conversion from barns to cm**2


# -----------------------------------------------------------------------------
#                      DEFAULT OPTIONS
# -----------------------------------------------------------------------------

DEF_OPT = "TBD"

# -----------------------------------------------------------------------------
#                      DATA MANAGEMENT
# -----------------------------------------------------------------------------
# Storing indices
#

# COMPLETE

# -----------------------------------------------------------------------------
#                      PLOTTING
# -----------------------------------------------------------------------------
FONT_SIZE = 16

# -----------------------------------------------------------------------------
#                      DATA ATTRIBUTES
# -----------------------------------------------------------------------------
# Attributes that must exist for transmutation and decay calculations
dataSettingsCard =\
{"NG" : "number of energy groups for multi-group parameters", 
"DN" : "Delayed neutron groups for kinetic parameters",
"macro" : "macro data",
"micro" : "micro data",
"kinetics" : "kinetic data",
"meta" : "metadata/general data",
"isotopes" : "ZZAAA0/1 for all the isotopes"}

INPUT_CARDS = {
    "DataSettings": dataSettingsCard,
    }



