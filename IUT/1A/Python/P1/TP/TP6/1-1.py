from random import randint

def strMois(listeMoisFR,listeMoisEN):
    moisFR = ""
    moisEN = ""
    numMois = randint(0,11)
    moisFR = listeMoisFR[numMois]
    moisEN = listeMoisEN[numMois]
    return moisFR, moisEN



listeMoisFR = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]

listeMoisEN = ["January","Febuary","March","April","May","June","July","August","Septembre","Octobre","November","December"]

print(strMois(listeMoisFR,listeMoisEN))