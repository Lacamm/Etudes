phr = input("Veuillez entrer une phrase: ") #On saisit une phrase
taille_phr = len(phr) #on calcule la taille de la liste
i = 0
nbr_z = 0

for n in range(taille_phr):
    if 'z' in phr[i]: #On regarde lettre aprés lettre si c'est un z ou non
        nbr_z= nbr_z+1 #On incrémente le nombre de z
        i=i+1 #On change de lettre
    elif 'Z' in phr[i]: #On regarde lettre aprés lettre si c'est un z ou non
        nbr_z= nbr_z+1 #On incrémente le nombre de z
        i=i+1 #On change de lettre
    else:
        i=i+1 #On change de lettre
print("Il y a",nbr_z,"'z' dans la phrase")
