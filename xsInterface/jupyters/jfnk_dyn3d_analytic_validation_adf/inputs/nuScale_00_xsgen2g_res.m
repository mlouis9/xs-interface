
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.31' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct  5 2020 15:48:35' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 30])  = 'NuScale full core ARO fixed TH' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 18])  = 'NuScale_00_xsgen2g' ;
WORKING_DIRECTORY         (idx, [1: 61])  = '/home/bilodid/MCSAFER/fuel_reflector/05-NuScale-xs_fuel_ref2D' ;
HOSTNAME                  (idx, [1: 14])  = 'csk028.cluster' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581576.0 ;
START_DATE                (idx, [1: 24])  = 'Mon Feb 15 12:38:52 2021' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Tue Feb 16 00:11:03 2021' ;

% Run parameters:

POP                       (idx, 1)        = 1000000 ;
CYCLES                    (idx, 1)        = 2000 ;
SKIP                      (idx, 1)        = 100 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1613389132675 ;
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

MPI_TASKS                 (idx, 1)        = 10 ;
OMP_THREADS               (idx, 1)        = 8 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:   8]) = [  1.00010E+00  1.00145E+00  1.00074E+00  9.97236E-01  1.00196E+00  1.00016E+00  1.00127E+00  9.97092E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 55])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.68192E-01 2.0E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  6.31808E-01 1.2E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.50783E-01 8.2E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  5.39340E-01 7.7E-06  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  5.87350E+00 1.7E-05  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.15662E+01 1.5E-05  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.15662E+01 1.5E-05  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  2.69613E+01 2.3E-05  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  5.20709E+01 1.8E-05  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 2000 ;
SIMULATED_HISTORIES       (idx, 1)        = 200001916 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.00001E+05 0.00004 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00001E+05 0.00004 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.13227E+03 ;
RUNNING_TIME              (idx, 1)        =  6.92184E+02 ;
INIT_TIME                 (idx, [1:  2])  = [  3.43433E-01  3.43433E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.10667E-02  1.10667E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  6.91829E+02  6.91829E+02  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  2.41393E+02  2.41386E+02 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.50773E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 3.08050 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.99830E+00 0.00122 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  6.34446E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 385645.68 ;
ALLOC_MEMSIZE             (idx, 1)        = 2834.30;
MEMSIZE                   (idx, 1)        = 2710.76;
XS_MEMSIZE                (idx, 1)        = 1492.65;
MAT_MEMSIZE               (idx, 1)        = 305.87;
RES_MEMSIZE               (idx, 1)        = 243.97;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 668.27;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 123.54;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 181 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 416982 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 35 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 65 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 65 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 1814 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.20282E+10 2.5E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  4.66778E-01 5.6E-05 ];
U235_FISS                 (idx, [1:   4]) = [  1.33223E+15 2.8E-05  9.39865E-01 8.4E-06 ];
U238_FISS                 (idx, [1:   4]) = [  8.52404E+13 0.00014  6.01350E-02 0.00013 ];
U235_CAPT                 (idx, [1:   4]) = [  3.07880E+14 7.1E-05  1.72017E-01 6.6E-05 ];
U238_CAPT                 (idx, [1:   4]) = [  7.65618E+14 5.2E-05  4.27760E-01 3.5E-05 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 2000025557 2.00000E+09 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.79743E+06 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 2000025557 2.00280E+09 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 1116086153 1.11766E+09 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 883939404 8.85142E+08 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 2000025557 2.00280E+09 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 7.39098E-06 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  4.60000E+04 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  3.48723E+15 5.6E-07 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.41751E+15 6.2E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  1.78982E+15 2.5E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  3.20732E+15 1.4E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  3.20282E+15 2.5E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  1.52419E+17 2.6E-05 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  3.20732E+15 1.4E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.01234E+17 2.3E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.65376E+00 2.2E-05 ];
SIX_FF_F                  (idx, [1:   2]) = [  8.11873E-01 1.4E-05 ];
SIX_FF_P                  (idx, [1:   2]) = [  6.14496E-01 1.8E-05 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.31966E+00 1.9E-05 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.08878E+00 2.5E-05 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.08878E+00 2.5E-05 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46011E+00 6.1E-07 ];
FISSE                     (idx, [1:   2]) = [  2.02545E+02 6.2E-08 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.08877E+00 2.6E-05  1.08128E-02 2.5E-05  7.49811E-05 0.00040 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.08881E+00 2.4E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.71522E+01 9.6E-06 ];
IMP_ALF                   (idx, [1:   2]) = [  1.71522E+01 4.5E-06 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  7.11283E-07 0.00017 ];
IMP_EALF                  (idx, [1:   2]) = [  7.11111E-07 7.7E-05 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.08989E-01 0.00014 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.08971E-01 5.7E-05 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  6.54202E-03 0.00027  2.08845E-04 0.00149  1.11713E-03 0.00065  1.08873E-03 0.00065  2.52902E-03 0.00043  1.12866E-03 0.00064  4.69646E-04 0.00099 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  5.00805E-01 0.00038  1.33549E-02 8.2E-06  3.26029E-02 8.3E-06  1.21075E-01 4.4E-06  3.05841E-01 1.0E-05  8.61666E-01 1.7E-05  2.89435E+00 2.8E-05 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.95012E-03 0.00039  2.22157E-04 0.00221  1.18475E-03 0.00097  1.15687E-03 0.00098  2.68603E-03 0.00063  1.20044E-03 0.00095  4.99870E-04 0.00149 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  5.01347E-01 0.00058  1.33549E-02 1.2E-05  3.26021E-02 1.2E-05  1.21077E-01 6.6E-06  3.05858E-01 1.6E-05  8.61725E-01 2.6E-05  2.89458E+00 4.1E-05 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.87236E-05 5.7E-05  1.87130E-05 5.7E-05  2.02473E-05 0.00056 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.03854E-05 5.0E-05  2.03739E-05 5.1E-05  2.20444E-05 0.00056 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.88688E-03 0.00041  2.19947E-04 0.00230  1.17530E-03 0.00099  1.14498E-03 0.00101  2.66087E-03 0.00066  1.19034E-03 0.00098  4.95446E-04 0.00153 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  5.01464E-01 0.00059  1.33550E-02 1.3E-05  3.26019E-02 1.3E-05  1.21076E-01 6.9E-06  3.05852E-01 1.6E-05  8.61733E-01 2.7E-05  2.89457E+00 4.3E-05 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.90459E-05 0.00013  1.90352E-05 0.00013  2.05790E-05 0.00142 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.07363E-05 0.00013  2.07247E-05 0.00013  2.24053E-05 0.00142 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.89471E-03 0.00128  2.20441E-04 0.00723  1.17517E-03 0.00312  1.13924E-03 0.00314  2.67363E-03 0.00207  1.19115E-03 0.00308  4.95085E-04 0.00478 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  5.01307E-01 0.00184  1.33545E-02 3.5E-05  3.26020E-02 4.0E-05  1.21075E-01 2.2E-05  3.05856E-01 5.0E-05  8.61819E-01 8.5E-05  2.89455E+00 0.00013 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.89164E-03 0.00124  2.20203E-04 0.00704  1.17516E-03 0.00303  1.13958E-03 0.00306  2.67040E-03 0.00202  1.19074E-03 0.00299  4.95556E-04 0.00466 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  5.01563E-01 0.00180  1.33544E-02 3.5E-05  3.26023E-02 3.9E-05  1.21075E-01 2.1E-05  3.05849E-01 4.9E-05  8.61824E-01 8.3E-05  2.89457E+00 0.00013 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.62336E+02 0.00128 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.89151E-05 3.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.05939E-05 2.6E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.90554E-03 0.00025 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.65091E+02 0.00025 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.45257E-07 3.0E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.03705E-06 2.7E-05  3.03749E-06 2.7E-05  2.97834E-06 0.00031 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.29331E-05 3.0E-05  2.29325E-05 3.1E-05  2.30153E-05 0.00034 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  6.15294E-01 1.8E-05  6.14761E-01 1.8E-05  6.97254E-01 0.00043 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.04895E+01 0.00062 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.15662E+01 1.5E-05  3.21798E+01 1.9E-05 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  3])  = 'C02' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  0.00000E+00  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.53000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  1.00000E+37 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  3.91019E+07 0.00018  1.60252E+08 0.00012  3.34729E+08 6.0E-05  3.69561E+08 4.4E-05  3.48155E+08 5.4E-05  3.81447E+08 4.4E-05  2.61715E+08 4.5E-05  2.32174E+08 6.1E-05  1.78469E+08 7.1E-05  1.45189E+08 4.7E-05  1.25241E+08 4.9E-05  1.12664E+08 7.0E-05  1.04348E+08 5.2E-05  9.88949E+07 6.9E-05  9.49781E+07 6.0E-05  8.40390E+07 5.1E-05  8.18507E+07 9.3E-05  8.12721E+07 6.4E-05  7.95176E+07 4.7E-05  1.54501E+08 4.7E-05  1.47683E+08 3.4E-05  1.05811E+08 7.0E-05  6.78608E+07 5.7E-05  7.74825E+07 4.9E-05  7.24646E+07 7.6E-05  6.56289E+07 8.7E-05  1.07181E+08 5.5E-05  2.45231E+07 0.00015  3.04134E+07 0.00014  2.74357E+07 6.0E-05  1.58792E+07 0.00012  2.78984E+07 9.3E-05  1.89198E+07 0.00015  1.58969E+07 0.00012  2.99044E+06 0.00025  2.97090E+06 0.00024  3.04501E+06 0.00019  3.14639E+06 0.00028  3.12138E+06 0.00024  3.07247E+06 0.00039  3.18898E+06 0.00026  2.99091E+06 0.00035  5.65212E+06 0.00024  9.01934E+06 0.00022  1.14645E+07 0.00012  3.00118E+07 0.00010  3.10227E+07 0.00011  3.24074E+07 0.00011  2.05100E+07 0.00010  1.42727E+07 8.8E-05  1.07341E+07 8.8E-05  1.21345E+07 0.00015  2.14885E+07 7.5E-05  2.65292E+07 7.7E-05  4.75001E+07 5.3E-05  6.46917E+07 6.1E-05  8.75564E+07 5.3E-05  5.20988E+07 7.2E-05  3.59550E+07 5.1E-05  2.51132E+07 9.8E-05  2.20347E+07 8.3E-05  2.12719E+07 0.00010  1.75880E+07 9.4E-05  1.16356E+07 1.0E-04  1.06715E+07 0.00012  9.38970E+06 0.00014  7.90909E+06 0.00018  6.05486E+06 4.6E-05  3.88556E+06 0.00017  1.31911E+06 0.00029 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.14269E+00 3.0E-05 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  6.97229E+16 2.8E-05  9.50875E+15 1.9E-05 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  5.62874E-01 4.5E-06  1.40468E+00 1.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  7.69235E-03 3.4E-05  5.38726E-02 3.6E-05 ];
INF_ABS                   (idx, [1:   4]) = [  1.10891E-02 2.4E-05  1.24394E-01 2.4E-05 ];
INF_FISS                  (idx, [1:   4]) = [  3.39679E-03 2.0E-05  7.05211E-02 3.2E-05 ];
INF_NSF                   (idx, [1:   4]) = [  8.57592E-03 2.0E-05  1.71839E-01 3.2E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.52471E+00 3.2E-06  2.43670E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03287E+02 2.1E-07  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.64624E-08 1.5E-05  2.28479E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  5.51784E-01 4.9E-06  1.28029E+00 1.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  2.51170E-01 1.3E-05  3.57963E-01 2.1E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  9.91623E-02 1.9E-05  9.41792E-02 6.3E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  7.36589E-03 0.00021  2.95026E-02 0.00016 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.05923E-02 0.00011 -4.69327E-03 0.00082 ];
INF_SCATT5                (idx, [1:   4]) = [  2.25109E-04 0.00443  5.67548E-03 0.00082 ];
INF_SCATT6                (idx, [1:   4]) = [  5.26341E-03 0.00017 -1.29306E-02 0.00039 ];
INF_SCATT7                (idx, [1:   4]) = [  7.57330E-04 0.00105 -2.32233E-04 0.02506 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  5.51824E-01 5.0E-06  1.28029E+00 1.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.51170E-01 1.3E-05  3.57963E-01 2.1E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.91625E-02 1.9E-05  9.41792E-02 6.3E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  7.36589E-03 0.00021  2.95026E-02 0.00016 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.05923E-02 0.00011 -4.69327E-03 0.00082 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.25124E-04 0.00442  5.67548E-03 0.00082 ];
INF_SCATTP6               (idx, [1:   4]) = [  5.26340E-03 0.00017 -1.29306E-02 0.00039 ];
INF_SCATTP7               (idx, [1:   4]) = [  7.57328E-04 0.00105 -2.32233E-04 0.02506 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.28699E-01 1.6E-05  9.23144E-01 1.7E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.45752E+00 1.6E-05  3.61085E-01 1.7E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  1.10496E-02 2.6E-05  1.24394E-01 2.4E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  2.84830E-02 1.3E-05  1.26741E-01 2.5E-05 ];

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

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  3.12030E-09 0.55263 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 2.4E-07  4.40582E-07 0.55256 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  5.34391E-01 4.7E-06  1.73938E-02 2.5E-05  2.35195E-03 0.00027  1.27794E+00 1.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  2.46111E-01 1.3E-05  5.05883E-03 5.4E-05  1.00815E-03 0.00040  3.56955E-01 2.0E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.00691E-01 1.9E-05 -1.52881E-03 0.00015  5.51224E-04 0.00049  9.36280E-02 6.2E-05 ];
INF_S3                    (idx, [1:   8]) = [  9.15929E-03 0.00016 -1.79341E-03 0.00013  2.01770E-04 0.00112  2.93008E-02 0.00016 ];
INF_S4                    (idx, [1:   8]) = [ -1.00093E-02 0.00012 -5.83031E-04 0.00031  8.32433E-06 0.01967 -4.70160E-03 0.00082 ];
INF_S5                    (idx, [1:   8]) = [  2.00405E-04 0.00504  2.47040E-05 0.00466 -7.25377E-05 0.00195  5.74802E-03 0.00082 ];
INF_S6                    (idx, [1:   8]) = [  5.39975E-03 0.00017 -1.36338E-04 0.00094 -9.63275E-05 0.00172 -1.28342E-02 0.00040 ];
INF_S7                    (idx, [1:   8]) = [  9.22636E-04 0.00079 -1.65306E-04 0.00110 -8.93722E-05 0.00172 -1.42861E-04 0.04140 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  5.34430E-01 4.7E-06  1.73938E-02 2.5E-05  2.35195E-03 0.00027  1.27794E+00 1.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  2.46112E-01 1.3E-05  5.05883E-03 5.4E-05  1.00815E-03 0.00040  3.56955E-01 2.0E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.00691E-01 1.9E-05 -1.52881E-03 0.00015  5.51224E-04 0.00049  9.36280E-02 6.2E-05 ];
INF_SP3                   (idx, [1:   8]) = [  9.15930E-03 0.00016 -1.79341E-03 0.00013  2.01770E-04 0.00112  2.93008E-02 0.00016 ];
INF_SP4                   (idx, [1:   8]) = [ -1.00092E-02 0.00012 -5.83031E-04 0.00031  8.32433E-06 0.01967 -4.70160E-03 0.00082 ];
INF_SP5                   (idx, [1:   8]) = [  2.00420E-04 0.00503  2.47040E-05 0.00466 -7.25377E-05 0.00195  5.74802E-03 0.00082 ];
INF_SP6                   (idx, [1:   8]) = [  5.39974E-03 0.00017 -1.36338E-04 0.00094 -9.63275E-05 0.00172 -1.28342E-02 0.00040 ];
INF_SP7                   (idx, [1:   8]) = [  9.22634E-04 0.00079 -1.65306E-04 0.00110 -8.93722E-05 0.00172 -1.42861E-04 0.04140 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  2.46176E-01 3.4E-05  8.28777E-01 0.00016 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  2.51124E-01 7.0E-05  8.34559E-01 0.00024 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  2.51154E-01 5.3E-05  8.34555E-01 0.00026 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  2.36817E-01 5.1E-05  8.17455E-01 0.00030 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  1.35404E+00 3.4E-05  4.02199E-01 0.00016 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  1.32737E+00 7.0E-05  3.99413E-01 0.00024 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  1.32721E+00 5.3E-05  3.99415E-01 0.00026 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  1.40756E+00 5.1E-05  4.07770E-01 0.00030 ];
TRC_TRANSPXS              (idx, [1:   4]) = [  2.41819E-01 1.1E-05  8.86925E-01 1.4E-05 ];
TRC_DIFFCOEF              (idx, [1:   4]) = [  1.37844E+00 1.1E-05  3.75830E-01 1.4E-05 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  6.90140E-03 0.00048  2.21058E-04 0.00273  1.17792E-03 0.00118  1.14824E-03 0.00120  2.66693E-03 0.00077  1.19151E-03 0.00116  4.95754E-04 0.00181 ];
LAMBDA                    (idx, [1:  14]) = [  5.00905E-01 0.00070  1.33546E-02 1.5E-05  3.26037E-02 1.5E-05  1.21073E-01 8.1E-06  3.05821E-01 1.9E-05  8.61568E-01 3.1E-05  2.89381E+00 5.0E-05 ];

