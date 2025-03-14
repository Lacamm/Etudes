#position bateau
position_bateau = (4,7)

#on sélectionne les cases à tirr
tirL = int(input("Sélectionnez la ligne à attaquée: "))
tirC = int(input("Sélectionnez la colonne à attaquée: "))

if tirL < 1 or tirL > 10 or tirC < 1 or tirC >10: #on est hors du champ de bataille
    print("Vous êtes hors du champ de bataille, mon général")
elif tirL == position_bateau[0] and tirC == position_bateau[1]: #Une cases case est correcte
    print("La cible est détruite, mon commandant")
elif tirL == position_bateau[0] or tirC == position_bateau[1]: #le bateau est detruit
    print("La cible est en vue, mon capitaine, rectifiez le tir!!!")
#on est dans le champs de battaille mais rienn'est touché
elif tirL >= 1 and tirL <= 10 and tirC >= 1 and tirC <= 10 and tirL != position_bateau[0] and tirC != position_bateau[1]:
    print("c'est le plein brouillard...")
