from random import choice #Importer la fonction

l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
    't','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]#Création d'une liste avec toutes les lettres en minuscules et les 10 chiffres
l2=[] #Création d'une liste qui servira à receuillir le code souhaité

for r in range(10): #Création d'une boucle pour qui fera 10 tours
    A= choice(l1) #Affecter à A la valeur choisie
    l2.append(A) #Ajouter à l2 la valeur A

print(l2) #Afficher l2