% Assembly discontinuity factors (order: W-S-E-N / NW-NE-SE-SW):

DF_SURFACE                (idx, [1:  6])  = 'adf_f1' ;
DF_SYM                    (idx, 1)        = 0 ;
DF_N_SURF                 (idx, 1)        = 4 ;
DF_N_CORN                 (idx, 1)        = 4 ;
DF_VOLUME                 (idx, 1)        =  4.62405E+02 ;
DF_SURF_AREA              (idx, [1:  4])  = [ 2.15036E+01  2.15036E+01  2.15036E+01  2.15036E+01 ];
DF_MID_AREA               (idx, [1:  4])  = [ 2.15036E+00  2.15036E+00  2.15036E+00  2.15036E+00 ];
DF_CORN_AREA              (idx, [1:  4])  = [ 2.15036E+00  2.15036E+00  2.15036E+00  2.15036E+00 ];
DF_SURF_IN_CURR           (idx, [1:  16]) = [  4.55211E+14 0.00030  6.56266E+13 0.00032  4.55839E+14 0.00013  8.67116E+13 0.00019  3.05661E+14 0.00022  2.12168E+13 0.00031  3.92146E+14 0.00032  5.49505E+13 0.00040 ];
DF_SURF_OUT_CURR          (idx, [1:  16]) = [  4.55211E+14 0.00030  6.56266E+13 0.00032  4.44736E+14 0.00017  7.31059E+13 0.00022  3.61279E+14 0.00026  3.86251E+13 0.00023  3.92146E+14 0.00032  5.49505E+13 0.00040 ];
DF_SURF_NET_CURR          (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  1.11030E+13 0.00317  1.36057E+13 0.00080 -5.56182E+13 0.00057 -1.74083E+13 0.00035  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_MID_IN_CURR            (idx, [1:  16]) = [  4.47677E+13 0.00033  6.52473E+12 0.00084  4.59949E+13 0.00022  9.09119E+12 0.00038  2.96540E+13 0.00021  1.96316E+12 0.00113  3.99021E+13 0.00042  5.83963E+12 0.00097 ];
DF_MID_OUT_CURR           (idx, [1:  16]) = [  4.47677E+13 0.00033  6.52473E+12 0.00084  4.50956E+13 0.00034  7.71291E+12 0.00039  3.51655E+13 0.00028  3.74357E+12 0.00089  3.99021E+13 0.00042  5.83963E+12 0.00097 ];
DF_MID_NET_CURR           (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  8.99309E+11 0.01459  1.37829E+12 0.00223 -5.51146E+12 0.00141 -1.78042E+12 0.00128  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_CORN_IN_CURR           (idx, [1:  16]) = [  4.42191E+13 0.00037  6.13226E+12 0.00073  2.95668E+13 0.00046  2.56970E+12 0.00118  3.89564E+13 0.00023  5.05708E+12 0.00082  4.86661E+13 0.00031  8.60280E+12 0.00064 ];
DF_CORN_OUT_CURR          (idx, [1:  16]) = [  4.42191E+13 0.00037  6.13226E+12 0.00073  3.26112E+13 0.00051  3.38791E+12 0.00094  3.93248E+13 0.00030  5.24738E+12 0.00057  4.87634E+13 0.00031  7.91860E+12 0.00058 ];
DF_CORN_NET_CURR          (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 -3.04437E+12 0.00150 -8.18211E+11 0.00178 -3.68407E+11 0.01794 -1.90299E+11 0.01942 -9.72713E+10 0.04349  6.84203E+11 0.00448 ];
DF_HET_VOL_FLUX           (idx, [1:   4]) = [  7.53892E+13 0.00022  1.02809E+13 0.00023 ];
DF_HET_SURF_FLUX          (idx, [1:  16]) = [  8.47140E+13 0.00029  1.25688E+13 0.00031  8.32263E+13 0.00016  1.51881E+13 0.00020  6.21087E+13 0.00025  5.63870E+12 0.00031  7.23255E+13 0.00037  1.05168E+13 0.00052 ];
DF_HET_CORN_FLUX          (idx, [1:  16]) = [  8.17249E+13 0.00040  1.17609E+13 0.00086  5.75995E+13 0.00053  5.65754E+12 0.00139  7.24820E+13 0.00027  9.78280E+12 0.00068  8.98907E+13 0.00040  1.57962E+13 0.00057 ];
DF_HOM_VOL_FLUX           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_HOM_SURF_FLUX          (idx, [1:  16]) = [  8.47537E+13 0.00029  1.18130E+13 0.00028  8.12834E+13 0.00022  1.36194E+13 0.00018  5.78549E+13 0.00026  4.93961E+12 0.00046  7.19983E+13 0.00032  9.60218E+12 0.00032 ];
DF_HOM_CORN_FLUX          (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SURF_DF                (idx, [1:  16]) = [  9.99532E-01 0.00021  1.06398E+00 0.00034  1.02390E+00 0.00017  1.11519E+00 0.00018  1.07353E+00 0.00021  1.14153E+00 0.00047  1.00454E+00 0.00017  1.09525E+00 0.00034 ];
DF_CORN_DF                (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SGN_SURF_IN_CURR       (idx, [1:  16]) = [ -1.34366E+13 0.00292 -3.00571E+12 0.00512 -2.11819E+13 0.00192 -5.40841E+12 0.00218 -2.16135E+13 0.00123 -2.47870E+12 0.00254 -3.61930E+13 0.00111 -5.30753E+12 0.00296 ];
DF_SGN_SURF_OUT_CURR      (idx, [1:  16]) = [ -1.34366E+13 0.00292 -3.00571E+12 0.00512 -3.01535E+13 0.00165 -5.01214E+12 0.00251 -1.88181E+13 0.00158 -3.08214E+12 0.00299 -3.61930E+13 0.00111 -5.30753E+12 0.00296 ];
DF_SGN_SURF_NET_CURR      (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  8.97160E+12 0.00333 -3.96266E+11 0.02803 -2.79541E+12 0.00538  6.03445E+11 0.01019  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SGN_HET_SURF_FLUX      (idx, [1:  16]) = [ -2.38577E+12 0.00416 -5.77164E+11 0.00758 -4.72711E+12 0.00221 -9.92841E+11 0.00290 -3.72941E+12 0.00132 -5.28525E+11 0.00355 -6.67456E+12 0.00145 -1.01751E+12 0.00345 ];
DF_SGN_HOM_SURF_FLUX      (idx, [1:  16]) = [ -2.50093E+12 0.00106 -5.56739E+11 0.00067 -6.97197E+12 0.00048 -1.20339E+12 0.00040 -2.50093E+12 0.00106 -5.56739E+11 0.00067 -6.97197E+12 0.00048 -1.20339E+12 0.00040 ];
DF_SGN_SURF_DF            (idx, [1:  16]) = [  9.53968E-01 0.00440  1.03666E+00 0.00716  6.78016E-01 0.00210  8.25041E-01 0.00305  1.49122E+00 0.00160  9.49332E-01 0.00378  9.57340E-01 0.00122  8.45537E-01 0.00330 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.31' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct  5 2020 15:48:35' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 30])  = 'NuScale full core ARO fixed TH' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 18])  = 'NuScale_00_xsgen2g' ;
WORKING_DIRECTORY         (idx, [1: 61])  = '/home/bilodid/MCSAFER/fuel_reflector/05-NuScale-xs_fuel_ref2D' ;
HOSTNAME                  (idx, [1: 14])  = 'csk028.cluster' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581576.0 ;
START_DATE                (idx, [1: 24])  = 'Mon Feb 15 12:38:52 2021' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Tue Feb 16 00:11:03 2021' ;

% Run parameters:

POP                       (idx, 1)        = 1000000 ;
CYCLES                    (idx, 1)        = 2000 ;
SKIP                      (idx, 1)        = 100 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1613389132675 ;
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

MPI_TASKS                 (idx, 1)        = 10 ;
OMP_THREADS               (idx, 1)        = 8 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:   8]) = [  1.00010E+00  1.00145E+00  1.00074E+00  9.97236E-01  1.00196E+00  1.00016E+00  1.00127E+00  9.97092E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 55])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.68192E-01 2.0E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  6.31808E-01 1.2E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.50783E-01 8.2E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  5.39340E-01 7.7E-06  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  5.87350E+00 1.7E-05  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.15662E+01 1.5E-05  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.15662E+01 1.5E-05  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  2.69613E+01 2.3E-05  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  5.20709E+01 1.8E-05  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 2000 ;
SIMULATED_HISTORIES       (idx, 1)        = 200001916 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.00001E+05 0.00004 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00001E+05 0.00004 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.13227E+03 ;
RUNNING_TIME              (idx, 1)        =  6.92184E+02 ;
INIT_TIME                 (idx, [1:  2])  = [  3.43433E-01  3.43433E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.10667E-02  1.10667E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  6.91829E+02  6.91829E+02  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  2.41393E+02  2.41386E+02 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.50773E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 3.08050 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.99830E+00 0.00122 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  6.34446E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 385645.68 ;
ALLOC_MEMSIZE             (idx, 1)        = 2834.30;
MEMSIZE                   (idx, 1)        = 2710.76;
XS_MEMSIZE                (idx, 1)        = 1492.65;
MAT_MEMSIZE               (idx, 1)        = 305.87;
RES_MEMSIZE               (idx, 1)        = 243.97;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 668.27;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 123.54;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 181 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 416982 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 35 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 65 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 65 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 1814 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.20282E+10 2.5E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  4.66778E-01 5.6E-05 ];
U235_FISS                 (idx, [1:   4]) = [  1.33223E+15 2.8E-05  9.39865E-01 8.4E-06 ];
U238_FISS                 (idx, [1:   4]) = [  8.52404E+13 0.00014  6.01350E-02 0.00013 ];
U235_CAPT                 (idx, [1:   4]) = [  3.07880E+14 7.1E-05  1.72017E-01 6.6E-05 ];
U238_CAPT                 (idx, [1:   4]) = [  7.65618E+14 5.2E-05  4.27760E-01 3.5E-05 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 2000025557 2.00000E+09 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.79743E+06 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 2000025557 2.00280E+09 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 1116086153 1.11766E+09 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 883939404 8.85142E+08 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 2000025557 2.00280E+09 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 7.39098E-06 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  4.60000E+04 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  3.48723E+15 5.6E-07 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.41751E+15 6.2E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  1.78982E+15 2.5E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  3.20732E+15 1.4E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  3.20282E+15 2.5E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  1.52419E+17 2.6E-05 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  3.20732E+15 1.4E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.01234E+17 2.3E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.65376E+00 2.2E-05 ];
SIX_FF_F                  (idx, [1:   2]) = [  8.11873E-01 1.4E-05 ];
SIX_FF_P                  (idx, [1:   2]) = [  6.14496E-01 1.8E-05 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.31966E+00 1.9E-05 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.08878E+00 2.5E-05 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.08878E+00 2.5E-05 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46011E+00 6.1E-07 ];
FISSE                     (idx, [1:   2]) = [  2.02545E+02 6.2E-08 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.08877E+00 2.6E-05  1.08128E-02 2.5E-05  7.49811E-05 0.00040 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.08881E+00 2.4E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.71522E+01 9.6E-06 ];
IMP_ALF                   (idx, [1:   2]) = [  1.71522E+01 4.5E-06 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  7.11283E-07 0.00017 ];
IMP_EALF                  (idx, [1:   2]) = [  7.11111E-07 7.7E-05 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.08989E-01 0.00014 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.08971E-01 5.7E-05 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  6.54202E-03 0.00027  2.08845E-04 0.00149  1.11713E-03 0.00065  1.08873E-03 0.00065  2.52902E-03 0.00043  1.12866E-03 0.00064  4.69646E-04 0.00099 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  5.00805E-01 0.00038  1.33549E-02 8.2E-06  3.26029E-02 8.3E-06  1.21075E-01 4.4E-06  3.05841E-01 1.0E-05  8.61666E-01 1.7E-05  2.89435E+00 2.8E-05 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.95012E-03 0.00039  2.22157E-04 0.00221  1.18475E-03 0.00097  1.15687E-03 0.00098  2.68603E-03 0.00063  1.20044E-03 0.00095  4.99870E-04 0.00149 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  5.01347E-01 0.00058  1.33549E-02 1.2E-05  3.26021E-02 1.2E-05  1.21077E-01 6.6E-06  3.05858E-01 1.6E-05  8.61725E-01 2.6E-05  2.89458E+00 4.1E-05 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.87236E-05 5.7E-05  1.87130E-05 5.7E-05  2.02473E-05 0.00056 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.03854E-05 5.0E-05  2.03739E-05 5.1E-05  2.20444E-05 0.00056 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.88688E-03 0.00041  2.19947E-04 0.00230  1.17530E-03 0.00099  1.14498E-03 0.00101  2.66087E-03 0.00066  1.19034E-03 0.00098  4.95446E-04 0.00153 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  5.01464E-01 0.00059  1.33550E-02 1.3E-05  3.26019E-02 1.3E-05  1.21076E-01 6.9E-06  3.05852E-01 1.6E-05  8.61733E-01 2.7E-05  2.89457E+00 4.3E-05 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.90459E-05 0.00013  1.90352E-05 0.00013  2.05790E-05 0.00142 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.07363E-05 0.00013  2.07247E-05 0.00013  2.24053E-05 0.00142 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.89471E-03 0.00128  2.20441E-04 0.00723  1.17517E-03 0.00312  1.13924E-03 0.00314  2.67363E-03 0.00207  1.19115E-03 0.00308  4.95085E-04 0.00478 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  5.01307E-01 0.00184  1.33545E-02 3.5E-05  3.26020E-02 4.0E-05  1.21075E-01 2.2E-05  3.05856E-01 5.0E-05  8.61819E-01 8.5E-05  2.89455E+00 0.00013 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.89164E-03 0.00124  2.20203E-04 0.00704  1.17516E-03 0.00303  1.13958E-03 0.00306  2.67040E-03 0.00202  1.19074E-03 0.00299  4.95556E-04 0.00466 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  5.01563E-01 0.00180  1.33544E-02 3.5E-05  3.26023E-02 3.9E-05  1.21075E-01 2.1E-05  3.05849E-01 4.9E-05  8.61824E-01 8.3E-05  2.89457E+00 0.00013 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.62336E+02 0.00128 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.89151E-05 3.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.05939E-05 2.6E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.90554E-03 0.00025 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.65091E+02 0.00025 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.45257E-07 3.0E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.03705E-06 2.7E-05  3.03749E-06 2.7E-05  2.97834E-06 0.00031 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.29331E-05 3.0E-05  2.29325E-05 3.1E-05  2.30153E-05 0.00034 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  6.15294E-01 1.8E-05  6.14761E-01 1.8E-05  6.97254E-01 0.00043 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.04895E+01 0.00062 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.15662E+01 1.5E-05  3.21798E+01 1.9E-05 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  3])  = 'B01' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  0.00000E+00  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.53000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  1.00000E+37 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  2.39811E+07 0.00031  9.81163E+07 7.3E-05  2.03781E+08 0.00010  2.22143E+08 5.8E-05  2.06697E+08 8.7E-05  2.24524E+08 6.4E-05  1.53008E+08 8.2E-05  1.35757E+08 0.00010  1.03842E+08 8.0E-05  8.46966E+07 6.8E-05  7.30682E+07 5.5E-05  6.58317E+07 8.1E-05  6.07607E+07 0.00012  5.77403E+07 8.5E-05  5.56695E+07 0.00012  4.91475E+07 9.6E-05  4.79326E+07 8.1E-05  4.75180E+07 7.7E-05  4.66506E+07 6.2E-05  9.09744E+07 5.7E-05  8.75918E+07 9.3E-05  6.31603E+07 0.00011  4.08720E+07 7.2E-05  4.70654E+07 0.00013  4.43554E+07 9.7E-05  4.04295E+07 1.0E-04  6.61433E+07 9.7E-05  1.51452E+07 8.0E-05  1.90016E+07 0.00018  1.72458E+07 0.00015  1.00060E+07 0.00014  1.73956E+07 9.6E-05  1.18210E+07 0.00012  1.00573E+07 0.00016  1.91709E+06 0.00031  1.90569E+06 0.00029  1.95086E+06 0.00034  2.01241E+06 0.00022  1.99385E+06 0.00026  1.96072E+06 0.00036  2.03222E+06 0.00040  1.90700E+06 0.00030  3.60331E+06 0.00030  5.75145E+06 0.00021  7.32295E+06 0.00017  1.93112E+07 0.00012  2.03458E+07 0.00015  2.22270E+07 1.0E-04  1.49904E+07 9.7E-05  1.09000E+07 0.00013  8.50687E+06 0.00020  9.94215E+06 0.00019  1.83426E+07 0.00010  2.35776E+07 9.1E-05  4.45972E+07 0.00011  6.38028E+07 6.5E-05  9.05876E+07 0.00010  5.54542E+07 8.3E-05  3.88784E+07 0.00011  2.74250E+07 7.0E-05  2.42418E+07 6.9E-05  2.35525E+07 0.00010  1.95834E+07 0.00014  1.30093E+07 7.8E-05  1.19607E+07 6.6E-05  1.05754E+07 0.00014  8.93683E+06 0.00016  6.84819E+06 0.00016  4.40313E+06 0.00014  1.48798E+06 0.00027 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.13757E+00 3.2E-05 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  4.15373E+16 6.1E-05  9.19491E+15 6.7E-05 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  5.60319E-01 1.1E-05  1.36523E+00 1.8E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  6.95328E-03 5.6E-05  3.33133E-02 1.8E-05 ];
INF_ABS                   (idx, [1:   4]) = [  9.26875E-03 4.3E-05  7.83320E-02 2.1E-05 ];
INF_FISS                  (idx, [1:   4]) = [  2.31547E-03 2.9E-05  4.50187E-02 2.6E-05 ];
INF_NSF                   (idx, [1:   4]) = [  5.93931E-03 3.0E-05  1.09697E-01 2.6E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.56506E+00 3.7E-06  2.43670E+00 5.6E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.03826E+02 3.9E-07  2.02270E+02 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.89392E-08 4.5E-05  2.41897E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  5.51051E-01 1.2E-05  1.28690E+00 2.0E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  2.50778E-01 1.2E-05  3.46798E-01 2.0E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  9.90765E-02 2.3E-05  8.87197E-02 8.4E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  7.55423E-03 0.00019  2.77856E-02 0.00026 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.04544E-02 0.00015 -5.35629E-03 0.00094 ];
INF_SCATT5                (idx, [1:   4]) = [  2.23607E-04 0.00742  6.02450E-03 0.00079 ];
INF_SCATT6                (idx, [1:   4]) = [  5.22397E-03 0.00029 -1.33721E-02 0.00027 ];
INF_SCATT7                (idx, [1:   4]) = [  7.67033E-04 0.00240  1.45243E-04 0.02305 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  5.51092E-01 1.1E-05  1.28690E+00 2.0E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  2.50779E-01 1.2E-05  3.46798E-01 2.0E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  9.90767E-02 2.3E-05  8.87197E-02 8.4E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  7.55425E-03 0.00019  2.77856E-02 0.00026 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.04544E-02 0.00015 -5.35629E-03 0.00094 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.23602E-04 0.00745  6.02450E-03 0.00079 ];
INF_SCATTP6               (idx, [1:   4]) = [  5.22395E-03 0.00029 -1.33721E-02 0.00027 ];
INF_SCATTP7               (idx, [1:   4]) = [  7.67046E-04 0.00240  1.45243E-04 0.02305 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.27139E-01 2.3E-05  9.03764E-01 1.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.46753E+00 2.3E-05  3.68828E-01 1.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  9.22776E-03 4.2E-05  7.83320E-02 2.1E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  2.76159E-02 2.6E-05  7.99218E-02 3.0E-05 ];

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

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 3.9E-09  5.55664E-09 0.40825 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  9.99999E-01 3.2E-07  7.78553E-07 0.40825 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  5.32703E-01 1.1E-05  1.83473E-02 3.6E-05  1.59035E-03 0.00026  1.28531E+00 2.0E-05 ];
INF_S1                    (idx, [1:   8]) = [  2.45421E-01 1.2E-05  5.35701E-03 7.8E-05  6.76837E-04 0.00050  3.46121E-01 2.0E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.00654E-01 2.2E-05 -1.57793E-03 0.00019  3.68994E-04 0.00080  8.83508E-02 8.5E-05 ];
INF_S3                    (idx, [1:   8]) = [  9.43775E-03 0.00016 -1.88353E-03 0.00014  1.33868E-04 0.00134  2.76517E-02 0.00026 ];
INF_S4                    (idx, [1:   8]) = [ -9.82613E-03 0.00016 -6.28287E-04 0.00016  4.43040E-06 0.05857 -5.36072E-03 0.00090 ];
INF_S5                    (idx, [1:   8]) = [  2.08446E-04 0.00816  1.51612E-05 0.01065 -4.93667E-05 0.00292  6.07387E-03 0.00077 ];
INF_S6                    (idx, [1:   8]) = [  5.37001E-03 0.00027 -1.46044E-04 0.00156 -6.49052E-05 0.00325 -1.33072E-02 0.00027 ];
INF_S7                    (idx, [1:   8]) = [  9.40444E-04 0.00197 -1.73411E-04 0.00108 -5.98418E-05 0.00192  2.05085E-04 0.01609 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  5.32744E-01 1.1E-05  1.83473E-02 3.6E-05  1.59035E-03 0.00026  1.28531E+00 2.0E-05 ];
INF_SP1                   (idx, [1:   8]) = [  2.45422E-01 1.2E-05  5.35701E-03 7.8E-05  6.76837E-04 0.00050  3.46121E-01 2.0E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.00655E-01 2.2E-05 -1.57793E-03 0.00019  3.68994E-04 0.00080  8.83508E-02 8.5E-05 ];
INF_SP3                   (idx, [1:   8]) = [  9.43778E-03 0.00016 -1.88353E-03 0.00014  1.33868E-04 0.00134  2.76517E-02 0.00026 ];
INF_SP4                   (idx, [1:   8]) = [ -9.82613E-03 0.00016 -6.28287E-04 0.00016  4.43040E-06 0.05857 -5.36072E-03 0.00090 ];
INF_SP5                   (idx, [1:   8]) = [  2.08441E-04 0.00819  1.51612E-05 0.01065 -4.93667E-05 0.00292  6.07387E-03 0.00077 ];
INF_SP6                   (idx, [1:   8]) = [  5.36999E-03 0.00027 -1.46044E-04 0.00156 -6.49052E-05 0.00325 -1.33072E-02 0.00027 ];
INF_SP7                   (idx, [1:   8]) = [  9.40457E-04 0.00196 -1.73411E-04 0.00108 -5.98418E-05 0.00192  2.05085E-04 0.01609 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  9.35741E-02 6.4E-05  4.20266E-01 0.00015 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  9.56795E-02 4.8E-05  4.29189E-01 0.00018 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  9.56901E-02 0.00011  4.29134E-01 0.00021 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  8.96202E-02 8.3E-05  4.03537E-01 0.00026 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  3.56224E+00 6.4E-05  7.93149E-01 0.00015 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  3.48385E+00 4.8E-05  7.76659E-01 0.00018 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  3.48347E+00 0.00011  7.76758E-01 0.00021 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  3.71940E+00 8.3E-05  8.26029E-01 0.00026 ];
TRC_TRANSPXS              (idx, [1:   4]) = [  2.40516E-01 1.7E-05  8.75380E-01 1.7E-05 ];
TRC_DIFFCOEF              (idx, [1:   4]) = [  1.38591E+00 1.7E-05  3.80787E-01 1.7E-05 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  7.03673E-03 0.00064  2.24108E-04 0.00361  1.19690E-03 0.00157  1.17221E-03 0.00157  2.71998E-03 0.00103  1.21635E-03 0.00155  5.07190E-04 0.00242 ];
LAMBDA                    (idx, [1:  14]) = [  5.02091E-01 0.00093  1.33556E-02 2.0E-05  3.25995E-02 2.0E-05  1.21084E-01 1.1E-05  3.05922E-01 2.5E-05  8.62010E-01 4.2E-05  2.89600E+00 6.8E-05 ];

