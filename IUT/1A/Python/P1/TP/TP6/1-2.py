from random import randint

def strMois(listeMoisFR):
    mois = ""
    mois3 = ""
    listeM = []
    
    for n in range(len(listeMoisFR)):
        mois = listeMoisFR[n]
        mois3 = mois[:3]
        listeM.append(mois3)
    return " ".join(listeM)



listeMoisFR = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]

print(strMois(listeMoisFR))