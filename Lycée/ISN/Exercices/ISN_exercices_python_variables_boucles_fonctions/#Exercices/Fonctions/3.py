def indexMax(l1):
    Max = l1[0]
    index = 1
    for i in range(len(l1)): #On teste les valeurs
        if Max < l1[i]:
            Max = l1[i]
            index = i+1
    return index, Max 
#####################
#Prog
####################
#Variables
l1 = []
i = 0
n = 0

print("Entrez 5 valeurs")

for n in range(5):
    l1.append(int(input("Entrez des valeurs: "))) #Valeurs de la liste

print(indexMax(l1))
