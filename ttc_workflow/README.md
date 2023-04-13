# CERN_workflow

## TopJets2015 enviroment configuration

### installing
```bash
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_16
cd CMSSW_10_6_16/src
cmsenv
git cms-init

#EGM id
git cms-merge-topic jainshilpi:ULV1_backport10616_forUsers
git clone https://github.com/jainshilpi/EgammaPostRecoTools.git -b ULV0
mv EgammaPostRecoTools/python/EgammaPostRecoTools.py RecoEgamma/EgammaTools/python/.
git clone https://github.com/jainshilpi/EgammaAnalysis-ElectronTools.git -b UL2017SSV2 EgammaAnalysis/ElectronTools/data/
git cms-addpkg EgammaAnalysis/ElectronTools
scram b -j 8

#B-fragmentation analyzer
mkdir TopQuarkAnalysis
cd TopQuarkAnalysis
git clone -b 94x https://gitlab.cern.ch/psilva/BFragmentationAnalyzer.git
scram b -j 8
cd -

#This package
cd $CMSSW_BASE/src
git clone https://github.com/efeyazgan/TopLJets2015.git -b 106_protonreco
cd TopLJets2015

scram b -j 8
```         
 

## 