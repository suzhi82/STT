#!/usr/bin/env bash

# Delete all characters except numbers from csv file 

# Option for Help
if [ x$1 = "x-h" ] || [ $# -lt 1 ]; then
  echo "Usage: sh $0 CSVFILE"
  exit 0
fi

#suf=${1##*.}
opf=${1%.*}
opf=$opf".dgt.csv"

grep ',' $1 | grep -v [A-Za-z] > $opf

if [ $? -ne 0 ]; then
  rm $opf
else
  echo "$opf generated!"
fi

