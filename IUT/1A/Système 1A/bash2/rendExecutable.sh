#!/bin/bash

if [ -f $1 ]
then
    if [ -x $1 ]
    then
        chmod u+x $1
    else
        echo $1" est déjà exécutable"
    fi
else
    echo $1" n'est pas un fichier"
fi
ls -l