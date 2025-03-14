#!/bin/bash

for n in $(seq -w $1 $2)
do
    echo info$1-$n: 
    ssh -oStrictHostKeyChecking=no info$1-$n who 2>/dev/null
done