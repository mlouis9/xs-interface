# -*- coding: utf-8 -*-
"""debug_relabelcoe.py

Debug:
--------
Relabel .coe file

Created on Mon Feb 27 05:00:00 2023 @author: Dan Kotlyar
Last updated on Mon Feb 27 05:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

Last Checked:
---------------
06/05/2023 - DK

"""

from xsInterface.functions.relabelcoe import coeRelabel


# create a modified .coe file with branches relabeled to a readable
# xsInterface format
coeRelabel(origCoeFile="../debug/debugfiles/combTest2.i.coe",
           modCoeFile='../debug/debugfiles/updatedCoe.coe',
           inpLabels='../debug/debugfiles/branchLabels')


