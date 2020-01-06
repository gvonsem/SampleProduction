#!/bin/zsh

EVENTSJOB=100
NJOBS=100
TEMPLATE=crabConfig_MCgeneration.py
DATE=`date +'%F'`

CONFIGLIST=(configs/TTTo2L2Nu_CustomBdecays_TuneCP5_13TeV-powheg-pythia8_cfg.py)

#for CONFIG in `ls configs/*.py`; do
for CONFIG in ${CONFIGLIST}; do
  #echo $CONFIG
  CONFIG=`print $CONFIG(:t:r)`
  CONFIG2="${CONFIG%_1_cfg}"
  #echo $CONFIG
  DATASET=${CONFIG2}_GEN-SIM
  CONFIGNAME=crabConfig_${DATASET}.py
  #echo $CONFIGNAME
  cp $TEMPLATE $CONFIGNAME
  sed -i -e "s/CONFIG/$CONFIG/g" $CONFIGNAME
  sed -i -e "s/DATASET/$DATASET/g" $CONFIGNAME
  sed -i -e "s/DATE/$DATE/g" $CONFIGNAME
  sed -i -e "s/EVENTSJOB/$EVENTSJOB/g" $CONFIGNAME
  sed -i -e "s/NJOBS/$NJOBS/g" $CONFIGNAME
  # crab submit -c $CONFIGNAME --dryrun --skip-estimates
  # crab proceed
  crab submit -c $CONFIGNAME
  #break
done
