print('La fin de la saisie des notes ne fera par l\'ajout d\'une note négative')

notes = float(input("Veuillez entrer vos notes: ")) #Saisie d'une note

#Définition des variables
notesTT = []
nbr_notes = 0



#Calcul du toatal des notes, de la moyenne, de la notes la plus élevés et la plus basse
while notes >= 0:
    while notes > 20: #Saisie d'une note inférieure à 20
        notes = float(input("Veuillez entrer vos notes inférieures à 20: "))
    notesTT.append (notes)
    nbr_notes = nbr_notes + 1
    maximum = max(notesTT)
    minimum = min(notesTT)
    moyenne = sum(notesTT)/len(notesTT)

#Affichage des valeurs
    print ("")
    print("Le nombre de notes est : ", nbr_notes)
    print("La moyenne des notes est : ", moyenne)
    print("La note mximale est : ", maximum)
    print("La note minimale est : ", minimum)
    print ("")
    
#Nouveau départ de boucle
    notes = float(input("Veuillez entrez vos notes: "))
