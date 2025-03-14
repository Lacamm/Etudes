#Nombre dont on va calculer les coefficiants binomiaux    
n = int(input("Entrer le nombre entier n : "))
coeffsBin = [] #Liste qui va receuillir les coefficiant binomiaux
ligne = [1] 

for j in range(1,n+1): #On s'occupe de la ligne 1 dont on remplit
#simplement de 0 après le 1
    ligne.append(0)
coeffsBin.append(ligne)

#On s'occupe ensuite de toutes les autres lignes
for i in range(1,n+1): #A chaque début le ligne le coefficiant binomial est 1
    ligne = [1]
    for j in range(1,n+1): #On calcule les coefficaiants suivants
        if j<i: #Si ca "appartient" au triangle Pascal
            #On applique la formule de Pascal
            ligne.append(coeffsBin[i-1][j-1] + coeffsBin[i-1][j])
        elif j==i: #"Bords" du triangle de Pascal
            ligne.append(1)
        else: #Tout ce qui n'appartient pas au triangle de Pascal
            ligne.append(0)
    coeffsBin.append(ligne)


#Affichage de toutes les listes dont les coefficiants ont étés calculés
for i in range(0,n+1):
    print(coeffsBin[i])


#J'ai repris la correction
