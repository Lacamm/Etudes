#!/bin/bash

while true
do
    echo $1
    DISPLAY=:0 chromium-browser &
done