# Un personnage est modélisé par un tuple (nom, genre, taille)
liste_personnages=[
    ('Luke Skywalker', 'male', 172), 
    ('C-3PO', 'droide', 167), 
    ('R2-D2', 'droide', 96), 
    ('Darth Vader', 'male', 202), 
    ('Leia Organa', 'female', 150), 
    ('Owen Lars', 'male', 178), 
    ('Beru Whitesun lars', 'female', 165), 
    ('R5-D4', 'droide', 97), 
    ('Biggs Darklighter', 'male', 183), 
    ('Obi-Wan Kenobi', 'male', 182),
    ]


def noms(listeP):
    """
    renvoie la liste des noms des personnages
    """
    liste=[]
    for (nom,_,_) in listeP:
        liste.append(nom)
    return liste   

def filtre(listeP,critere):
    """
    renvoie la liste des personnages de type 'critere'
    """
    liste=[]
    for (nom,genre,_) in listeP:
	    if genre==critere:
		    liste.append(nom)
    return liste


def femmes(liste):
    """renvoie la liste des personnages féminins"""
    return filtre(liste,'female')
    
def droides(liste):
    """renvoie la liste des droides"""
    return filtre(liste,'droide')

def hommes(liste):
    """renvoie la liste des personnages masculins"""
    return filtre(liste,'male')

def grands(listeP):
    """
    renvoie la liste des personnages 'grands' cad taille >= 1.80m
    """
    liste=[]
    for (nom,_,taille) in listeP:
	    if taille>=180:
		    liste.append(nom)
    return liste
