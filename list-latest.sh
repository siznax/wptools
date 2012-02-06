#!/bin/bash

# siznax 2012

if [ $# -lt 1 ]
then
    echo "Usage: "`basename $0`" wiki pattern"
    exit 0
fi

wiki=$1
pattern=$2
base=dumps.wikimedia.org
resource=http://${base}/${wiki}/latest

echo ${resource}

lynx -dump -nolist -width 1024 ${resource}\
 | tr -s " "\
 | grep "${pattern}"
