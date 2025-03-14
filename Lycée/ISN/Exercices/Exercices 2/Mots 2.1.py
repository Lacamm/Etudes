mot=[] #Création d'une liste mot
mottotal=[] #Création d'une liste motttotal
rang = 0


while mot != '': #Tant que la touche entrée n'est pas préssée
    mot= input() #Mettre des mots dan liste mot
    rang = rang+1
    mottotal.append(rang)
    mottotal.append(mot) #Ajouter la liste mot à mottotal

print(mottotal) #Afficher la liste mottotal
print('Au revoir') #Afficher 'au revoir'
