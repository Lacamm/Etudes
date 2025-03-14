def premieres_occurences(liste):
    """ 
    résultat : un dictionnaire dont les clés sont les éléments de
    'liste' et les valeurs l'indice de la première occurence de chaque élément
    """
    for i in range (len(liste)):
        if liste liste[i] in dico.

# TESTS
liste=['a','b','b','a','!']
print(premieres_occurences(liste))


assert premieres_occurences(liste)=={'a':0, 'b':1, '!':4}
assert premieres_occurences([])=={}
print("Bravo ! Vous avez terminé la première question de cet exercice")