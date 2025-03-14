def augementeTous(liste):
    """
        Cette fonction incrémente de 1 tous les éléments de la liste
        Paramètre : une liste de nombre
        Résultat : None (rien)

    """
2	    for i in range(len(liste)):
3	        liste[i] = liste[i]+1 #ICI
4	maListe = [5,3,7,9]
5	augementeTous(maListe)
6	print(maListe)