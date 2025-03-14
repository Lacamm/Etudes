chaine = input() #on écrit une phrase
taille_de_la_phrase = len(chaine) #on calcule la taille de a phrase
n = 0
compteur = 0

for n in range(taille_de_la_phrase): #Boucle pour que le fera autant de fois que la phrase comporte des lettres
    if 'e' in chaine [n]: # Si il y a un 'e' à la lettre 'n'
        compteur += 1 #on incrémente le compteur

print('Il y a ',compteur, '"e" dans la phrase') #on affiche le nombre de 'e' dans la phrase
