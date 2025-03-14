compte = 100
print("Au départ il y a 100 euros")
print("Avec un taus de 4.3%:")

#Somme des calculs des intérêts de chaque année
for n in range(21):
    compte = compte + compte*0.043
    compte = round(compte,2)
    print('Au bout de',n,'années, il y a', compte,"d'euros sur le compte")