% Assembly discontinuity factors (order: W-S-E-N / NW-NE-SE-SW):

DF_SURFACE                (idx, [1:  6])  = 'adf_f2' ;
DF_SYM                    (idx, 1)        = 0 ;
DF_N_SURF                 (idx, 1)        = 4 ;
DF_N_CORN                 (idx, 1)        = 4 ;
DF_VOLUME                 (idx, 1)        =  4.62405E+02 ;
DF_SURF_AREA              (idx, [1:  4])  = [ 2.15036E+01  2.15036E+01  2.15036E+01  2.15036E+01 ];
DF_MID_AREA               (idx, [1:  4])  = [ 2.15036E+00  2.15036E+00  2.15036E+00  2.15036E+00 ];
DF_CORN_AREA              (idx, [1:  4])  = [ 2.15036E+00  2.15036E+00  2.15036E+00  2.15036E+00 ];
DF_SURF_IN_CURR           (idx, [1:  16]) = [  5.06209E+14 0.00011  1.11318E+14 0.00020  5.06234E+14 0.00014  1.11265E+14 0.00040  4.44762E+14 0.00019  7.30710E+13 0.00026  4.44736E+14 0.00017  7.31059E+13 0.00022 ];
DF_SURF_OUT_CURR          (idx, [1:  16]) = [  5.06209E+14 0.00011  1.11318E+14 0.00020  5.06234E+14 0.00014  1.11265E+14 0.00040  4.55870E+14 0.00016  8.66909E+13 0.00023  4.55839E+14 0.00013  8.67116E+13 0.00019 ];
DF_SURF_NET_CURR          (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 -1.11077E+13 0.00315 -1.36198E+13 0.00082 -1.11030E+13 0.00317 -1.36057E+13 0.00080 ];
DF_MID_IN_CURR            (idx, [1:  16]) = [  5.07744E+13 0.00017  1.15873E+13 0.00070  5.07766E+13 0.00018  1.15938E+13 0.00082  4.50810E+13 0.00019  7.70322E+12 0.00053  4.50956E+13 0.00034  7.71291E+12 0.00039 ];
DF_MID_OUT_CURR           (idx, [1:  16]) = [  5.07744E+13 0.00017  1.15873E+13 0.00070  5.07766E+13 0.00018  1.15938E+13 0.00082  4.59851E+13 0.00021  9.08808E+12 0.00050  4.59949E+13 0.00022  9.09119E+12 0.00038 ];
DF_MID_NET_CURR           (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 -9.04104E+11 0.00829 -1.38486E+12 0.00238 -8.99309E+11 0.01459 -1.37829E+12 0.00223 ];
DF_CORN_IN_CURR           (idx, [1:  16]) = [  4.85962E+13 0.00029  8.47505E+12 0.00056  3.76620E+13 0.00032  5.11797E+12 0.00073  4.86083E+13 0.00026  8.47329E+12 0.00068  5.24071E+13 0.00012  1.14854E+13 0.00091 ];
DF_CORN_OUT_CURR          (idx, [1:  16]) = [  4.84990E+13 0.00030  9.15925E+12 0.00053  4.11872E+13 0.00022  6.46756E+12 0.00087  4.85125E+13 0.00021  9.15340E+12 0.00055  5.24071E+13 0.00012  1.14854E+13 0.00091 ];
DF_CORN_NET_CURR          (idx, [1:  16]) = [  9.72713E+10 0.04349 -6.84203E+11 0.00448 -3.52523E+12 0.00296 -1.34959E+12 0.00314  9.57357E+10 0.08554 -6.80112E+11 0.00226  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_HET_VOL_FLUX           (idx, [1:   4]) = [  8.98299E+13 5.9E-05  1.98847E+13 6.9E-05 ];
DF_HET_SURF_FLUX          (idx, [1:  16]) = [  9.36690E+13 0.00011  2.10624E+13 0.00016  9.36728E+13 0.00014  2.10467E+13 0.00038  8.32275E+13 0.00020  1.51810E+13 0.00028  8.32263E+13 0.00016  1.51881E+13 0.00020 ];
DF_HET_CORN_FLUX          (idx, [1:  16]) = [  8.97479E+13 0.00029  1.67713E+13 0.00060  7.29201E+13 0.00026  1.10135E+13 0.00068  8.97645E+13 0.00030  1.67508E+13 0.00086  9.66882E+13 0.00022  2.17747E+13 0.00095 ];
DF_HOM_VOL_FLUX           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_HOM_SURF_FLUX          (idx, [1:  16]) = [  9.30563E+13 0.00010  2.09457E+13 0.00010  9.30538E+13 0.00013  2.09448E+13 0.00012  8.42562E+13 0.00016  1.56208E+13 0.00025  8.42603E+13 9.2E-05  1.56250E+13 0.00016 ];
DF_HOM_CORN_FLUX          (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SURF_DF                (idx, [1:  16]) = [  1.00658E+00 0.00012  1.00557E+00 0.00021  1.00665E+00 0.00010  1.00487E+00 0.00034  9.87792E-01 0.00014  9.71843E-01 0.00034  9.87727E-01 0.00019  9.72041E-01 0.00026 ];
DF_CORN_DF                (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SGN_SURF_IN_CURR       (idx, [1:  16]) = [ -1.20531E+13 0.00408 -4.42193E+12 0.00522 -1.19628E+13 0.00361 -4.40271E+12 0.00607 -3.01908E+13 0.00157 -5.06765E+12 0.00341 -3.01535E+13 0.00165 -5.01214E+12 0.00251 ];
DF_SGN_SURF_OUT_CURR      (idx, [1:  16]) = [ -1.20531E+13 0.00408 -4.42193E+12 0.00522 -1.19628E+13 0.00361 -4.40271E+12 0.00607 -2.12121E+13 0.00214 -5.44236E+12 0.00318 -2.11819E+13 0.00192 -5.40841E+12 0.00218 ];
DF_SGN_SURF_NET_CURR      (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 -8.97867E+12 0.00344  3.74708E+11 0.03057 -8.97160E+12 0.00333  3.96266E+11 0.02803 ];
DF_SGN_HET_SURF_FLUX      (idx, [1:  16]) = [ -2.11716E+12 0.00675 -8.44258E+11 0.00744 -2.10126E+12 0.00500 -8.35659E+11 0.00842 -4.73570E+12 0.00203 -1.00302E+12 0.00371 -4.72711E+12 0.00221 -9.92841E+11 0.00290 ];
DF_SGN_HOM_SURF_FLUX      (idx, [1:  16]) = [ -2.38558E+12 0.00115 -8.64913E+11 0.00070 -2.38746E+12 0.00133 -8.65684E+11 0.00093 -2.38558E+12 0.00115 -8.64913E+11 0.00070 -2.38746E+12 0.00133 -8.65684E+11 0.00093 ];
DF_SGN_SURF_DF            (idx, [1:  16]) = [  8.87493E-01 0.00688  9.76097E-01 0.00708  8.80130E-01 0.00493  9.65343E-01 0.00871  1.98513E+00 0.00141  1.15968E+00 0.00369  1.97999E+00 0.00210  1.14689E+00 0.00284 ];


% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.31' ;
COMPILE_DATE              (idx, [1: 20])  = 'Oct  5 2020 15:48:35' ;
DEBUG                     (idx, 1)        = 0 ;
TITLE                     (idx, [1: 30])  = 'NuScale full core ARO fixed TH' ;
CONFIDENTIAL_DATA         (idx, 1)        = 0 ;
INPUT_FILE_NAME           (idx, [1: 18])  = 'NuScale_00_xsgen2g' ;
WORKING_DIRECTORY         (idx, [1: 61])  = '/home/bilodid/MCSAFER/fuel_reflector/05-NuScale-xs_fuel_ref2D' ;
HOSTNAME                  (idx, [1: 14])  = 'csk028.cluster' ;
CPU_TYPE                  (idx, [1: 40])  = 'Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz' ;
CPU_MHZ                   (idx, 1)        = 33581576.0 ;
START_DATE                (idx, [1: 24])  = 'Mon Feb 15 12:38:52 2021' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Tue Feb 16 00:11:03 2021' ;

% Run parameters:

POP                       (idx, 1)        = 1000000 ;
CYCLES                    (idx, 1)        = 2000 ;
SKIP                      (idx, 1)        = 100 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 1613389132675 ;
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

MPI_TASKS                 (idx, 1)        = 10 ;
OMP_THREADS               (idx, 1)        = 8 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 1 ;
OMP_HISTORY_PROFILE       (idx, [1:   8]) = [  1.00010E+00  1.00145E+00  1.00074E+00  9.97236E-01  1.00196E+00  1.00016E+00  1.00127E+00  9.97092E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;
OMP_SHARED_QUEUE_LIM      (idx, 1)        = 0 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 55])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.dec' ;
SFY_DATA_FILE_PATH        (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.nfy' ;
NFY_DATA_FILE_PATH        (idx, [1: 52])  = '/home/fridman/serpent/install/xsdata/sss_endfb71.nfy' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  5.00000E-02 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  9.00000E-01  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  3.68192E-01 2.0E-05  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  6.31808E-01 1.2E-05  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  4.50783E-01 8.2E-06  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  5.39340E-01 7.7E-06  0.00000E+00 0.0E+00 ];
AVG_TRACKING_LOOPS        (idx, [1:   8]) = [  5.87350E+00 1.7E-05  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  3.15662E+01 1.5E-05  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  3.15662E+01 1.5E-05  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  2.69613E+01 2.3E-05  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  5.20709E+01 1.8E-05  0.00000E+00 0.0E+00 ];
LOST_PARTICLES            (idx, 1)        = 0 ;

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 2000 ;
SIMULATED_HISTORIES       (idx, 1)        = 200001916 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  1.00001E+05 0.00004 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  1.00001E+05 0.00004 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  2.13227E+03 ;
RUNNING_TIME              (idx, 1)        =  6.92184E+02 ;
INIT_TIME                 (idx, [1:  2])  = [  3.43433E-01  3.43433E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  1.10667E-02  1.10667E-02 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  6.91829E+02  6.91829E+02  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  2.41393E+02  2.41386E+02 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  4.50773E+02  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 3.08050 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  3.99830E+00 0.00122 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  6.34446E-01 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 385645.68 ;
ALLOC_MEMSIZE             (idx, 1)        = 2834.30;
MEMSIZE                   (idx, 1)        = 2710.76;
XS_MEMSIZE                (idx, 1)        = 1492.65;
MAT_MEMSIZE               (idx, 1)        = 305.87;
RES_MEMSIZE               (idx, 1)        = 243.97;
IFC_MEMSIZE               (idx, 1)        = 0.00;
MISC_MEMSIZE              (idx, 1)        = 668.27;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 123.54;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 181 ;
UNION_CELLS               (idx, 1)        = 0 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 416982 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  1.00000E+37 ;
URES_EMAX                 (idx, 1)        = -1.00000E+37 ;
URES_AVAIL                (idx, 1)        = 35 ;
URES_USED                 (idx, 1)        = 0 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 65 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 65 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 1814 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Neutron physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 0 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.20282E+10 2.5E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  4.66778E-01 5.6E-05 ];
U235_FISS                 (idx, [1:   4]) = [  1.33223E+15 2.8E-05  9.39865E-01 8.4E-06 ];
U238_FISS                 (idx, [1:   4]) = [  8.52404E+13 0.00014  6.01350E-02 0.00013 ];
U235_CAPT                 (idx, [1:   4]) = [  3.07880E+14 7.1E-05  1.72017E-01 6.6E-05 ];
U238_CAPT                 (idx, [1:   4]) = [  7.65618E+14 5.2E-05  4.27760E-01 3.5E-05 ];

% Neutron balance (particles/weight):

BALA_SRC_NEUTRON_SRC     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_FISS    (idx, [1:  2])  = [ 2000025557 2.00000E+09 ];
BALA_SRC_NEUTRON_NXN     (idx, [1:  2])  = [ 0 2.79743E+06 ];
BALA_SRC_NEUTRON_VR      (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_SRC_NEUTRON_TOT     (idx, [1:  2])  = [ 2000025557 2.00280E+09 ];

BALA_LOSS_NEUTRON_CAPT    (idx, [1:  2])  = [ 1116086153 1.11766E+09 ];
BALA_LOSS_NEUTRON_FISS    (idx, [1:  2])  = [ 883939404 8.85142E+08 ];
BALA_LOSS_NEUTRON_LEAK    (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_CUT     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_ERR     (idx, [1:  2])  = [ 0 0.00000E+00 ];
BALA_LOSS_NEUTRON_TOT     (idx, [1:  2])  = [ 2000025557 2.00280E+09 ];

BALA_NEUTRON_DIFF         (idx, [1:  2])  = [ 0 7.39098E-06 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  4.60000E+04 0.0E+00 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  3.48723E+15 5.6E-07 ];
TOT_FISSRATE              (idx, [1:   2]) = [  1.41751E+15 6.2E-08 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  1.78982E+15 2.5E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  3.20732E+15 1.4E-05 ];
TOT_SRCRATE               (idx, [1:   2]) = [  3.20282E+15 2.5E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  1.52419E+17 2.6E-05 ];
TOT_PHOTON_PRODRATE       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  3.20732E+15 1.4E-05 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  1.01234E+17 2.3E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Six-factor formula:

SIX_FF_ETA                (idx, [1:   2]) = [  1.65376E+00 2.2E-05 ];
SIX_FF_F                  (idx, [1:   2]) = [  8.11873E-01 1.4E-05 ];
SIX_FF_P                  (idx, [1:   2]) = [  6.14496E-01 1.8E-05 ];
SIX_FF_EPSILON            (idx, [1:   2]) = [  1.31966E+00 1.9E-05 ];
SIX_FF_LF                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_LT                 (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
SIX_FF_KINF               (idx, [1:   2]) = [  1.08878E+00 2.5E-05 ];
SIX_FF_KEFF               (idx, [1:   2]) = [  1.08878E+00 2.5E-05 ];

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46011E+00 6.1E-07 ];
FISSE                     (idx, [1:   2]) = [  2.02545E+02 6.2E-08 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.08877E+00 2.6E-05  1.08128E-02 2.5E-05  7.49811E-05 0.00040 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.08881E+00 2.4E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.08880E+00 1.4E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% ALF (Average lethargy of neutrons causing fission):
% Based on E0 = 2.000000E+01 MeV

ANA_ALF                   (idx, [1:   2]) = [  1.71522E+01 9.6E-06 ];
IMP_ALF                   (idx, [1:   2]) = [  1.71522E+01 4.5E-06 ];

% EALF (Energy corresponding to average lethargy of neutrons causing fission):

ANA_EALF                  (idx, [1:   2]) = [  7.11283E-07 0.00017 ];
IMP_EALF                  (idx, [1:   2]) = [  7.11111E-07 7.7E-05 ];

% AFGE (Average energy of neutrons causing fission):

ANA_AFGE                  (idx, [1:   2]) = [  2.08989E-01 0.00014 ];
IMP_AFGE                  (idx, [1:   2]) = [  2.08971E-01 5.7E-05 ];

% Forward-weighted delayed neutron parameters:

PRECURSOR_GROUPS          (idx, 1)        = 6 ;
FWD_ANA_BETA_ZERO         (idx, [1:  14]) = [  6.54202E-03 0.00027  2.08845E-04 0.00149  1.11713E-03 0.00065  1.08873E-03 0.00065  2.52902E-03 0.00043  1.12866E-03 0.00064  4.69646E-04 0.00099 ];
FWD_ANA_LAMBDA            (idx, [1:  14]) = [  5.00805E-01 0.00038  1.33549E-02 8.2E-06  3.26029E-02 8.3E-06  1.21075E-01 4.4E-06  3.05841E-01 1.0E-05  8.61666E-01 1.7E-05  2.89435E+00 2.8E-05 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  14]) = [  6.95012E-03 0.00039  2.22157E-04 0.00221  1.18475E-03 0.00097  1.15687E-03 0.00098  2.68603E-03 0.00063  1.20044E-03 0.00095  4.99870E-04 0.00149 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  14]) = [  5.01347E-01 0.00058  1.33549E-02 1.2E-05  3.26021E-02 1.2E-05  1.21077E-01 6.6E-06  3.05858E-01 1.6E-05  8.61725E-01 2.6E-05  2.89458E+00 4.1E-05 ];

% Adjoint weighted time constants using Nauchi's method:

IFP_CHAIN_LENGTH          (idx, 1)        = 15 ;
ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  1.87236E-05 5.7E-05  1.87130E-05 5.7E-05  2.02473E-05 0.00056 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  2.03854E-05 5.0E-05  2.03739E-05 5.1E-05  2.20444E-05 0.00056 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  14]) = [  6.88688E-03 0.00041  2.19947E-04 0.00230  1.17530E-03 0.00099  1.14498E-03 0.00101  2.66087E-03 0.00066  1.19034E-03 0.00098  4.95446E-04 0.00153 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  14]) = [  5.01464E-01 0.00059  1.33550E-02 1.3E-05  3.26019E-02 1.3E-05  1.21076E-01 6.9E-06  3.05852E-01 1.6E-05  8.61733E-01 2.7E-05  2.89457E+00 4.3E-05 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  1.90459E-05 0.00013  1.90352E-05 0.00013  2.05790E-05 0.00142 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  2.07363E-05 0.00013  2.07247E-05 0.00013  2.24053E-05 0.00142 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  14]) = [  6.89471E-03 0.00128  2.20441E-04 0.00723  1.17517E-03 0.00312  1.13924E-03 0.00314  2.67363E-03 0.00207  1.19115E-03 0.00308  4.95085E-04 0.00478 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  14]) = [  5.01307E-01 0.00184  1.33545E-02 3.5E-05  3.26020E-02 4.0E-05  1.21075E-01 2.2E-05  3.05856E-01 5.0E-05  8.61819E-01 8.5E-05  2.89455E+00 0.00013 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  14]) = [  6.89164E-03 0.00124  2.20203E-04 0.00704  1.17516E-03 0.00303  1.13958E-03 0.00306  2.67040E-03 0.00202  1.19074E-03 0.00299  4.95556E-04 0.00466 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  14]) = [  5.01563E-01 0.00180  1.33544E-02 3.5E-05  3.26023E-02 3.9E-05  1.21075E-01 2.1E-05  3.05849E-01 4.9E-05  8.61824E-01 8.3E-05  2.89457E+00 0.00013 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -3.62336E+02 0.00128 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  1.89151E-05 3.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  2.05939E-05 2.6E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  6.90554E-03 0.00025 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -3.65091E+02 0.00025 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  3.45257E-07 3.0E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  3.03705E-06 2.7E-05  3.03749E-06 2.7E-05  2.97834E-06 0.00031 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  2.29331E-05 3.0E-05  2.29325E-05 3.1E-05  2.30153E-05 0.00034 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  6.15294E-01 1.8E-05  6.14761E-01 1.8E-05  6.97254E-01 0.00043 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.04895E+01 0.00062 ];
ANA_MEAN_NCOL             (idx, [1:   4]) = [  3.15662E+01 1.5E-05  3.21798E+01 1.9E-05 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  3])  = 'RR4' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  0.00000E+00  5.00000E-09  1.00000E-08  1.50000E-08  2.00000E-08  2.50000E-08  3.00000E-08  3.50000E-08  4.20000E-08  5.00000E-08  5.80000E-08  6.70000E-08  8.00000E-08  1.00000E-07  1.40000E-07  1.80000E-07  2.20000E-07  2.50000E-07  2.80000E-07  3.00000E-07  3.20000E-07  3.50000E-07  4.00000E-07  5.00000E-07  6.25000E-07  7.80000E-07  8.50000E-07  9.10000E-07  9.50000E-07  9.72000E-07  9.96000E-07  1.02000E-06  1.04500E-06  1.07100E-06  1.09700E-06  1.12300E-06  1.15000E-06  1.30000E-06  1.50000E-06  1.85500E-06  2.10000E-06  2.60000E-06  3.30000E-06  4.00000E-06  9.87700E-06  1.59680E-05  2.77000E-05  4.80520E-05  7.55014E-05  1.48728E-04  3.67262E-04  9.06898E-04  1.42510E-03  2.23945E-03  3.51910E-03  5.53000E-03  9.11800E-03  1.50300E-02  2.47800E-02  4.08500E-02  6.74300E-02  1.11000E-01  1.83000E-01  3.02500E-01  5.00000E-01  8.21000E-01  1.35300E+00  2.23100E+00  3.67900E+00  6.06550E+00  1.00000E+37 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Micro-group spectrum:

