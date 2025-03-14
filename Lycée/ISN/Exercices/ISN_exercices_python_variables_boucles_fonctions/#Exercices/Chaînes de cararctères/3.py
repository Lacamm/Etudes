mot = input("Entrer un mot : ")
# On initialise notre chaine en lui affectant la première
# lettre du mot entré par l'utilisateur.
chaine = mot[0]

# Si la chaine de carcatère ne comporte qu'une lettre
#la boucle n'est pas parcourue

if len(mot)>1:
    for i in range (1,len(mot)):
        chaine = chaine + "*" + mot[i] 

print(chaine)

# J'ai bien cherché mais j'ai pas trouvé
