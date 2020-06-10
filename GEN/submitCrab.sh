#!/bin/zsh

EVENTSJOB=200
NJOBS=250
TEMPLATE=crabConfig_MCgeneration.py
DATE=`date +'%F'`

CONFIGLIST=(configs/sherpa_ttbar_jetsNLO_MASTER_cff_py_GEN.py configs/sherpa_ttbar_jetsNLO_EW_MASTER_cff_py_GEN.py)

#for CONFIG in `ls configs/*.py`; do
for CONFIG in ${CONFIGLIST}; do
  #echo $CONFIG
  CONFIG=`print $CONFIG(:t:r)`
  CONFIG2="${CONFIG%_1_cfg}"
  #echo $CONFIG
  DATASET=${CONFIG2}_GEN
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
###  crab submit -c $CONFIGNAME
  #break
done
