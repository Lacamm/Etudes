entier = int(input("Veuillez rentrer un entier naturel: ")) #On saisit un nombre entier
i = entier
a = 0

for n in range(entier): #On regarde si pour chaque valeur depuis le nombre entrer et 0
    quotient = entier/i #On dic=vise le nombre entrer par le nouveau diviseur
    if int(i)*int(quotient)==entier: #Si la multiplication des entiers donne le nombre entrer
        print(i) #On l'affiche
        a = a+1 #On incrémente le nombre de diviseur trouvés
        i = i-1 #on passe au diviseur suivant
    else:       #Sinon
        i = i-1 #on passe au diviseur suivant
print(entier,"a",a,"diviseurs") #On affiche les résultats
    
