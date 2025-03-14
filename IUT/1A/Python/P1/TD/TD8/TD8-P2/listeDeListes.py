#!/usr/bin/python3

################################################
## Exercice sur les listes de listes          ##
## Nom: ALLAIN Lucas                          ##
################################################

# liste de listes pour le premier ascii art 
asciiart1=[[' ', '|', '\\', '/', '\\', '/', '\\', '/', '|', ' ', ' '],[' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '],\
   [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' '], [' ', '|', ' ', '(', 'o', ')', '(', 'o', ')', ' ', ' '],\
   [' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '_', ')', ' '], [' ', ' ', '|', ' ', ',', '_', '_', '_', '|', ' ', ' '],\
   [' ', ' ', '|', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' '], [' ', '/', '_', '_', '_', '_', '\\', ' ', ' ', ' ', ' '],\
   ['/', ' ', ' ', ' ', ' ', ' ', ' ', '\\']]

# liste de listes pour le deuxième ascii art 
asciiart2=[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', 'n', 'n', 'n', 'n', '_'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', 'G', 'G', 'G', 'G', 'M', 'M', 'b'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', 'p', '~', 'q', 'p', '~', '~', 'q', 'M', 'b'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', '|', '@', '|', '|', '@', ')', ' ', 'M', '|'],\
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '@', ',', '-', '-', '-', '-', '.', 'J', 'M', '|'],\
    [' ', ' ', ' ', ' ', ' ', ' ', 'J', 'S', '^', '\\', '_', '_', '/', ' ', ' ', 'q', 'K', 'L'],\
    [' ', ' ', ' ', ' ', ' ', 'd', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', 'K', 'R', 'b'],\
    [' ', ' ', ' ', ' ', 'd', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'q', 'K', 'K', 'b'],\
    [' ', ' ', ' ', 'f', 'Z', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', 'M', 'M', 'b'],\
    [' ', ' ', ' ', 'H', 'Z', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', 'M', 'M', 'M'],\
    [' ', ' ', ' ', 'F', 'q', 'M', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', 'M', 'M', 'M'],\
    [' ', '_', '_', '|', ' ', '"', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\\', 'd', 'S', '"', 'q', 'M', 'L'],\
    [' ', '|', ' ', ' ', ' ', ' ', '`', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '`', "'", ' ', '\\', 'Z', 'q'],\
    ['_', ')', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '.', '_', '_', '_', '.', ',', '|', ' ', ' ', ' ', ' ', ' ', '.', "'"], \
    ['\\', '_', '_', '_', '_', ' ', ' ', ' ', ')', 'M', 'M', 'M', 'M', 'M', 'P', '|', ' ', ' ', ' ', '.', "'"],\
    [' ', ' ', ' ', ' ', ' ', '`', '-', "'", ' ', ' ', ' ', ' ', ' ', ' ', ' ', '`', '-', '-', "'", ' ', 'h', 'j', 'm']]


def listeDeListesToStr(liste):
    """
    cette fonction transforme une liste de listes en une chaine de caractères
    où les éléments de la liste principale sont accolés sur une même ligne
    paramètre:
    résultat:
    """
    res = ""
    for n in range(len(liste)):
        for j in range(len(liste[n])):
            res += str(liste[n][j])
        res += "\n"
    return res

assert listeDeListesToStr([])=='',"Pb appel listeDeListesToStr([])"
assert listeDeListesToStr([[0,1,2],[3,4,5],[6,7,8]])=='012\n345\n678\n', "Pb appel listeDeListesToStr([[0,1,2][3,4,5][6,7,8]])"
assert listeDeListesToStr([['X',' ','O'],['O','X',' '],['O',' ','X']])=='X O\nOX \nO X\n',"Pb appel listeDeListesToStr([['X',' ','O'],['O','X',' '],['O',' ','X']])"
print(listeDeListesToStr(asciiart1))
print(listeDeListesToStr(asciiart2))

print(listeDeListesToStr([]))
print(listeDeListesToStr([[0,1,2],[3,4,5],[6,7,8]]))=='012\n345\n678\n', "Pb appel listeDeListesToStr([[0,1,2][3,4,5][6,7,8]])"
print(listeDeListesToStr([['X',' ','O'],['O','X',' '],['O',' ','X']]))=='X O\nOX \nO X\n',"Pb appel listeDeListesToStr([['X',' ','O'],['O','X',' '],['O',' ','X']])"



def maxDansListeDeListes(liste):
    """
    retourne le plus grand élément d'une liste de listes
    paramètre:
    résultat:
    """
    maxi = None
    if liste != []:
        maxi = liste [0][0]
        for n in range(len(liste)):
            for j in range(len(liste[n])):
                if liste [n][j] > maxi:
                    maxi = liste [n][j]
    return maxi

print(maxDansListeDeListes([[0,1,2],[3,4,5],[6,7,8]]))
print(maxDansListeDeListes([[0,11,25],[7,14,58],[26,17,8]]))
print(maxDansListeDeListes([]))
assert maxDansListeDeListes([[0,1,2],[3,4,5],[6,7,8]])==8,"Pb appel maxDansListeDeListes([[0,1,2],[3,4,5],[6,7,8]])"
assert maxDansListeDeListes([[0,11,25],[7,14,58],[26,17,8]])==58,"Pb appel maxDansListeDeListes([[0,11,25],[7,14,58],[26,17,8]])"
assert maxDansListeDeListes([])==None,"Pb appel maxDansListeDeListes([])"




def maxParLigneDansListeDeListes(liste):
    """
    retourne la liste des plus grands éléments de chaque ligne dans une liste de listes
    paramètre:
    résultat:
    """
    listeMaxi = []
    maxi = None
    if liste != []:
        maxi = liste [0][0]
        for n in range(len(liste)):
            if liste[n] == []:
                    maxi = None
            else:
                maxi = liste [n][0]
                for j in range(len(liste[n])):
                    if liste [n][j] > maxi:
                        maxi = liste [n][j]
            listeMaxi.append(maxi)
    else:
        listeMaxi = None
    return listeMaxi

print()
print()
print(maxParLigneDansListeDeListes([[0,1,2],[3,4,5],[6,7,8]]))
print(maxParLigneDansListeDeListes([[0,11,25],[7,14,58],[26,17,8]]))
print(maxParLigneDansListeDeListes([[45,1,24],[],[47,85,2,14]]))

assert maxParLigneDansListeDeListes([[0,1,2],[3,4,5],[6,7,8]])==[2,5,8],\
       "Pb Appel maxParLigneDansListeDeListes([[0,1,2],[3,4,5],[6,7,8]])"
assert maxParLigneDansListeDeListes([[0,11,25],[7,14,58],[26,17,8]])==[25,58,26],\
       "Pb Appel maxParLigneDansListeDeListes([[0,11,25],[7,14,58],[26,17,8]])"
assert maxParLigneDansListeDeListes([[45,1,24],[],[47,85,2,14]])==[45,None,85],\
       "Pb Appel maxParLigneDansListeDeListes([[45,1,24],[],[47,85,2,14]])"