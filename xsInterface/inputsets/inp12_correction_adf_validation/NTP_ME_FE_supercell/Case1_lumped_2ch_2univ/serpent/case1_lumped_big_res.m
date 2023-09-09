
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct  3 2022 09:43:32' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 23])  = 'ntp_supercell_2D case 1' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1:  5])  = 'case1' ;
WORKING_DIRECTORY         (idx, [1: 29])  = '/home/jsmith818/Research_jake' ;
HOSTNAME                  (idx, [1: 28])  = 'ME04L0358GRD09.me.gatech.edu' ;
CPU_TYPE                  (idx, [1: 36])  = '12th Gen Intel(R) Core(TM) i9-12900K' ;
CPU_MHZ                   (idx, 1)        = 26.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Sep  7 19:14:59 2023' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Sep  7 19:34:46 2023' ;

% Run parameters:

POP                       (idx, 1)        = 20000 ;
CYCLES                    (idx, 1)        = 260 ;
SKIP                      (idx, 1)        = 40 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1694128499910 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 6 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:   6]) = [  1.00281E+00  9.97633E-01  9.99119E-01  1.00086E+00  9.99314E-01  1.00027E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 62])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 3.2E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.23608E-01 3.9E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  6.76392E-01 1.9E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.64805E-01 7.2E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  2.63888E-01 7.2E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  6.35597E+00 0.00036  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  4.56948E+01 0.00019  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  4.56948E+01 0.00019  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.27465E+02 0.00024  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  8.00533E+01 0.00024  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 260 ;
SIMULATED_HISTORIES       (idx, 1)        = 5200615 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00024E+04 0.00058 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00024E+04 0.00058 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.17029E+02 ;
RUNNING_TIME              (idx, 1)        =  1.97741E+01 ;
INIT_TIME                 (idx, [1:  2])  = [  7.65233E-01  7.65233E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.98333E-03  1.98333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.90069E+01  1.90069E+01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.97741E+01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 5.91827 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.99972E+00 2.3E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.80088E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 31798.27 ;
ALLOC_MEMSIZE             (idx, 1)        = 1224.16;
MEMSIZE                   (idx, 1)        = 1125.71;
XS_MEMSIZE                (idx, 1)        = 914.33;
MAT_MEMSIZE               (idx, 1)        = 75.83;
RES_MEMSIZE               (idx, 1)        = 1.83;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 133.72;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 98.45;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 3 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 230535 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.26000E-03 ;
URES_EMAX                 (idx, 1)        =  4.00000E-01 ;
URES_AVAIL                (idx, 1)        = 37 ;
URES_USED                 (idx, 1)        = 37 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 79 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 79 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 1736 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  0.00000E+00 ;
TOT_DECAY_HEAT            (idx, 1)        =  0.00000E+00 ;
TOT_SF_RATE               (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  0.00000E+00 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  0.00000E+00 ;
INGESTION_TOXICITY        (idx, 1)        =  0.00000E+00 ;
ACTINIDE_INH_TOX          (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ING_TOX          (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  0.00000E+00 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  0.00000E+00 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  0.00000E+00 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  2.98513E+08 0.00051  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.63840E-01 0.00104 ];
TH232_FISS                (idx, [1:   4]) = [  1.15703E+06 1.00000  3.71143E-07 1.00000 ];
U235_FISS                 (idx, [1:   4]) = [  3.03250E+12 0.00056  9.83945E-01 7.3E-05 ];
U238_FISS                 (idx, [1:   4]) = [  4.94808E+10 0.00455  1.60541E-02 0.00448 ];
TH232_CAPT                (idx, [1:   4]) = [  1.15897E+08 0.09476  4.00838E-05 0.09498 ];
U235_CAPT                 (idx, [1:   4]) = [  9.76400E+11 0.00107  3.37689E-01 0.00091 ];
U238_CAPT                 (idx, [1:   4]) = [  1.45856E+12 0.00107  5.04419E-01 0.00065 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 5200615 5.20000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.81451E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 5200615 5.20281E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 2517366 2.51842E+06 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 2683249 2.68440E+06 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 5200615 5.20281E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 1.24797E-07 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.00000E+02 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.83638E-41 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  7.54210E+12 2.9E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  3.08457E+12 2.8E-07 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.89083E+12 0.00053 ];
TOT_ABSRATE               (idx, [1:   2]) = [  5.97541E+12 0.00026 ];
TOT_SRCRATE               (idx, [1:   2]) = [  5.97026E+12 0.00051 ];
TOT_FLUX                  (idx, [1:   2]) = [  1.02922E+15 0.00048 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  5.97541E+12 0.00026 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.72943E+14 0.00042 ];
INI_FMASS                 (idx, 1)        =  5.44548E+36 ;
TOT_FMASS                 (idx, 1)        =  5.44548E+36 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.98193E+00 0.00034 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.67281E-01 0.00014 ];
SIX_FF_P                  (idx, [1:   2]) = [  3.27364E-01 0.00063 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  2.01147E+00 0.00059 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.26225E+00 0.00040 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.26225E+00 0.00040 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44510E+00 3.1E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02346E+02 2.8E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.26227E+00 0.00042  1.25391E+00 0.00041  8.34379E-03 0.00706 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.26288E+00 0.00026 ];
COL_KEFF                  (idx, [1:   2]) = [  1.26336E+00 0.00051 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.26288E+00 0.00026 ];
ABS_KINF                  (idx, [1:   2]) = [  1.26288E+00 0.00026 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.54022E+01 0.00019 ];
IMP_ALF                   (idx, [1:   2]) = [  1.53990E+01 0.00012 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  4.09634E-06 0.00286 ];
IMP_EALF                  (idx, [1:   2]) = [  4.10676E-06 0.00182 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  8.41657E-02 0.00348 ];
IMP_AFGE                  (idx, [1:   2]) = [  8.39152E-02 0.00079 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.29187E-03 0.00479  1.65610E-04 0.03140  8.63052E-04 0.01358  8.50721E-04 0.01441  2.44265E-03 0.00724  7.18755E-04 0.01560  2.51081E-04 0.02366 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  7.67327E-01 0.01243  1.23465E-02 0.00671  3.17776E-02 0.00011  1.09592E-01 0.00015  3.17972E-01 0.00011  1.35157E+00 9.9E-05  8.70372E+00 0.00089 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.59323E-03 0.00831  2.11641E-04 0.04929  1.10133E-03 0.02117  1.05568E-03 0.02185  3.04137E-03 0.01203  8.71703E-04 0.02366  3.11499E-04 0.03685 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  7.60661E-01 0.01924  1.24906E-02 1.3E-06  3.17797E-02 0.00016  1.09576E-01 0.00018  3.17928E-01 0.00018  1.35173E+00 0.00014  8.71072E+00 0.00133 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.37307E-05 0.00111  2.37242E-05 0.00111  2.47061E-05 0.01149 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.99532E-05 0.00102  2.99450E-05 0.00102  3.11869E-05 0.01150 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.61694E-03 0.00714  2.05027E-04 0.04818  1.07109E-03 0.01857  1.05346E-03 0.02016  3.03941E-03 0.01079  9.22062E-04 0.02093  3.25893E-04 0.03157 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  7.86778E-01 0.01651  1.24906E-02 1.1E-06  3.17763E-02 0.00016  1.09585E-01 0.00020  3.18031E-01 0.00017  1.35144E+00 0.00014  8.71578E+00 0.00145 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.37711E-05 0.00217  2.37614E-05 0.00218  2.51819E-05 0.02905 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.00049E-05 0.00217  2.99927E-05 0.00218  3.17843E-05 0.02904 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.47634E-03 0.02257  1.86552E-04 0.12603  1.04909E-03 0.06044  1.01967E-03 0.05285  3.04121E-03 0.03242  8.70378E-04 0.06076  3.09437E-04 0.09488 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  7.79153E-01 0.05112  1.24906E-02 3.6E-06  3.17722E-02 0.00045  1.09609E-01 0.00049  3.17909E-01 0.00045  1.35044E+00 0.00045  8.67329E+00 0.00203 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.44121E-03 0.02221  1.86477E-04 0.11955  1.05664E-03 0.05594  1.02071E-03 0.05300  2.98813E-03 0.02993  8.86269E-04 0.05869  3.02978E-04 0.09077 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  7.76676E-01 0.04836  1.24906E-02 3.5E-06  3.17701E-02 0.00045  1.09599E-01 0.00047  3.17892E-01 0.00042  1.35027E+00 0.00045  8.67002E+00 0.00189 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.73344E+02 0.02293 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.37452E-05 0.00065 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.99714E-05 0.00045 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.57942E-03 0.00394 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.77115E+02 0.00399 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.19228E-07 0.00077 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.30562E-05 0.00074  1.30560E-05 0.00074  1.30677E-05 0.00886 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  4.02936E-05 0.00068  4.02939E-05 0.00069  4.02234E-05 0.00848 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  3.36241E-01 0.00062  3.35735E-01 0.00063  4.34042E-01 0.01051 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.06190E+01 0.01289 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  4.56948E+01 0.00019  4.87095E+01 0.00027 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = 'M1' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  2.49324E+04 0.00575  1.09664E+05 0.00155  2.47194E+05 0.00155  4.61237E+05 0.00161  5.30039E+05 0.00109  5.29275E+05 0.00098  4.79793E+05 0.00115  4.20842E+05 0.00113  3.61454E+05 0.00134  3.12215E+05 0.00161  2.78406E+05 0.00135  2.59872E+05 0.00145  2.37636E+05 0.00109  2.26524E+05 0.00157  2.18673E+05 0.00133  1.88853E+05 0.00126  1.83670E+05 0.00113  1.81034E+05 0.00185  1.76327E+05 0.00221  3.35255E+05 0.00095  3.02213E+05 0.00143  2.06978E+05 0.00095  1.25967E+05 0.00194  1.37193E+05 0.00220  1.18318E+05 0.00153  9.77083E+04 0.00159  1.53047E+05 0.00142  3.23235E+04 0.00365  4.09405E+04 0.00288  3.76658E+04 0.00215  2.17413E+04 0.00417  3.85278E+04 0.00323  2.57148E+04 0.00380  2.16285E+04 0.00564  4.13429E+03 0.00735  3.97110E+03 0.00702  4.13824E+03 0.00923  4.25224E+03 0.00690  4.25866E+03 0.00868  4.23356E+03 0.00869  4.30673E+03 0.01215  4.01337E+03 0.00897  7.61483E+03 0.00897  1.21989E+04 0.00435  1.54628E+04 0.00479  4.01043E+04 0.00275  4.01397E+04 0.00300  3.92064E+04 0.00250  2.25283E+04 0.00428  1.46520E+04 0.00623  1.03883E+04 0.00668  1.10271E+04 0.00469  1.76891E+04 0.00487  1.97991E+04 0.00299  3.10265E+04 0.00351  3.80952E+04 0.00201  4.99649E+04 0.00229  3.14784E+04 0.00285  2.34008E+04 0.00281  1.75471E+04 0.00307  1.64929E+04 0.00401  1.72060E+04 0.00373  1.52472E+04 0.00492  1.08938E+04 0.00404  1.06323E+04 0.00666  1.01526E+04 0.00422  9.16521E+03 0.00391  7.78681E+03 0.00434  5.49949E+03 0.00619  2.18967E+03 0.00982 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  1.07936E+14 0.00059  7.04799E+12 0.00100 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  5.52384E-01 0.00026  1.01054E+00 0.00055 ];
INF_CAPT                  (idx, [1:   4]) = [  8.62339E-04 0.00048  8.38885E-03 0.00058 ];
INF_ABS                   (idx, [1:   4]) = [  8.62339E-04 0.00048  8.38885E-03 0.00058 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.08640E-08 0.00058  2.33896E-06 0.00065 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  5.51520E-01 0.00026  1.00216E+00 0.00054 ];
INF_SCATT1                (idx, [1:   4]) = [  2.65423E-01 0.00029  3.86191E-01 0.00069 ];
INF_SCATT2                (idx, [1:   4]) = [  1.01842E-01 0.00030  1.52072E-01 0.00139 ];
INF_SCATT3                (idx, [1:   4]) = [  2.98964E-03 0.01391  5.31561E-02 0.00307 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.44403E-02 0.00334  1.73408E-02 0.01207 ];
INF_SCATT5                (idx, [1:   4]) = [ -7.62630E-04 0.03700  6.02467E-03 0.02459 ];
INF_SCATT6                (idx, [1:   4]) = [  5.60887E-03 0.00461  3.12021E-03 0.04672 ];
INF_SCATT7                (idx, [1:   4]) = [  6.97096E-04 0.02854  2.56898E-03 0.03769 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  5.51523E-01 0.00026  1.00216E+00 0.00054 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.65423E-01 0.00029  3.86191E-01 0.00069 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.01842E-01 0.00030  1.52072E-01 0.00139 ];
INF_SCATTP3               (idx, [1:   4]) = [  2.98964E-03 0.01389  5.31561E-02 0.00307 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.44403E-02 0.00334  1.73408E-02 0.01207 ];
INF_SCATTP5               (idx, [1:   4]) = [ -7.62657E-04 0.03699  6.02467E-03 0.02459 ];
INF_SCATTP6               (idx, [1:   4]) = [  5.60888E-03 0.00461  3.12021E-03 0.04672 ];
INF_SCATTP7               (idx, [1:   4]) = [  6.97206E-04 0.02853  2.56898E-03 0.03769 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.30682E-01 0.00037  5.48779E-01 0.00081 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.44499E+00 0.00037  6.07413E-01 0.00081 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  8.59135E-04 0.00059  8.38885E-03 0.00058 ];
INF_REMXS                 (idx, [1:   4]) = [  1.53708E-02 0.00054  9.59937E-03 0.00369 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison decay constants:

PM147_LAMBDA              (idx, 1)        =  8.37254E-09 ;
PM148_LAMBDA              (idx, 1)        =  1.49451E-06 ;
PM148M_LAMBDA             (idx, 1)        =  1.94297E-07 ;
PM149_LAMBDA              (idx, 1)        =  3.62737E-06 ;
I135_LAMBDA               (idx, 1)        =  2.93061E-05 ;
XE135_LAMBDA              (idx, 1)        =  2.10657E-05 ;
XE135M_LAMBDA             (idx, 1)        =  7.55556E-04 ;
I135_BR                   (idx, 1)        =  9.01450E-01 ;

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  5.37013E-01 0.00026  1.45074E-02 0.00055  1.21696E-03 0.01033  1.00094E+00 0.00054 ];
INF_S1                    (idx, [1:   8]) = [  2.59801E-01 0.00030  5.62196E-03 0.00096  4.98617E-04 0.01778  3.85693E-01 0.00069 ];
INF_S2                    (idx, [1:   8]) = [  1.03055E-01 0.00031 -1.21306E-03 0.00271  4.11750E-04 0.02354  1.51660E-01 0.00137 ];
INF_S3                    (idx, [1:   8]) = [  5.51788E-03 0.00754 -2.52824E-03 0.00159  3.05445E-04 0.02078  5.28506E-02 0.00303 ];
INF_S4                    (idx, [1:   8]) = [ -1.33840E-02 0.00344 -1.05628E-03 0.00416  2.02360E-04 0.02943  1.71385E-02 0.01224 ];
INF_S5                    (idx, [1:   8]) = [ -8.04962E-04 0.03369  4.23326E-05 0.06141  1.13454E-04 0.04664  5.91121E-03 0.02543 ];
INF_S6                    (idx, [1:   8]) = [  5.43667E-03 0.00483  1.72203E-04 0.02146  4.84093E-05 0.12040  3.07180E-03 0.04752 ];
INF_S7                    (idx, [1:   8]) = [  6.65286E-04 0.03191  3.18103E-05 0.08191  8.91072E-06 0.77914  2.56007E-03 0.03596 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  5.37016E-01 0.00026  1.45074E-02 0.00055  1.21696E-03 0.01033  1.00094E+00 0.00054 ];
INF_SP1                   (idx, [1:   8]) = [  2.59801E-01 0.00030  5.62196E-03 0.00096  4.98617E-04 0.01778  3.85693E-01 0.00069 ];
INF_SP2                   (idx, [1:   8]) = [  1.03055E-01 0.00031 -1.21306E-03 0.00271  4.11750E-04 0.02354  1.51660E-01 0.00137 ];
INF_SP3                   (idx, [1:   8]) = [  5.51788E-03 0.00753 -2.52824E-03 0.00159  3.05445E-04 0.02078  5.28506E-02 0.00303 ];
INF_SP4                   (idx, [1:   8]) = [ -1.33841E-02 0.00344 -1.05628E-03 0.00416  2.02360E-04 0.02943  1.71385E-02 0.01224 ];
INF_SP5                   (idx, [1:   8]) = [ -8.04990E-04 0.03367  4.23326E-05 0.06141  1.13454E-04 0.04664  5.91121E-03 0.02543 ];
INF_SP6                   (idx, [1:   8]) = [  5.43668E-03 0.00483  1.72203E-04 0.02146  4.84093E-05 0.12040  3.07180E-03 0.04752 ];
INF_SP7                   (idx, [1:   8]) = [  6.65396E-04 0.03190  3.18103E-05 0.08191  8.91072E-06 0.77914  2.56007E-03 0.03596 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  7.79347E-02 0.00114  3.15292E-01 0.00869 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  7.76498E-02 0.00143  3.00955E-01 0.01429 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  7.78061E-02 0.00129  3.00049E-01 0.01230 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  7.83551E-02 0.00193  3.51124E-01 0.01337 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  4.27715E+00 0.00114  1.05817E+00 0.00859 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  4.29288E+00 0.00143  1.11026E+00 0.01408 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  4.28424E+00 0.00129  1.11291E+00 0.01208 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  4.25433E+00 0.00193  9.51327E-01 0.01311 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
LAMBDA                    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.32' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct  3 2022 09:43:32' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 23])  = 'ntp_supercell_2D case 1' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1:  5])  = 'case1' ;
WORKING_DIRECTORY         (idx, [1: 29])  = '/home/jsmith818/Research_jake' ;
HOSTNAME                  (idx, [1: 28])  = 'ME04L0358GRD09.me.gatech.edu' ;
CPU_TYPE                  (idx, [1: 36])  = '12th Gen Intel(R) Core(TM) i9-12900K' ;
CPU_MHZ                   (idx, 1)        = 26.0 ;
START_DATE                (idx, [1: 24])  = 'Thu Sep  7 19:14:59 2023' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Sep  7 19:34:46 2023' ;

