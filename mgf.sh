#!/usr/bin/env bash

# Merge conditional files into one file

# Option for Help
if [ x$1 = "x-h" ]; then
  echo "Usage: sh $0 [condition]"
  exit 0
fi

# Initialization
opf=`date +%Y%m%d%H%M%S`
opff="$opf.csv"
larg="$1*.csv"

# Put input file(s) content into ouput file circularly
> $opf
for ipf in $(ls $larg)
do
  echo $ipf >> $opf
  cat $ipf >> $opf
  echo "" >> $opf
  echo "" >> $opf
done

mv $opf $opff
echo "Generated: $opff "

