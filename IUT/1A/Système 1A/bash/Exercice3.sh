#!/bin/bash
touch fic4
chmod 500 fic4
mkdir -p rep1
cd rep1
touch fic1
touch fic2
touch fic3
chmod 000 fic1
chmod 400 fic2
chmod 500 fic3
cd ..
mkdir -p rep2
cd rep2
touch fic1
touch fic2
touch fic3
chmod 000 fic1
chmod 400 fic2
chmod 500 fic3
cd ..
mkdir -p rep3
cd rep3
touch fic1
touch fic2
touch fic3
chmod 000 fic1
chmod 400 fic2
chmod 500 fic3
cd ..
mkdir -p rep4
cd rep4
touch fic1
touch fic2
touch fic3
chmod 000 fic1
chmod 400 fic2
chmod 500 fic3
cd ..
chmod 400 fic4
chmod 500 rep1
chmod 740 rep2
chmod 700 rep3
chmod 100 rep4