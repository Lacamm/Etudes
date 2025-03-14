#!/bin/bash

read fichier

if [ -f $fichier ] # si c'est un fichier
then
    if [ -x $fichier ] # si il est déjà exécutable
    then 
        echo le fichier est déjà exécutable
    else 
        chmod u+x $fichier
        echo le fichier est désormais exécutable
    fi
else
    echo "Ce n'est pas un fichier du répertoire courant"
fi