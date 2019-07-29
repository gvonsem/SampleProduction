# SampleProduction
Scripts for private MC production with crab3. Based on [repository](https://github.com/clelange/QStarProduction) of Clemens Lange.

## setup

Clone the repository into a new directory (more directories will show up in parallel):
```
mkdir signalProduction
cd signalProduction
git clone git@github.com:gvonsem/SampleProduction.git
```

Get a CMS software environment:
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
```

Note: the CMSSW releases below and corresponding architectures may be adapted according to the recommended [production releases for the campaign](https://cms-pdmv.cern.ch/mcm/campaigns?page=-1&shown=63). Or other changes can be made if differences in configuration with previous samples are to be minimized. 

## GEN-SIM step

This step needs a working CMS software environment (see above). Need to be in ```signalProduction``` directory. 


```
export SCRAM_ARCH=slc7_amd64_gcc630
cmsrel CMSSW_9_3_15_patch1
cd CMSSW_9_3_15_patch1/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
for i in `ls ../../SampleProduction/GEN-SIM`; do ln -s ../../SampleProduction/GEN-SIM/$i; done
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
export SCRAM_ARCH=slc7_amd64_gcc630
cmsrel CMSSW_9_4_0_patch1
cd CMSSW_9_4_0_patch1/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
for i in `ls ../../SampleProduction/DIGI-RECO-MiniAODv2`; do ln -s ../../SampleProduction/DIGI-RECO-MiniAODv2/$i; done
```

## DIGI step

Put your GEN-SIM dataset names into ```datasets_GENSIM.txt```, one per line.

Then you can submit:
```
./submitCrab_DIGI.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit_DIGI.sh
```

## RECO step

This step needs the same setup as the DIGI one, so you can just setup CMSSW and crab again, or reuse the same shell:

```
cd CMSSW_9_4_0_patch1/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
```

Put your DIGI dataset names into ```datasets_DIGI.txt```, one per line.

Then you can submit:
```
./submitCrab_RECO.sh
```

### job sitting

To check the status of your jobs and to resubmit the failed ones:
```
./resubmit_RECO.sh
```

## MiniAOD (v2) step

Start again in the ```signalProduction``` directory, probably best from a clean shell (set up CMS software environment again).


```
export SCRAM_ARCH=slc7_amd64_gcc630
cmsrel CMSSW_9_4_6_patch1
cd CMSSW_9_4_6_patch1/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
for i in `ls ../../SampleProduction/DIGI-RECO-MiniAODv2`; do ln -s ../../SampleProduction/DIGI-RECO-MiniAODv2/$i; done
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
