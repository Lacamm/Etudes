from random import randint

def moisLePlusHumide(releve,mois):
    humide = 0
    for n in range(len(releve)):
        if humide < releve[n]:
            humide = releve[n]
            moisHumide = mois[n]

    return moisHumide

releve = []
for n in range(12):
    releve.append(randint(0,70))
    
mois = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    
print(moisLePlusHumide(releve,mois))