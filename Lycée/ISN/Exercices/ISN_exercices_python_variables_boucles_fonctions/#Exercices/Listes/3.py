#Définition des listes
t1 = [31, 28,31, 30,31, 30,31,31, 30, 31, 30, 31]
t2 = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
   'aout', 'septembre', 'octobre', 'novembre', 'décembre']
t3 = []
# On remplit la liste t3 des éléments de t1 et t2
for n in range(len(t1)):
    t3.append(t2[n])
    t3.append(t1[n])
    t3.append('jours')

print(t3) #Affichage t3