INF_MICRO_FLX             (idx, [1: 140]) = [  3.15080E+06 0.00033  1.30347E+07 0.00038  3.34997E+07 0.00020  5.56784E+07 0.00015  8.90314E+07 0.00016  1.35532E+08 0.00012  1.14800E+08 0.00024  9.57461E+07 0.00017  8.67225E+07 0.00021  6.09315E+07 0.00014  5.23777E+07 0.00026  3.97027E+07 0.00020  4.59069E+07 0.00019  3.67098E+07 0.00014  2.49282E+07 0.00018  3.01644E+07 0.00014  2.90775E+07 0.00019  3.63173E+07 0.00020  3.06264E+07 0.00020  5.61263E+07 0.00020  5.02184E+07 0.00016  4.04745E+07 0.00016  2.56357E+07 8.7E-05  2.98127E+07 0.00015  2.80790E+07 0.00014  2.28708E+07 0.00023  3.78362E+07 0.00024  7.20950E+06 0.00027  8.53529E+06 0.00034  7.25867E+06 0.00035  4.03602E+06 0.00026  6.61582E+06 0.00034  4.24298E+06 0.00032  3.48525E+06 0.00035  6.58129E+05 0.00058  6.43640E+05 0.00067  6.54555E+05 0.00068  6.65130E+05 0.00036  6.50697E+05 0.00055  6.34359E+05 0.00030  6.45895E+05 0.00057  6.01962E+05 0.00038  1.11847E+06 0.00042  1.74340E+06 0.00041  2.14359E+06 0.00040  5.25674E+06 0.00041  4.91660E+06 0.00031  4.57561E+06 0.00029  2.59345E+06 0.00055  1.68690E+06 0.00042  1.19275E+06 0.00038  1.26088E+06 0.00052  2.03662E+06 0.00051  2.25162E+06 0.00031  3.41859E+06 0.00024  3.96149E+06 0.00030  4.44141E+06 0.00026  2.29214E+06 0.00052  1.44306E+06 0.00051  9.46036E+05 0.00049  7.86746E+05 0.00053  7.18176E+05 0.00057  5.60259E+05 0.00077  3.52467E+05 0.00098  3.07103E+05 0.00066  2.55688E+05 0.00039  2.01116E+05 0.00075  1.43348E+05 0.00105  8.34628E+04 0.00100  2.50699E+04 0.00195 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Flux spectra in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.18078E+16 0.00011  6.47779E+14 0.00020 ];
INF_FISS_FLX              (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  5.57067E-01 2.0E-05  1.01333E+00 8.5E-06 ];
INF_CAPT                  (idx, [1:   4]) = [  3.71468E-03 9.0E-05  1.00473E-01 6.2E-05 ];
INF_ABS                   (idx, [1:   4]) = [  3.71468E-03 9.0E-05  1.00473E-01 6.2E-05 ];
INF_FISS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NSF                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_NUBAR                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_INVV                  (idx, [1:   4]) = [  5.09345E-08 0.00012  1.79142E-06 6.2E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  5.53352E-01 2.0E-05  9.12863E-01 1.6E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  4.34469E-02 7.8E-05  3.54664E-02 0.00107 ];
INF_SCATT2                (idx, [1:   4]) = [  2.20819E-02 0.00016  7.58351E-03 0.00293 ];
INF_SCATT3                (idx, [1:   4]) = [  4.36810E-03 0.00074  2.34116E-03 0.00667 ];
INF_SCATT4                (idx, [1:   4]) = [  1.40661E-03 0.00209 -7.48555E-05 0.18766 ];
INF_SCATT5                (idx, [1:   4]) = [  3.86591E-04 0.00387  2.55565E-04 0.05869 ];
INF_SCATT6                (idx, [1:   4]) = [  5.27893E-04 0.00489 -6.77102E-04 0.03175 ];
INF_SCATT7                (idx, [1:   4]) = [  5.98435E-05 0.01710 -1.45061E-04 0.10604 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  5.53353E-01 2.0E-05  9.12863E-01 1.6E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  4.34469E-02 7.8E-05  3.54664E-02 0.00107 ];
INF_SCATTP2               (idx, [1:   4]) = [  2.20819E-02 0.00016  7.58351E-03 0.00293 ];
INF_SCATTP3               (idx, [1:   4]) = [  4.36810E-03 0.00074  2.34116E-03 0.00667 ];
INF_SCATTP4               (idx, [1:   4]) = [  1.40661E-03 0.00209 -7.48555E-05 0.18766 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.86591E-04 0.00387  2.55565E-04 0.05869 ];
INF_SCATTP6               (idx, [1:   4]) = [  5.27891E-04 0.00489 -6.77102E-04 0.03175 ];
INF_SCATTP7               (idx, [1:   4]) = [  5.98407E-05 0.01710 -1.45061E-04 0.10604 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  3.38001E-01 2.3E-05  9.72977E-01 4.3E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  9.86190E-01 2.3E-05  3.42591E-01 4.3E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  3.71384E-03 8.9E-05  1.00473E-01 6.2E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  5.34176E-03 0.00011  1.08529E-01 0.00015 ];

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

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHIP                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  5.51725E-01 2.0E-05  1.62685E-03 0.00021  8.06008E-03 0.00068  9.04802E-01 2.0E-05 ];
INF_S1                    (idx, [1:   8]) = [  4.33496E-02 7.8E-05  9.72163E-05 0.00144 -6.09919E-04 0.00412  3.60763E-02 0.00106 ];
INF_S2                    (idx, [1:   8]) = [  2.22083E-02 0.00016 -1.26323E-04 0.00087 -2.46732E-04 0.00571  7.83024E-03 0.00289 ];
INF_S3                    (idx, [1:   8]) = [  4.47803E-03 0.00072 -1.09934E-04 0.00126 -9.33407E-05 0.02167  2.43450E-03 0.00641 ];
INF_S4                    (idx, [1:   8]) = [  1.42832E-03 0.00209 -2.17104E-05 0.00369 -5.63799E-05 0.02456 -1.84755E-05 0.78324 ];
INF_S5                    (idx, [1:   8]) = [  3.76508E-04 0.00401  1.00822E-05 0.01205 -4.49840E-05 0.02841  3.00549E-04 0.04747 ];
INF_S6                    (idx, [1:   8]) = [  5.34527E-04 0.00486 -6.63396E-06 0.00732 -3.59128E-05 0.03068 -6.41189E-04 0.03300 ];
INF_S7                    (idx, [1:   8]) = [  7.08018E-05 0.01402 -1.09583E-05 0.00635 -2.67515E-05 0.01821 -1.18310E-04 0.13273 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  5.51726E-01 2.0E-05  1.62685E-03 0.00021  8.06008E-03 0.00068  9.04802E-01 2.0E-05 ];
INF_SP1                   (idx, [1:   8]) = [  4.33496E-02 7.8E-05  9.72163E-05 0.00144 -6.09919E-04 0.00412  3.60763E-02 0.00106 ];
INF_SP2                   (idx, [1:   8]) = [  2.22083E-02 0.00016 -1.26323E-04 0.00087 -2.46732E-04 0.00571  7.83024E-03 0.00289 ];
INF_SP3                   (idx, [1:   8]) = [  4.47803E-03 0.00072 -1.09934E-04 0.00126 -9.33407E-05 0.02167  2.43450E-03 0.00641 ];
INF_SP4                   (idx, [1:   8]) = [  1.42832E-03 0.00209 -2.17104E-05 0.00369 -5.63799E-05 0.02456 -1.84755E-05 0.78324 ];
INF_SP5                   (idx, [1:   8]) = [  3.76509E-04 0.00401  1.00822E-05 0.01205 -4.49840E-05 0.02841  3.00549E-04 0.04747 ];
INF_SP6                   (idx, [1:   8]) = [  5.34525E-04 0.00486 -6.63396E-06 0.00732 -3.59128E-05 0.03068 -6.41189E-04 0.03300 ];
INF_SP7                   (idx, [1:   8]) = [  7.07990E-05 0.01402 -1.09583E-05 0.00635 -2.67515E-05 0.01821 -1.18310E-04 0.13273 ];

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

