# QStarProduction
scripts for QStar to qV private MC production with crab3

## setup

Clone the repository into a new directory (more directories will show up in parallel):
```
mkdir signalProduction
cd signalProduction
git clone git@github.com:clelange/QStarProduction.git
```

### at PSI

Get a CMS software environment:
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
```


## GEN-SIM step

This step needs a working CMS software environment (see above). Need to be in ```signalProduction``` directory.

```
cmsrel CMSSW_7_1_24
cd CMSSW_7_1_24/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
for i in `ls ../../QStarProduction/GEN-SIM`; do ln -s ../../QStarProduction/GEN-SIM/$i; done
```

Then submit:
```
./submitCrab.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit.sh
```

## DIGI, RECO, and MiniAODv2 setup

All following steps need the same environment. Start again in the ```signalProduction``` directory, probably best from a clean shell (set up CMS software environment again).
```
cmsrel CMSSW_8_0_11
cd CMSSW_8_0_11/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
for i in `ls ../../QStarProduction/DIGI-RECO-MiniAODv2`; do ln -s ../../QStarProduction/DIGI-RECO-MiniAODv2/$i; done
```

## DIGI step

Put your GEN-SIM dataset names into ```datasets_GENSIM.txt```, one per line.

Then you can submit:
```
submitCrab_DIGI.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit_DIGI.sh
```

## RECO step

This step needs the same setup as the DIGI one, so you can just setup CMSSW and crab again, or reuse the same shell:

```
cd CMSSW_8_0_11/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

Put your DIGI dataset names into ```datasets_DIGI.txt```, one per line.

Then you can submit:
```
submitCrab_RECO.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit_RECO.sh
```

## MiniAOD (v2) step

Start again in the ```signalProduction``` directory, probably best from a clean shell (set up CMS software environment again).


```
cmsrel CMSSW_8_0_11
cd CMSSW_8_0_11/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
for i in `ls ../../QStarProduction/MiniAODv2`; do ln -s ../../QStarProduction/MiniAODv2/$i; done
```

Put your RECO dataset names into ```datasets_AODSIM.txt```, one per line.

Then you can submit:
```
submitCrab_MiniAODv2.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit.sh
```
