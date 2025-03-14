#!/bin/bash

echo $1 $2
DISPLAY=:0 zenity --entry --title=$1 --text=$2

# DISPLAY=:0 xmassage $1