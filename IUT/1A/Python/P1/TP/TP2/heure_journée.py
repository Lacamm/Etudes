heure = int(input('Heure entière: '))
while heure > 23 or heure < 0:
    print('Heure incorrecte')
    heure = int(input('Heure entière: '))
etat =''

def journee(heure,etat):
    """
    Cette fonction a pour objectif de déterminer dans quelle partie de la
    journée on est:
    Paramètres
       param1: C'est l'heure donnée    
    Résultat: Un str qui dit dans quelle partie de la journée on est
    """
    if 7 <= heure < 19:
        etat = " et c'est le jour"
    else:
        etat = " et c'est la nuit"  
    if 6 <= heure < 7:
        etat = "C'est le matin"+etat
    elif 7 <= heure < 12:
        etat = "C'est le matin"+etat
    elif 12 <= heure < 18:
        etat = "C'est l'après-midi"+etat
    elif 18 <= heure < 21:
        etat = "C'est la soirée"+etat
    else:
        etat = "C'est la nuit"
    
    return etat

assert journee(3) == "C'est la nuit","problème, on attend:C'est la nuit"
assert journee(6) == "C'est le matin et c'est la nuit","problème, on attend:C'est le matin et c'est la nuit"
assert journee(8) == "C'est le matin et c'est le jour","problème, on attend:C'est le matin et c'est le jour"
assert journee(16) == "C'est l'après-midi et c'est le jour","problème, on attend:C'est l'après-midi et c'est le jour"
assert journee(18) == "C'est la soirée et c'est le jour","problème, on attend:C'est la soirée et c'est le jour"
assert journee(19) == "C'est la soirée et c'est la nuit","problème, on attend:C'est la soirée et c'est la nuit"

print(journee(heure,etat))

#again = input('again? y')
#while again == 'y':
#    heure = int(input('Heure entière: '))
#    print(journee(heure))
#    again = input('again? y')