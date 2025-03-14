numero_objet_bot = 0

inventaire_bot = ['CAS', 'DRL', 'REE', 'BOM', 'ADC']


objet_gene = input('objet_gene = ')

print(objet_gene)
print(inventaire_bot[1])



for n in range(len(inventaire_bot)):
    if objet_gene == inventaire_bot[n]:
        numero_objet_bot = n
        print(n)
        print('salut')
    

print("")
print(n)
print(numero_objet_bot)
