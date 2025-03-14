nbr_secondes1 = int(input("Veuillez entrez un nombre entier de secondes "))
# le nombre se secondes à convertir
nbr_secondes2 = nbr_secondes1 # on calcule sur une nouvelle variable pour garder la
#valeur initiale

nbr_années = nbr_secondes2//(60*60*24*365) #Calcul nombre années restantes
nbr_secondes2 = nbr_secondes2%(60*60*24*365) #Calcul nombre secondes restantes

nbr_mois = nbr_secondes2//(60*60*24*30) #Calcul nombre mois restantes
nbr_secondes2 = nbr_secondes2%(60*60*24*30) #Calcul nombre secondes restantes

nbr_jours = nbr_secondes2//(60*60*24) #Calcul nombre jours restantes
nbr_secondes2 = nbr_secondes2%(60*60*24) #Calcul nombre secondes restantes

nbr_heures =nbr_secondes2//(60*60) #Calcul nombre heures restantes
nbr_secondes2 =nbr_secondes2%(60*60) #Calcul nombre secondes restantes

nbr_minutes = nbr_secondes2//(60) #Calcul nombre minutes restantes
nbr_secondes2 =nbr_secondes2%(60) #Calcul nombre secondes restantes


print(nbr_secondes1," seconde(s) =", nbr_années," année(s),",nbr_mois," mois, ",
      nbr_jours," jour(s), ",nbr_heures," heure(s), ",nbr_minutes," minute(s), ",
      nbr_secondes2," seconde(s).") #Affichage des valeurs
