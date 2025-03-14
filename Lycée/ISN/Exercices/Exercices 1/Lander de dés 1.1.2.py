from random import randint #Importer la fonction randint

N= int(input()) #Affecter à N une valeur entière
print (N)       #Afficher N
F= int(input()) #Affecter à F une valeur entière
print (F)       #Afficher F
P=0             #Affecter à P la valeur 0

for i in range(N): #Création d'une boucle pour que l'on fera N fois

   R=(randint(1,F)) #Affecter à R la valeur d'un dés
   print(R)         #Afficher la valeur du dés
   P=P+R            #Faire la somme du résultat R avec la somme des résulats précédents

print (P) #Afficher la somme de tout les résultats
