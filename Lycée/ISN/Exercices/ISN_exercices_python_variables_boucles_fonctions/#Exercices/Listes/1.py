taille = int(input("Définissez la taille de la liste: "))
#Définition de la taille de la liste
l1 = [] # On créé une liste vide pour stocker les valeurs

for n in range(taille):
    l1.append(int(input("Rentrez une valeur: ")))
#On demande de rentrer les valeurs à comparer

a = l1[0] #Définition d'une variable

for i in range(taille):
    if l1[i]>a:
        a = l1[i]
#On recherche le plus grand nombre de la liste

print("la plus grande valeur de la liste est: ",a)
#Affichage de la plus grande valeur de la liste


print("""
2° Méthode, voir le code
""")


"""Ici on définit grâce  à la commande def... : une fonction nommée maximum
qui prend un unique paramètre : tableau
dont le but est de déterminer le plus grans élément de la lsite tableau"""

def maximum(l1):
    max = l1[0]
    for c in range(1,taille):
        if l1[c] > max:
            max = l1 [c]
    return(max)
# la fonction retourne la variable max

print("Le plus grand élément de la lsite est  : ", maximum(l1)) #  on affiche le résultat retourné par la
# fonction maximum appliqué à la liste t1
