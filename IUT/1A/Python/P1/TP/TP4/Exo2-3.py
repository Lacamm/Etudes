def booleens(liste, nombre):
    """
    Cette fonction a pour objectif de renvoyer la liste des nombres premiers
    inférieurs à une valeur voulue
    Paramètres:
        para1: la taille de la liste à créée
    Résultat: une liste de booléenns
    """
    listeNP = []

    for n in range(len(liste)):
        if n == 0 or n == 1:
            liste[n] = False
        elif n%nombre == 0 and n != nombre:
            liste[n] = False
        else:
            liste[n] = True
                
    print(liste)    
    for i in range(len(liste)):
        if liste[i] == 	True:
            listeNP.append(i)

    return listeNP

taille = int(input("La taille de la liste de booléens: "))
nombre = int(input("Un mutiple: "))
liste =[]

for i in range(taille):
    liste.append(True)

print(booleens(liste,nombre))