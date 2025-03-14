def compteCar(ca,ch): #on définit le compteur de 'ca'
    nbr_ca = 0
    for n in range (len(ch)): #on vérifie lettre par lettre
        if ca == ch[n]:  #On démarre le compteur
            nbr_ca += 1
    return nbr_ca

ch = input("Chaîne de caractère: ") #l'utilisateur rentre une phrase
ca = input("Caractère : ") #l'utilisateur rentre le caractère à rechercher
print(compteCar(ca,ch)) #On affiche