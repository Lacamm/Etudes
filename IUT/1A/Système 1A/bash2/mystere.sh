#!/bin/bash

if [ $# -eq 0 ]
then
    echo "Eh Eh"
else
    if [ $1 = 'banzai' ]
    then
        echo "Ah Ah $*"
    else
        echo 'Oh Oh $1'
    fi
fi