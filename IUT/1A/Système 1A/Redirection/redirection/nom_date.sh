#!/bin/bash

read nom
touch monNom2.txt
rm monNom2.txt
echo "Je m appelle $nom il est $(date +%H:%M) heures.">> monNom2.txt
chmod 700 monNom2.txt
cat monNom2.txt