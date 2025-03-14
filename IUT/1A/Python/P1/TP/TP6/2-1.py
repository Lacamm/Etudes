from random import randint

def releveDuMois(nomMois,releve,mois):
    faux =0
    for n in range(len(mois)):
        if nomMois != mois[n]:
            faux += 1
    if faux == 12:
        releve = None
    
    return releve

releve = randint(0, 50)
numMois = randint(0,11)

mois = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]

nomMois = mois[numMois]

print("relve= ",releveDuMois(nomMois,releve,mois))