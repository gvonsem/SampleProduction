#!/bin/zsh

EVENTSJOB=100
NJOBS=100
TEMPLATE=crabConfig_MCgeneration.py
DATE=`date +'%F'`

for CONFIG in `ls configs/*.py`; do
  #echo $CONFIG
  CONFIG=`print $CONFIG(:t:r)`
  CONFIG2="${CONFIG%_1_cfg}"
  #echo $CONFIG
  DATASET=${CONFIG2}_GEN-SIM
  CONFIGNAME=crabConfig_${DATASET}.py
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
