#!/bin/zsh

NJOBS=100
CRABTEMPLATE=crabConfig_MCgeneration_RECO94X_step2.py
DATE=`date +'%F'`

for DATASETIN in `cat datasets_DIGI.txt`; do

  ##skip lines in txt file that start with #
  if [[ $DATASETIN == "#"* ]] ; then
    continue
  fi
  
  echo "DATASETIN: $DATASETIN"
  #a=("${(@s/-/)DATASETIN}")
  a=("${(@s|/|)DATASETIN}")
#  INSHORT=$a[2]-$a[3]
#  INSHORT=$a[2]

  INSHORT=("${(@s|_DIGI|)a[3]}")
  INSHORT=("${(@s|gvonsem-|)INSHORT[1]}")
#  echo "INSHORT = "$INSHORT

  ##remove leading whitespaces
  INSHORT="${INSHORT##*( )}"
#  echo "INSHORT = "$INSHORT  

  CRABCONFIG=crabConfig_${INSHORT}_RECO_94X.py
  echo "CRABCONFIG $CRABCONFIG"
  DATASETOUT=${INSHORT}_RECO94X
  echo "DATASETOUT: $DATASETOUT"
  cp $CRABTEMPLATE $CRABCONFIG
  sed -i -e "s|DATASETIN|$DATASETIN|g" $CRABCONFIG
  sed -i -e "s|INSHORT|$INSHORT|g" $CRABCONFIG
  sed -i -e "s/DATASETOUT/$DATASETOUT/g" $CRABCONFIG
  sed -i -e "s/DATE/$DATE/g" $CRABCONFIG
  sed -i -e "s/NJOBS/$NJOBS/g" $CRABCONFIG
  crab submit -c $CRABCONFIG
done