CMM_TRANSPXS              (idx, [1:   4]) = [  4.13478E-02 8.8E-05  2.78164E-02 0.00028 ];
CMM_TRANSPXS_X            (idx, [1:   4]) = [  4.15139E-02 0.00012  2.79565E-02 0.00034 ];
CMM_TRANSPXS_Y            (idx, [1:   4]) = [  4.15161E-02 7.5E-05  2.79528E-02 0.00029 ];
CMM_TRANSPXS_Z            (idx, [1:   4]) = [  4.10174E-02 0.00010  2.75441E-02 0.00032 ];
CMM_DIFFCOEF              (idx, [1:   4]) = [  8.06170E+00 8.8E-05  1.19833E+01 0.00028 ];
CMM_DIFFCOEF_X            (idx, [1:   4]) = [  8.02944E+00 0.00012  1.19233E+01 0.00033 ];
CMM_DIFFCOEF_Y            (idx, [1:   4]) = [  8.02902E+00 7.5E-05  1.19249E+01 0.00029 ];
CMM_DIFFCOEF_Z            (idx, [1:   4]) = [  8.12664E+00 0.00010  1.21018E+01 0.00032 ];
TRC_TRANSPXS              (idx, [1:   4]) = [  3.38001E-01 2.3E-05  9.72977E-01 4.3E-05 ];
TRC_DIFFCOEF              (idx, [1:   4]) = [  9.86190E-01 2.3E-05  3.42591E-01 4.3E-05 ];

