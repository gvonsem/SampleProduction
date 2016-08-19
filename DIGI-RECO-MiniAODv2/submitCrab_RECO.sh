#!/bin/zsh

NJOBS=1000
CRABTEMPLATE=crabConfig_MCgeneration_RECO80X_step2.py
DATE=`date +'%F'`

for DATASETIN in `cat datasets_DIGI.txt`; do
  echo "DATASETIN: $DATASETIN"
  #a=("${(@s/-/)DATASETIN}")
  a=("${(@s|/|)DATASETIN}")
  INSHORT=$a[2]-$a[3]
  INSHORT=$a[2]
  CRABCONFIG=crabConfig_${INSHORT}.py
  echo "CRABCONFIG $CRABCONFIG"
  DATASETOUT=${INSHORT}_RECO80X
  echo "DATASETOUT: $DATASETOUT"
  cp $CRABTEMPLATE $CRABCONFIG
  sed -i -e "s|DATASETIN|$DATASETIN|g" $CRABCONFIG
  sed -i -e "s|INSHORT|$INSHORT|g" $CRABCONFIG
  sed -i -e "s/DATASETOUT/$DATASETOUT/g" $CRABCONFIG
  sed -i -e "s/DATE/$DATE/g" $CRABCONFIG
  sed -i -e "s/NJOBS/$NJOBS/g" $CRABCONFIG
  crab submit -c $CRABCONFIG
done
