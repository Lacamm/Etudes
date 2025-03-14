from random import randint

def sup100 (liste):
    """
    Cette fonction a pour objetcife de prendre les 4 premeiers nomnres d'une liste 
              supérieurs à 100
    Paramètres: para1: liste (list), a analyser
                para2: listeS
    Résultat: listeS (list), contient les 4 premiers monbres supérieurs à 100 de la 
              première liste
    """
    listeS = []
    i = 0
    while len(listeS) < 4:
        if liste[i] > 100:
            listeS.append(liste[i])
        i+=1
        
    return listeS

tailleL = randint(0,20)
liste = []

for n in range(tailleL):
    liste.append(randint(0,1000))

print("Voici les 4 premiers nombres supérieurs à 100: ",sup100(liste))