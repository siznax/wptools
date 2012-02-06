#!/bin/bash
# siznax 2012

dumpbase="http://dumps.wikimedia.org/enwiki"
dlbase="http://download.wikimedia.org"
rate_limit='640K'

if [ $# -lt 1 ]
then
    echo -n "Usage: "`basename $0`" date ext"
    echo " | tee "`basename $0 .sh`"-{date}-{ext}.log"
    exit 0
fi

date
start=`date +%s`
lstfile="enwiki-$1-$2.lst"
resource="${dumpbase}/${1}/"

wget --quiet --spider ${resource} > /dev/null
if [ $? != 0 ]; then echo $?; exit; fi

echo "${resource} 200 OK"

curl -s $resource\
 | grep -o 'href="[^\"]*"'\
 | grep $2\
 | cut -d \" -f 2\
 > $lstfile

while read line
do 
    target=${dlbase}${line}
    echo "curl -sOL --limit-rate ${rate_limit} ${target}"
    curl -sOL --limit-rate ${rate_limit} ${target}
done < $lstfile

finish=`date +%s`
echo $((finish-start)) seconds
