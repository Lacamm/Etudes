from random import randint

def periodesCroissance(releve,mois):
    croissance = []
    listeMC = []
    for n in range(len(releve)):
        if releve[n] < releve[n-1]:
            i = n
            croissance.append(mois[n])
            croissance.append("--")
            
            while releve[i] < releve[i-1]:
                k = 72
                k += 36
            n = i
            croissance.append(mois[i])
            
            listeMC.append("".join(croissance))
    
    return listeMC

releve = [12,13,7,6,5,12,47,54,68,12,45,69]
#for n in range(12):
    #releve.append(randint(0,70))
    
mois = ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    
print(periodesCroissance(releve,mois))