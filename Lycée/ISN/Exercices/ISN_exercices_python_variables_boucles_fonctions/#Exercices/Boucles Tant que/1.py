n = 1

#On calcule les 20 premiers résultats de la table de 7
while n <= 20:
    résultat = 7*n
    #On regarde si c'est un multiple de 3
    if résultat%3 == False:
       print('7 X',n,"=",résultat,'*') 
    else:
        print('7 X',n,"=",résultat)
    n+=1
