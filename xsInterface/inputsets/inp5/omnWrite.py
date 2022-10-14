# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:13:34 2022

@author: vlujan3
"""

def omnGen(num_groups, X, Y, Z, numPart, cycles, inactive, np, pnOrder, Nx, Ny, Nz):
    
    binEnergy = {  1 : "1.0000000000E+07 1.0000000000E-05",
                   2 : "1.5000000000E+07 6.2500000000E-01 1.0000000000E-11",
			       4 : "1.0000000000E+07 8.2100000000E+05 5.5300000000E+03 6.2500000000E-01 1.0000000000E-05",
			       8 : "1.0000000000E+07 8.2100000000E+05 5.5300000000E+03 4.0000000000E+00 6.2500000000E-01 2.8000000000E-01 1.4000000000E-01 5.8000000000E-02 1.0000000000E-05",
			       16 : "1.0000000000E+07 8.2100000000E+05 5.5300000000E+03 4.0000000000E+00 1.3000000000E+00 1.1500000000E+00 1.0970000000E+00 1.0200000000E+00 9.7200000000E-01 8.5000000000E-01 6.2500000000E-01 3.5000000000E-01 2.8000000000E-01 1.4000000000E-01 5.8000000000E-02 3.0000000000E-02 1.0000000000E-05",
			       40 : "1.0000000000E+07 6.0655000000E+06 3.6790000000E+06 2.2310000000E+06 1.3530000000E+06 8.2100000000E+05 5.0000000000E+05 1.1100000000E+05 9.1180000000E+03 5.5300000000E+03 1.4872800000E+02 4.8052000000E+01 2.7700000000E+01 1.5968000000E+01 9.8770000000E+00 4.0000000000E+00 3.3000000000E+00 2.6000000000E+00 2.1000000000E+00 1.8550000000E+00 1.5000000000E+00 1.3000000000E+00 1.1500000000E+00 1.0970000000E+00 1.0200000000E+00 9.7200000000E-01 9.5000000000E-01 8.5000000000E-01 6.2500000000E-01 3.5000000000E-01 2.8000000000E-01 2.2000000000E-01 1.8000000000E-01 1.4000000000E-01 1.0000000000E-01 8.0000000000E-02 5.8000000000E-02 4.2000000000E-02 3.0000000000E-02 1.5000000000E-02 1.0000000000E-05",
			       70 : "1.0000000000E+07 6.0655000000E+06 3.6790000000E+06 2.2310000000E+06 1.3530000000E+06 8.2100000000E+05 5.0000000000E+05 3.0250000000E+05 1.8300000000E+05 1.1100000000E+05 6.7430000000E+04 4.0850000000E+04 2.4780000000E+04 1.5030000000E+04 9.1180000000E+03 5.5300000000E+03 3.5191000000E+03 2.2394500000E+03 1.4251000000E+03 9.0689800000E+02 3.6726200000E+02 1.4872800000E+02 7.5501400000E+01 4.8052000000E+01 2.7700000000E+01 1.5968000000E+01 9.8770000000E+00 4.0000000000E+00 3.3000000000E+00 2.6000000000E+00 2.1000000000E+00 1.8550000000E+00 1.5000000000E+00 1.3000000000E+00 1.1500000000E+00 1.1230000000E+00 1.0970000000E+00 1.0710000000E+00 1.0450000000E+00 1.0200000000E+00 9.9600000000E-01 9.7200000000E-01 9.5000000000E-01 9.1000000000E-01 8.5000000000E-01 7.8000000000E-01 6.2500000000E-01 5.0000000000E-01 4.0000000000E-01 3.5000000000E-01 3.2000000000E-01 3.0000000000E-01 2.8000000000E-01 2.5000000000E-01 2.2000000000E-01 1.8000000000E-01 1.4000000000E-01 1.0000000000E-01 8.0000000000E-02 6.7000000000E-02 5.8000000000E-02 5.0000000000E-02 4.2000000000E-02 3.5000000000E-02 3.0000000000E-02 2.5000000000E-02 2.0000000000E-02 1.5000000000E-02 1.0000000000E-02 5.0000000000E-03 1.0000000000E-05"
                   }
    
    base = open("bwr_base.omn","r")
    omn = open("bwr.omn","w")
    
    for baseLine in base.readlines():
        omn.write(baseLine)
        
        if baseLine == "[PHYSICS=mg]\n":
            omn.write("neutron_bounds ")
            omn.write(binEnergy[num_groups])
            omn.write("\n")
            omn.write("num_groups ")
            omn.write(str(num_groups))
            omn.write("\n")
            omn.write("pn_order ")
            omn.write(str(pnOrder))
            omn.write("\n")
            omn.write('xml_path "')
            omn.write("output_fuel0.xml")
            omn.write('"\n')
            
        elif baseLine == "[SOURCE][SHAPE=box]\n":
            omn.write("box 0 ")
            omn.write(str(X))
            omn.write(" 0 ")
            omn.write(str(Y))
            omn.write(" 0 ")
            omn.write(str(Z))
            omn.write("\n")
            
        elif baseLine == "[SHIFT][KCODE]\n":
            omn.write("num_histories_per_cycle ")
            omn.write(str(numPart))
            omn.write("\n")
            omn.write("num_cycles ")
            omn.write(str(cycles))
            omn.write("\n")
            omn.write("num_inactive_cycles ")
            omn.write(str(inactive))
            omn.write("\n")
            
        elif baseLine == "[SHIFT][DECOMPOSITION=BMESH]\n":
            omn.write("x 0.00001 ")
            omn.write(str(X-0.00001))
            omn.write("\n")
            omn.write("y 0.00001 ")
            omn.write(str(Y-0.00001))
            omn.write("\n")
            omn.write("z 0.00001 ")
            omn.write(str(Z-0.00001))
            omn.write("\n")
            
        elif baseLine == "[RUN=mpi]\n":
            omn.write("np ")
            omn.write(str(np))
            
        elif baseLine == "[TALLY][NODAL]\n":
            omn.write("name tallies\n")
            omn.write("reactions flux fission\n")
            omn.write("neutron_bins ")
            omn.write(binEnergy[num_groups])
            omn.write("\n")
            omn.write("x 0 ")
            if Nx > 1:
                omn.write(str(Nx-1))
                omn.write("i ")
            omn.write(str(X))
            omn.write("\n")
            omn.write("y 0 ")
            if Ny > 1:
                omn.write(str(Ny-1))
                omn.write("i ")
            omn.write(str(Y))
            omn.write("\n")
            omn.write("z 0 ")
            if Nz > 1:
                omn.write(str(Nz-1))
                omn.write("i ")
            omn.write(str(Z))
            omn.write("\n")
        
    base.close()
    omn.close()