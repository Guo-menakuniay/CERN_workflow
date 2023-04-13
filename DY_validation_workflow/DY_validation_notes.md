# DY FxFx

* Work getting web: https://docs.google.com/document/d/1IYeXkOFKhg-wOJSsW8NBDiC4fF5ZvhzQOqutEbr-0tI/edit
* Before submit_cmsconnect_gridpack_generation.sh: voms-proxy-init -voms cms -valid 192:00 -> Password
* MG265 -> MG273: git checkout mg27x
* MG273 -> MG265: git checkout master
* Check the size of ".xz" file：du -h *.xz

## Test Running—Genvalidation

### 1.README
    preparing validation setup including gridpack generation using the example of MG5_aMC@NLO

### 2.Finished
#### create your working path
    mkdir -p SOMENAME
    cd SOMENAME
    git clone https://github.com/cms-sw/genproductions.git genproductions
#### make gridpacks e.g. at lxplus, more info can be found at https://twiki.cern.ch/twiki/bin/viewauth/CMS/QuickGuideMadGraph5aMCatNLO
    cd ${WORKDIR}/genproductions/bin/MadGraph5_aMCatNLO
    cp -rp ${WORKDIR}/genproductions/bin/GenValidation/updated_validation_cards .
    ./gridpack_generation.sh <PROCESS> <PROCESS's location>
    e.g: ./gridpack_generation.sh dyellell0j_mll10to50_5f_NLO_FXFX updated_validation_cards/dy_fxfx_lowmass/jet_binned/dy0jfxfx


## Produce DY FxFx gridpack [ssh wawang@login-el7.uscms.org]

### 1.Setup to run NanoGen with default weights
    cmsrel CMSSW_11_2_0_pre7
    cd CMSSW_11_2_0_pre7/src
    cmsenv
    git cms-init
    git config --global user.github WanyueWang
    git cms-merge-topic kdlong:NanoGen_dqm
    scram b -j 5
    
    cd CMSSW_11_2_0_pre7/src
    mkdir Configuration
    cd Configuration
    git clone git@github.com:kdlong/WMassNanoGen.git
    scram b

### 2.Setup to store all genWeights
    cmsrel CMSSW_10_6_18
    cd CMSSW_10_6_18/src
    cmsenv
    git cms-init
    git config --global user.github WanyueWang
    git cms-merge-topic kdlong:NanoGenWeights_CMSSW_10_6_18
    scram b -j 5
    
    cd CMSSW_10_6_18/src
    cd Configuration
    git clone git@github.com:kdlong/WMassNanoGen.git
    scram b

### 3.Make CMS Connect can identify cms.org.cern
    mkdir ~/.ciconnect
    echo "cms.org.cern" > ~/.ciconnect/defaultproject

### 4.Create your working path
    mkdir -p SOMENAME
    cd SOMENAME
    git clone https://github.com/cms-sw/genproductions.git genproductions

### 5.make gridpacks e.g. at lxplus, more info can be found at https://twiki.cern.ch/twiki/bin/viewauth/CMS/QuickGuideMadGraph5aMCatNLO
    cd ${WORKDIR}/genproductions/bin/DY_mll10to50_FXFX/MadGraph5_aMCatNLO/
    cp -rp ${WORKDIR}/genproductions/bin/GenValidation/updated_validation_cards .
    cd ${WORKDIR}/updated_validation_cards/dy_fxfx_lowmass/jet_binned
    sh create_cards.sh

### 6.Use submit_cmsconnect_gridpack_generation.sh
    cd ${WORKDIR}
    voms-proxy-init -voms cms -valid 192:00
    Password
    inc：nohup ./submit_cmsconnect_gridpack_generation.sh dyellell012j_mll10to50_5f_NLO_FXFX updated_validation_cards/dy_fxfx_lowmass/inc 4 "30 Gb" >& dyellell012j_mll10to50_5f_NLO_FXFX.log &
    jet-binned：nohup ./submit_cmsconnect_gridpack_generation.sh dyellell0j_mll10to50_5f_NLO_FXFX updated_validation_cards/dy_fxfx_lowmass/jet_binned/dy0jfxfx 2 "10 Gb" >& dyellell0j_mll10to50_5f_NLO_FXFX.log &
    nohup ./submit_condor_gridpack_generation.sh dyellell0j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy0jmlm >& dyellell0j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_condor_gridpack_generation.sh dyellell1j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy1jmlm >& dyellell1j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_condor_gridpack_generation.sh dyellell2j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy2jmlm >& dyellell2j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_cmsconnect_gridpack_generation.sh dyellell0j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy0jmlm >& dyellell0j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_cmsconnect_gridpack_generation.sh dyellell1j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy1jmlm >& dyellell1j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_cmsconnect_gridpack_generation.sh dyellell2j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy2jmlm >& dyellell2j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_cmsconnect_gridpack_generation.sh dyellell3j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy3jmlm >& dyellell3j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_cmsconnect_gridpack_generation.sh dyellell4j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/jet_binned/dy4jmlm >& dyellell4j_mll10to50_5f_LO_MLM.log &
    nohup ./submit_cmsconnect_gridpack_generation.sh dyellell01234j_mll10to50_5f_LO_MLM updated_validation_cards/dy_mlm_lowmass/inc 4 "30 Gb" >& dyellell01234j_mll10to50_5f_LO_MLM.log &