% Run parameters:

POP                       (idx, 1)        = 20000 ;
CYCLES                    (idx, 1)        = 260 ;
SKIP                      (idx, 1)        = 40 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1694128499910 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;

CRIT_SPEC_MODE            (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
DOUBLE_INDEXING           (idx, 1)        = 0 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 6 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:   6]) = [  1.00281E+00  9.97633E-01  9.99119E-01  1.00086E+00  9.99314E-01  1.00027E+00  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 62])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7u.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 58])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 58])  = '/home/dkotlyar6/Codes/data_libraries/endfb7/sss_endfb7.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 3.2E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.23608E-01 3.9E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  6.76392E-01 1.9E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  2.64805E-01 7.2E-05  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  2.63888E-01 7.2E-05  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  6.35597E+00 0.00036  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  4.56948E+01 0.00019  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  4.56948E+01 0.00019  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.27465E+02 0.00024  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  8.00533E+01 0.00024  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 260 ;
SIMULATED_HISTORIES       (idx, 1)        = 5200615 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  2.00024E+04 0.00058 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  2.00024E+04 0.00058 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  1.17029E+02 ;
RUNNING_TIME              (idx, 1)        =  1.97742E+01 ;
INIT_TIME                 (idx, [1:  2])  = [  7.65233E-01  7.65233E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.98333E-03  1.98333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.90069E+01  1.90069E+01  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.97741E+01  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 5.91826 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  5.99972E+00 2.3E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.80088E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 31798.27 ;
ALLOC_MEMSIZE             (idx, 1)        = 1224.16;
MEMSIZE                   (idx, 1)        = 1125.71;
XS_MEMSIZE                (idx, 1)        = 914.33;
MAT_MEMSIZE               (idx, 1)        = 75.83;
RES_MEMSIZE               (idx, 1)        = 1.83;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 133.72;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 98.45;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 3 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 230535 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.26000E-03 ;
URES_EMAX                 (idx, 1)        =  4.00000E-01 ;
URES_AVAIL                (idx, 1)        = 37 ;
URES_USED                 (idx, 1)        = 37 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 79 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 79 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 1736 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 1 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Energy deposition:

EDEP_MODE                 (idx, 1)        = 0 ;
EDEP_DELAYED              (idx, 1)        = 1 ;
EDEP_KEFF_CORR            (idx, 1)        = 1 ;
EDEP_LOCAL_EGD            (idx, 1)        = 0 ;
EDEP_COMP                 (idx, [1:  9])  = [ 0 0 0 0 0 0 0 0 0 ];
EDEP_CAPT_E               (idx, 1)        =  0.00000E+00 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  0.00000E+00 ;
TOT_DECAY_HEAT            (idx, 1)        =  0.00000E+00 ;
TOT_SF_RATE               (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  0.00000E+00 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  0.00000E+00 ;
INGESTION_TOXICITY        (idx, 1)        =  0.00000E+00 ;
ACTINIDE_INH_TOX          (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ING_TOX          (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_INH_TOX   (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ING_TOX   (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
PHOTON_DECAY_SOURCE       (idx, 1)        =  0.00000E+00 ;
NEUTRON_DECAY_SOURCE      (idx, 1)        =  0.00000E+00 ;
ALPHA_DECAY_SOURCE        (idx, 1)        =  0.00000E+00 ;
ELECTRON_DECAY_SOURCE     (idx, 1)        =  0.00000E+00 ;

% Normalization coefficient:

NORM_COEF                 (idx, [1:   4]) = [  2.98513E+08 0.00051  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  3.63840E-01 0.00104 ];
TH232_FISS                (idx, [1:   4]) = [  1.15703E+06 1.00000  3.71143E-07 1.00000 ];
U235_FISS                 (idx, [1:   4]) = [  3.03250E+12 0.00056  9.83945E-01 7.3E-05 ];
U238_FISS                 (idx, [1:   4]) = [  4.94808E+10 0.00455  1.60541E-02 0.00448 ];
TH232_CAPT                (idx, [1:   4]) = [  1.15897E+08 0.09476  4.00838E-05 0.09498 ];
U235_CAPT                 (idx, [1:   4]) = [  9.76400E+11 0.00107  3.37689E-01 0.00091 ];
U238_CAPT                 (idx, [1:   4]) = [  1.45856E+12 0.00107  5.04419E-01 0.00065 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 5200615 5.20000E+06 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.81451E+03 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 5200615 5.20281E+06 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 2517366 2.51842E+06 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 2683249 2.68440E+06 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 5200615 5.20281E+06 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 1.24797E-07 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.00000E+02 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  1.83638E-41 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  7.54210E+12 2.9E-06 ];
TOT_FISSRATE              (idx, [1:   2]) = [  3.08457E+12 2.8E-07 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  2.89083E+12 0.00053 ];
TOT_ABSRATE               (idx, [1:   2]) = [  5.97541E+12 0.00026 ];
TOT_SRCRATE               (idx, [1:   2]) = [  5.97026E+12 0.00051 ];
TOT_FLUX                  (idx, [1:   2]) = [  1.02922E+15 0.00048 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  5.97541E+12 0.00026 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  2.72943E+14 0.00042 ];
INI_FMASS                 (idx, 1)        =  5.44548E+36 ;
TOT_FMASS                 (idx, 1)        =  5.44548E+36 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.98193E+00 0.00034 ];
SIX_FF_F                  (idx, [1:   2]) = [  9.67281E-01 0.00014 ];
SIX_FF_P                  (idx, [1:   2]) = [  3.27364E-01 0.00063 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  2.01147E+00 0.00059 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.26225E+00 0.00040 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.26225E+00 0.00040 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44510E+00 3.1E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02346E+02 2.8E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.26227E+00 0.00042  1.25391E+00 0.00041  8.34379E-03 0.00706 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.26288E+00 0.00026 ];
COL_KEFF                  (idx, [1:   2]) = [  1.26336E+00 0.00051 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.26288E+00 0.00026 ];
ABS_KINF                  (idx, [1:   2]) = [  1.26288E+00 0.00026 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.54022E+01 0.00019 ];
IMP_ALF                   (idx, [1:   2]) = [  1.53990E+01 0.00012 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  4.09634E-06 0.00286 ];
IMP_EALF                  (idx, [1:   2]) = [  4.10676E-06 0.00182 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  8.41657E-02 0.00348 ];
IMP_AFGE                  (idx, [1:   2]) = [  8.39152E-02 0.00079 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  5.29187E-03 0.00479  1.65610E-04 0.03140  8.63052E-04 0.01358  8.50721E-04 0.01441  2.44265E-03 0.00724  7.18755E-04 0.01560  2.51081E-04 0.02366 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  7.67327E-01 0.01243  1.23465E-02 0.00671  3.17776E-02 0.00011  1.09592E-01 0.00015  3.17972E-01 0.00011  1.35157E+00 9.9E-05  8.70372E+00 0.00089 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.59323E-03 0.00831  2.11641E-04 0.04929  1.10133E-03 0.02117  1.05568E-03 0.02185  3.04137E-03 0.01203  8.71703E-04 0.02366  3.11499E-04 0.03685 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  7.60661E-01 0.01924  1.24906E-02 1.3E-06  3.17797E-02 0.00016  1.09576E-01 0.00018  3.17928E-01 0.00018  1.35173E+00 0.00014  8.71072E+00 0.00133 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  2.37307E-05 0.00111  2.37242E-05 0.00111  2.47061E-05 0.01149 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.99532E-05 0.00102  2.99450E-05 0.00102  3.11869E-05 0.01150 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.61694E-03 0.00714  2.05027E-04 0.04818  1.07109E-03 0.01857  1.05346E-03 0.02016  3.03941E-03 0.01079  9.22062E-04 0.02093  3.25893E-04 0.03157 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  7.86778E-01 0.01651  1.24906E-02 1.1E-06  3.17763E-02 0.00016  1.09585E-01 0.00020  3.18031E-01 0.00017  1.35144E+00 0.00014  8.71578E+00 0.00145 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  2.37711E-05 0.00217  2.37614E-05 0.00218  2.51819E-05 0.02905 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  3.00049E-05 0.00217  2.99927E-05 0.00218  3.17843E-05 0.02904 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.47634E-03 0.02257  1.86552E-04 0.12603  1.04909E-03 0.06044  1.01967E-03 0.05285  3.04121E-03 0.03242  8.70378E-04 0.06076  3.09437E-04 0.09488 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  7.79153E-01 0.05112  1.24906E-02 3.6E-06  3.17722E-02 0.00045  1.09609E-01 0.00049  3.17909E-01 0.00045  1.35044E+00 0.00045  8.67329E+00 0.00203 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.44121E-03 0.02221  1.86477E-04 0.11955  1.05664E-03 0.05594  1.02071E-03 0.05300  2.98813E-03 0.02993  8.86269E-04 0.05869  3.02978E-04 0.09077 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  7.76676E-01 0.04836  1.24906E-02 3.5E-06  3.17701E-02 0.00045  1.09599E-01 0.00047  3.17892E-01 0.00042  1.35027E+00 0.00045  8.67002E+00 0.00189 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -2.73344E+02 0.02293 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  2.37452E-05 0.00065 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.99714E-05 0.00045 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.57942E-03 0.00394 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -2.77115E+02 0.00399 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.19228E-07 0.00077 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.30562E-05 0.00074  1.30560E-05 0.00074  1.30677E-05 0.00886 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  4.02936E-05 0.00068  4.02939E-05 0.00069  4.02234E-05 0.00848 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  3.36241E-01 0.00062  3.35735E-01 0.00063  4.34042E-01 0.01051 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.06190E+01 0.01289 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  4.56948E+01 0.00019  4.87095E+01 0.00027 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  2])  = 'F1' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  1.60975E+05 0.00444  7.21800E+05 0.00162  1.62543E+06 0.00107  3.01066E+06 0.00097  3.44240E+06 0.00050  3.42425E+06 0.00070  3.12698E+06 0.00063  2.74558E+06 0.00066  2.35550E+06 0.00053  2.03143E+06 0.00079  1.79001E+06 0.00037  1.64552E+06 0.00082  1.48190E+06 0.00089  1.39260E+06 0.00074  1.32246E+06 0.00101  1.12901E+06 0.00088  1.08513E+06 0.00103  1.06945E+06 0.00099  1.03238E+06 0.00114  1.93177E+06 0.00070  1.68412E+06 0.00053  1.11834E+06 0.00103  6.58814E+05 0.00156  6.81607E+05 0.00131  5.56527E+05 0.00107  4.74850E+05 0.00115  6.95039E+05 0.00180  1.62299E+05 0.00240  2.14081E+05 0.00193  2.06121E+05 0.00241  1.21690E+05 0.00223  2.19344E+05 0.00224  1.49079E+05 0.00294  1.23054E+05 0.00305  2.30194E+04 0.00619  2.24307E+04 0.00486  2.32458E+04 0.00530  2.41373E+04 0.00536  2.39709E+04 0.00544  2.37102E+04 0.00788  2.43601E+04 0.00653  2.30171E+04 0.00601  4.36443E+04 0.00462  7.02544E+04 0.00243  8.91470E+04 0.00275  2.31464E+05 0.00375  2.29788E+05 0.00195  2.17891E+05 0.00130  1.20960E+05 0.00328  7.62081E+04 0.00386  5.30169E+04 0.00374  5.47765E+04 0.00403  8.70662E+04 0.00456  9.39199E+04 0.00275  1.38375E+05 0.00244  1.54285E+05 0.00224  1.69603E+05 0.00296  8.87010E+04 0.00433  5.78336E+04 0.00282  3.94082E+04 0.00466  3.42064E+04 0.00508  3.21895E+04 0.00269  2.62371E+04 0.00484  1.71995E+04 0.00786  1.55407E+04 0.00715  1.34190E+04 0.00716  1.09062E+04 0.00878  8.04929E+03 0.00980  4.65110E+03 0.00981  1.30353E+03 0.01151 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.29649E+00 0.00068 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  6.59902E+14 0.00059  2.60530E+13 0.00093 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  2.95716E-01 0.00011  4.24489E-01 0.00054 ];
INF_CAPT                  (idx, [1:   4]) = [  3.60815E-03 0.00053  1.37278E-02 0.00062 ];
INF_ABS                   (idx, [1:   4]) = [  5.95398E-03 0.00040  7.27139E-02 0.00060 ];
INF_FISS                  (idx, [1:   4]) = [  2.34582E-03 0.00031  5.89861E-02 0.00060 ];
INF_NSF                   (idx, [1:   4]) = [  5.75534E-03 0.00030  1.43731E-01 0.00060 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.45344E+00 6.1E-06  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.02421E+02 5.9E-07  2.02270E+02 5.5E-09 ];
INF_INVV                  (idx, [1:   4]) = [  4.47233E-08 0.00061  1.78948E-06 0.00036 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  2.89769E-01 0.00011  3.51724E-01 0.00049 ];
INF_SCATT1                (idx, [1:   4]) = [  2.84135E-02 0.00058  1.82950E-02 0.00351 ];
INF_SCATT2                (idx, [1:   4]) = [  7.55613E-03 0.00156  2.95762E-03 0.01821 ];
INF_SCATT3                (idx, [1:   4]) = [  1.48169E-03 0.00583  1.12310E-03 0.02895 ];
INF_SCATT4                (idx, [1:   4]) = [  5.64087E-04 0.01329  5.02217E-04 0.10421 ];
INF_SCATT5                (idx, [1:   4]) = [  2.98544E-04 0.02969  2.96779E-04 0.15497 ];
INF_SCATT6                (idx, [1:   4]) = [  2.20950E-04 0.02091  1.97694E-04 0.15410 ];
INF_SCATT7                (idx, [1:   4]) = [  4.48535E-05 0.12902  1.02524E-04 0.46100 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  2.89773E-01 0.00011  3.51724E-01 0.00049 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.84135E-02 0.00058  1.82950E-02 0.00351 ];
INF_SCATTP2               (idx, [1:   4]) = [  7.55622E-03 0.00156  2.95762E-03 0.01821 ];
INF_SCATTP3               (idx, [1:   4]) = [  1.48167E-03 0.00582  1.12310E-03 0.02895 ];
INF_SCATTP4               (idx, [1:   4]) = [  5.64070E-04 0.01329  5.02217E-04 0.10421 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.98552E-04 0.02968  2.96779E-04 0.15497 ];
INF_SCATTP6               (idx, [1:   4]) = [  2.20919E-04 0.02091  1.97694E-04 0.15410 ];
INF_SCATTP7               (idx, [1:   4]) = [  4.48407E-05 0.12932  1.02524E-04 0.46100 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.31809E-01 0.00013  3.97157E-01 0.00053 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.43796E+00 0.00013  8.39301E-01 0.00053 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  5.94961E-03 0.00041  7.27139E-02 0.00060 ];
INF_REMXS                 (idx, [1:   4]) = [  7.13583E-03 0.00033  8.76142E-02 0.00113 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_YIELD          (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM147_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM148M_MICRO_ABS      (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison decay constants:

PM147_LAMBDA              (idx, 1)        =  8.37254E-09 ;
PM148_LAMBDA              (idx, 1)        =  1.49451E-06 ;
PM148M_LAMBDA             (idx, 1)        =  1.94297E-07 ;
PM149_LAMBDA              (idx, 1)        =  3.62737E-06 ;
I135_LAMBDA               (idx, 1)        =  2.93061E-05 ;
XE135_LAMBDA              (idx, 1)        =  2.10657E-05 ;
XE135M_LAMBDA             (idx, 1)        =  7.55556E-04 ;
I135_BR                   (idx, 1)        =  9.01450E-01 ;

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  2.88581E-01 0.00011  1.18811E-03 0.00149  1.48497E-02 0.00212  3.36875E-01 0.00054 ];
INF_S1                    (idx, [1:   8]) = [  2.85619E-02 0.00056 -1.48410E-04 0.00725 -1.45348E-03 0.01355  1.97485E-02 0.00340 ];
INF_S2                    (idx, [1:   8]) = [  7.59498E-03 0.00154 -3.88514E-05 0.01802 -5.83977E-04 0.01861  3.54159E-03 0.01589 ];
INF_S3                    (idx, [1:   8]) = [  1.50326E-03 0.00584 -2.15723E-05 0.02011 -2.15087E-04 0.03769  1.33819E-03 0.02694 ];
INF_S4                    (idx, [1:   8]) = [  5.73748E-04 0.01303 -9.66129E-06 0.05425 -1.16468E-04 0.07158  6.18685E-04 0.08619 ];
INF_S5                    (idx, [1:   8]) = [  3.02938E-04 0.02986 -4.39409E-06 0.07359 -5.85664E-05 0.13283  3.55345E-04 0.11825 ];
INF_S6                    (idx, [1:   8]) = [  2.23115E-04 0.02083 -2.16522E-06 0.18102 -4.17117E-05 0.17405  2.39405E-04 0.13701 ];
INF_S7                    (idx, [1:   8]) = [  4.69578E-05 0.12275 -2.10422E-06 0.17185 -3.20059E-05 0.15055  1.34530E-04 0.35782 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  2.88585E-01 0.00011  1.18811E-03 0.00149  1.48497E-02 0.00212  3.36875E-01 0.00054 ];
INF_SP1                   (idx, [1:   8]) = [  2.85619E-02 0.00056 -1.48410E-04 0.00725 -1.45348E-03 0.01355  1.97485E-02 0.00340 ];
INF_SP2                   (idx, [1:   8]) = [  7.59507E-03 0.00154 -3.88514E-05 0.01802 -5.83977E-04 0.01861  3.54159E-03 0.01589 ];
INF_SP3                   (idx, [1:   8]) = [  1.50324E-03 0.00584 -2.15723E-05 0.02011 -2.15087E-04 0.03769  1.33819E-03 0.02694 ];
INF_SP4                   (idx, [1:   8]) = [  5.73732E-04 0.01303 -9.66129E-06 0.05425 -1.16468E-04 0.07158  6.18685E-04 0.08619 ];
INF_SP5                   (idx, [1:   8]) = [  3.02946E-04 0.02985 -4.39409E-06 0.07359 -5.85664E-05 0.13283  3.55345E-04 0.11825 ];
INF_SP6                   (idx, [1:   8]) = [  2.23085E-04 0.02084 -2.16522E-06 0.18102 -4.17117E-05 0.17405  2.39405E-04 0.13701 ];
INF_SP7                   (idx, [1:   8]) = [  4.69449E-05 0.12303 -2.10422E-06 0.17185 -3.20059E-05 0.15055  1.34530E-04 0.35782 ];

% Micro-group spectrum:

B1_MICRO_FLX              (idx, [1: 140]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectra in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS_FLX               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM147_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM148M_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Additional diffusion parameters:

CMM_TRANSPXS              (idx, [1:   4]) = [  1.12082E-01 0.00062  1.76249E-01 0.00275 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  1.14511E-01 0.00054  1.79085E-01 0.00622 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  1.14589E-01 0.00057  1.77396E-01 0.00648 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  1.07454E-01 0.00158  1.72603E-01 0.00644 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  2.97403E+00 0.00062  1.89143E+00 0.00273 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  2.91093E+00 0.00054  1.86216E+00 0.00612 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  2.90897E+00 0.00057  1.87998E+00 0.00643 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  3.10220E+00 0.00160  1.93216E+00 0.00638 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  6.59323E-03 0.00831  2.11641E-04 0.04929  1.10133E-03 0.02117  1.05568E-03 0.02185  3.04137E-03 0.01203  8.71703E-04 0.02366  3.11499E-04 0.03685 ];
LAMBDA                    (idx, [1:  14]) = [  7.60661E-01 0.01924  1.24906E-02 1.3E-06  3.17797E-02 0.00016  1.09576E-01 0.00018  3.17928E-01 0.00018  1.35173E+00 0.00014  8.71072E+00 0.00133 ];

