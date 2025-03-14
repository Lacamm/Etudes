from random import choice #Importer la fonction choice

l1=[1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,6,6] #Définir une liste avec le pourcentage de chance de tirer un nombre précis
l2=[] #Création d'une liste qui stockera les nombre choisit par Python

for r in range(100): #Création d'une boucle pour que l'on fera 100 fois
    A= choice(l1)    #Chopisir un nombre de l1 que l'on stockera dans A
    l2.append(A)     #Ajouter A à la liste l2

print(l2) #Afficher l2
