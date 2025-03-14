def table(n): #On fait les calculs 
  a = 1
  for i in range(20):
    print(a,'x',n,'=',n*a)
    a += 1

###################
#Prog
###################

n = int(input("De quel entier voulez-vous avoir la table? ")) #O définit de quel nomnre on veut la table

print("Table de",n)
table(n) #On exécute la fonction
