taille = int(input("Entrer la taille de la liste : "))
liste = [] # on créé une liste vide
nombre_de_nombre_pairs = 0
liste_nombre_pairs = []

for i in range(taille): # Pour  chaque passage valeur de i = 0 à i = taille - 1 
    liste.append(int(input("Entrer la valeur suivante : "))) #on ajoute  à la liste précédente la valeur suivante
    if liste[i]%2 == False:
        nombre_de_nombre_pairs = nombre_de_nombre_pairs + 1
        liste_nombre_pairs.append(liste[i])

print("Il y a",nombre_de_nombre_pairs,"nombres pairs")
print(liste_nombre_pairs)