% Delayed neutron parameters (Meulekamp method):

BETA_EFF                  (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
LAMBDA                    (idx, [1:  14]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Assembly discontinuity factors (order: W-S-E-N / NW-NE-SE-SW):

DF_SURFACE                (idx, [1:  6])  = 'adf_r1' ;
DF_SYM                    (idx, 1)        = 0 ;
DF_N_SURF                 (idx, 1)        = 4 ;
DF_N_CORN                 (idx, 1)        = 4 ;
DF_VOLUME                 (idx, 1)        =  4.62405E+02 ;
DF_SURF_AREA              (idx, [1:  4])  = [ 2.15036E+01  2.15036E+01  2.15036E+01  2.15036E+01 ];
DF_MID_AREA               (idx, [1:  4])  = [ 2.15036E+00  2.15036E+00  2.15036E+00  2.15036E+00 ];
DF_CORN_AREA              (idx, [1:  4])  = [ 2.15036E+00  2.15036E+00  2.15036E+00  2.15036E+00 ];
DF_SURF_IN_CURR           (idx, [1:  16]) = [  3.61279E+14 0.00026  3.86251E+13 0.00023  3.61325E+14 8.1E-05  3.86319E+13 0.00023  2.24716E+14 0.00026  5.12726E+12 0.00095  2.24708E+14 0.00025  5.12762E+12 0.00070 ];
DF_SURF_OUT_CURR          (idx, [1:  16]) = [  3.05661E+14 0.00022  2.12168E+13 0.00031  3.05690E+14 8.0E-05  2.12155E+13 0.00013  2.24716E+14 0.00026  5.12726E+12 0.00095  2.24708E+14 0.00025  5.12762E+12 0.00070 ];
DF_SURF_NET_CURR          (idx, [1:  16]) = [  5.56182E+13 0.00057  1.74083E+13 0.00035  5.56348E+13 0.00037  1.74165E+13 0.00048  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_MID_IN_CURR            (idx, [1:  16]) = [  3.51655E+13 0.00028  3.74357E+12 0.00089  3.51905E+13 0.00026  3.74323E+12 0.00072  2.14434E+13 0.00039  3.30182E+11 0.00323  2.14368E+13 0.00040  3.27630E+11 0.00254 ];
DF_MID_OUT_CURR           (idx, [1:  16]) = [  2.96540E+13 0.00021  1.96316E+12 0.00113  2.96587E+13 0.00027  1.96545E+12 0.00098  2.14434E+13 0.00039  3.30182E+11 0.00323  2.14368E+13 0.00040  3.27630E+11 0.00254 ];
DF_MID_NET_CURR           (idx, [1:  16]) = [  5.51146E+12 0.00141  1.78042E+12 0.00128  5.53176E+12 0.00176  1.77778E+12 0.00123  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_CORN_IN_CURR           (idx, [1:  16]) = [  3.18748E+13 0.00047  2.72249E+12 0.00092  1.93717E+13 0.00063  3.00065E+11 0.00468  3.18566E+13 0.00043  2.72538E+12 0.00102  4.09909E+13 0.00023  5.36898E+12 0.00042 ];
DF_CORN_OUT_CURR          (idx, [1:  16]) = [  2.88304E+13 0.00040  1.90428E+12 0.00122  1.93717E+13 0.00063  3.00065E+11 0.00468  2.88135E+13 0.00049  1.90246E+12 0.00076  3.67136E+13 0.00026  3.64238E+12 0.00047 ];
DF_CORN_NET_CURR          (idx, [1:  16]) = [  3.04437E+12 0.00150  8.18211E+11 0.00178  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  3.04308E+12 0.00140  8.22916E+11 0.00192  4.27723E+12 0.00179  1.72660E+12 0.00134 ];
DF_HET_VOL_FLUX           (idx, [1:   4]) = [  4.71619E+13 0.00011  1.40100E+12 0.00023 ];
DF_HET_SURF_FLUX          (idx, [1:  16]) = [  6.21087E+13 0.00025  5.63870E+12 0.00031  6.21152E+13 9.7E-05  5.63848E+12 0.00021  4.17223E+13 0.00031  9.61298E+11 0.00129  4.17263E+13 0.00029  9.61306E+11 0.00096 ];
DF_HET_CORN_FLUX          (idx, [1:  16]) = [  5.63984E+13 0.00045  4.36490E+12 0.00082  3.59194E+13 0.00074  5.59703E+11 0.00559  5.63946E+13 0.00054  4.36964E+12 0.00113  7.20667E+13 0.00026  8.53611E+12 0.00063 ];
DF_HOM_VOL_FLUX           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_HOM_SURF_FLUX          (idx, [1:  16]) = [  6.37331E+13 0.00022  5.43962E+12 0.00028  6.37381E+13 5.4E-05  5.44148E+12 0.00038  3.97180E+13 7.3E-05  9.47004E+11 0.00023  3.97158E+13 0.00019  9.46809E+11 0.00018 ];
DF_HOM_CORN_FLUX          (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SURF_DF                (idx, [1:  16]) = [  9.74513E-01 0.00013  1.03660E+00 0.00032  9.74539E-01 0.00010  1.03620E+00 0.00028  1.05046E+00 0.00033  1.01510E+00 0.00138  1.05062E+00 0.00019  1.01531E+00 0.00082 ];
DF_CORN_DF                (idx, [1:  16]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SGN_SURF_IN_CURR       (idx, [1:  16]) = [ -1.88181E+13 0.00158 -3.08214E+12 0.00299 -1.87967E+13 0.00135 -3.07848E+12 0.00232 -2.43869E+13 0.00152 -2.05900E+12 0.00295 -2.43819E+13 0.00118 -2.05752E+12 0.00213 ];
DF_SGN_SURF_OUT_CURR      (idx, [1:  16]) = [ -2.16135E+13 0.00123 -2.47870E+12 0.00254 -2.16221E+13 0.00142 -2.49025E+12 0.00289 -2.43869E+13 0.00152 -2.05900E+12 0.00295 -2.43819E+13 0.00118 -2.05752E+12 0.00213 ];
DF_SGN_SURF_NET_CURR      (idx, [1:  16]) = [  2.79541E+12 0.00538 -6.03445E+11 0.01019  2.82540E+12 0.00801 -5.88222E+11 0.00876  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DF_SGN_HET_SURF_FLUX      (idx, [1:  16]) = [ -3.72941E+12 0.00132 -5.28525E+11 0.00355 -3.73492E+12 0.00222 -5.29143E+11 0.00246 -4.56566E+12 0.00201 -3.91153E+11 0.00328 -4.56888E+12 0.00149 -3.90563E+11 0.00247 ];
DF_SGN_HOM_SURF_FLUX      (idx, [1:  16]) = [ -5.73398E+12 0.00036 -4.27285E+11 0.00038 -5.73224E+12 0.00055 -4.27099E+11 0.00029 -5.73398E+12 0.00036 -4.27285E+11 0.00038 -5.73224E+12 0.00055 -4.27099E+11 0.00029 ];
DF_SGN_SURF_DF            (idx, [1:  16]) = [  6.50406E-01 0.00139  1.23694E+00 0.00362  6.51563E-01 0.00207  1.23892E+00 0.00243  7.96246E-01 0.00198  9.15433E-01 0.00307  7.97049E-01 0.00133  9.14458E-01 0.00255 ];

