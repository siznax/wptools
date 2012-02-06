#!/bin/bash

# siznax 2012

if [ $# -lt 1 ]
then
    echo "Usage: image.sql.gz"
    exit 0
fi

if [ "${1:${#1}-7}" != '.sql.gz' ]
then
    echo "invalid input: $1"
    exit 1
fi

start=`date +%s`
base=`basename $1 .sql.gz`

date
echo $1

mimes=( gif jpg jpeg pdf png svg tiff )
for ext in "${mimes[@]}"
do
    out=${base}.${ext}.lst.gz
    zcat $1\
     | grep -oi "'[^\']*\.${ext}'"\
     | cut -d \' -f 2\
     | grep -v '^[[:digit:]14]'\
     | grep -v '[[:space:]]'\
     | uniq\
     | gzip\
     > ${out}
    echo ${out} `zcat ${out} | wc -l` lines
done

finish=`date +%s`
echo $((finish-start)) seconds
