#!/bin/bash

echo le nombre de fichier dans $2 se terminant par $1 est:
a=ls $2 |wc -l
echo $a