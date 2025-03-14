#!/bin/bash

while true
do
    DISPLAY=:0 xrandr -o 1
    sleep 
    DISPLAY=:0 xrandr -o 2
    sleep 5
    DISPLAY=:0 xrandr -o 3
    sleep 5
    DISPLAY=:0 xrandr -o 0
    sleep 5
done