## Produce events locally [ssh -Y wawang@lxplus.cern.ch]
    cmsrel CMSSW_10_6_22
    cd CMSSW_10_6_22/src
    cmsenv
    
    mkdir -p Configuration/NanoGEN
    cd Configuration/NanoGEN
    mkdir python
    mkdir configs
    (put the fragment files in directory 'python')
    scram b (currently under directory 'NanoGEN')

### Test the events that have been produced above
    cmsDriver.py Configuration/NanoGEN/python/DY0j_FxFx_MG265_cff.py --eventcontent NANOAODGEN --python_filename configs/DY0j_FxFx_MG265_cfg.py --mc --datatier NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN -n 30 --no_exec (only need to change the name of DY0j_FxFx_MG265_cff.py & DY0j_FxFx_MG265_cfg.py)
    cmsRun configs/DY0j_FxFx_MG265_cfg.py (for lxplus local run)
    
    cmsDriver.py Configuration/NanoGEN/python/DY01234j_MLM_MG330_cff.py --eventcontent NANOAODGEN --python_filename configs/DY01234j_MLM_MG330_cfg.py --mc --datatier NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN -n 30 --no_exec (only need to change the name of DY0j_FxFx_MG265_cff.py & DY0j_FxFx_MG265_cfg.py)

### Submit works
    (make the cff.py files in directory 'python')
    (WORKPATH：/afs/cern.ch/user/w/wawang/CMSSW_10_6_22/src/Configuration/NanoGEN)
    cmsDriver.py Configuration/NanoGEN/python/DY0j_FxFx_MG265_cff.py --eventcontent NANOAODGEN --python_filename configs/DY0j_FxFx_MG265_cfg.py --mc --datatier NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN -n 30 --no_exec
    (Produce cfg.py files in "crab" dictionary)
    cmsenv
    voms-proxy-init -voms cms -valid 192:00
    crab submit -c crab/DY2j_FxFx_MG265_cfg.py #Submit works
    crab status -d DY_validation_MG265/crab_DY2j_MG265 #Check how the submission process proceeds

## Calculate cross sections
    (Put nanoXS.sh file into each process's log dictionary under the dictionary of /eos/user/w/wawang/)
    sh nanoXS.sh
    (Write down all the output informations)

## histo & plot under /afs/cern.ch/user/w/wawang
    cd CMSSW_8_1_0/src
    cmsenv

### histo
    (Put histo.py&histo.sh files into each process's dictionary)
    sh histo.sh -q <LOCAL/SUBMIT>
    
    (Under the Output dictionary)
    hadd FinalRootFILENAME.root *.root #Merge all root files into one file
    (Merge all processes as each process only has one root file)

### plot
    (Put plot.py&plot.sh files into plot dictionaries)
    vi plot.sh
    
    #array length is 2 for two version comparison
    xs=(19417.83 19419.01)
    histo_name=("histo_0j_265.root" "histo_0j_273.root")
    inDIR="./"
    names=("MG265" "MG273")
    
    #array length is larger than 2 for inclusive vs stitched, e.g.:
    xs=(20047.18 19417.26 441.78 259.77)
    histo_name=("histo_inc_265.root" "histo_0j_265.root" "histo_1j_265.root" "histo_2j_265.root")
    inDIR="./"
    names=("MGinc" "MG0j" "MG1j" "MG2j")
    
    sh plot.sh -m <TWOVERSION/INCVSSTIT>

## The pictures of comparison processes are finally created !!!
## The last step for your work is to make slides for presentation.

# Congratulation !!!

## submit condor gridpack [ From Xiao Jie ]
    https://github.com/freejiebao/genproductions/tree/mg33x/bin/GenValidation/nanogen_cms_connect/
