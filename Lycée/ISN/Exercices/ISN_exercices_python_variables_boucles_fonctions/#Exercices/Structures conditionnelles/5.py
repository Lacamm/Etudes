print("Veuillez rentrer trois longueurs") #Saisir les valeurs des longueurs

a = float(input("Longueur 1: ")) #longueur 1
cote1 = round(a,2)               #on l'arrondie pour faciliter les calculs
b = float(input("Longueur 2: ")) #longueur 2
cote2 = round(b,2)              #on l'arrondie pour faciliter les calculs
c = float(input("Longueur 3: ")) #longueur 3
cote3 = round(c,2)              #on l'arrondie pour faciliter les calculs

#On les range dans une liste pour déterminer la plus grande longueur
cotes = [cote1,cote2,cote3]
cotes.sort(reverse=True)


if cotes[0]<cotes[1]+cotes[2]: #On vérifie que c'est un triangle
    if cotes[0]**2==cotes[1]**2+cotes[2]**2: #on vérifie si il est rectangle
        print("C'est un triangle rectangle")
    elif cotes[0]==cotes[1]==cotes[2]: #on vérifie si il est équilatéral
        print("C'est un triangle équilatéral")
    elif cotes[0]==cotes[1]!=cotes[2] or cotes[0]!=cotes[1]==cotes[2] or cotes[0]==cotes[2]!=cotes[1]:
        #On vérifie si il est isocèle
        print("C'est un triangle isocèle")
    else:
        print("C'est un triangle quelconque")
else:
    print("Ce n'est pas un triangle") 
