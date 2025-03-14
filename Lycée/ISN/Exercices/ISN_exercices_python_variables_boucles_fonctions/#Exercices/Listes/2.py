#On définit la taille de la liste
taille_l1 = int(input("Définisez la taille de la liste: "))
l1 = []

#On donne les valeurs de la liste
for n in range(taille_l1):
    l1.append(int(input("Entrez des valeurs: ")))

#Listes pour stockage
liste_paire = []
liste_impaire = []

#On vérifie que le nombre soit un multiple de 2 et on le range dans la liste correspondante
for i in l1:
    if i%2:
        liste_paire.append(i)
    else:
        liste_impaire.append(i)

print("Liste contenant les nombres pairs: ",liste_paire) #Affichage des impairs
print("Liste contenant les nombres impairs: ",liste_impaire) #Affichage des pairs

#tout ce que j'ai essayé ce rapporte à la correction
