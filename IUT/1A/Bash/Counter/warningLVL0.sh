#!/bin/bash
echo "WARNING LAUNCH"
echo $1
ssh -o "StrictHostKeyChecking no" -X duval@$1 'export DISPLAY=:0.0 && zenity --error --text="Qu\`est ce que tu fais ? Déconnecte toi sinon RIP \!" --title="Attention !" --width=300'
