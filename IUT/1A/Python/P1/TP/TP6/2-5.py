from random import randint

def moisLePlusSec(releve,mois):
    sec = 100
    for n in range(len(releve)):
        if sec > releve[n]:
            sec = releve[n]
            moisSec = mois[n]

    return moisSec

releve = []
for n in range(12):
    releve.append(randint(0,70))
    
mois = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    
print(moisLePlusSec(releve,mois))