#! /usr/bin/python3



def Personne(nom,age,moyen):
    """
    creer une personne qui doit être représentée par un dictionnaire
    paramètres: nom: str
                age: int
                moyen: str
    resultat: perso: dico
    """
    return {'nomP':nom, 'ageP': age, 'moyenT': moyen}

def getNom(pers):
    """
    retourne le nom de la personne
    """
    return pers['nomP']

def getAge(pers):
    """
    retourne l'age de la personne
    """
    return pers['ageP']

def getMoyenTransport(pers):
    """
    retourne le moyen de transport utilisé par la personne
    """
    return pers['moyenT']

def setNom(pers,nom):
    """
    change le nom de la persone
    """
    pers['nomP'] = nom

def setAge(pers,age):
    """
    change l'age de la personne
    """
    pers['ageP'] = age

def setMoyenTransport(pers,moyen):
    """ 
    change le moyen de transport de la personne
    """
    pers['moyenT'] = moyen

def affichePers(pers):
    """
    affiche une personne
    """
    print('-'*10)
    print('Nom:',getNom(pers))
    print('Age:',getAge(pers))
    print('Moyen de transport:', getMoyenTransport(pers))
    print('-'*10)


def lireFichierPersonnes(nomFic):
    """
    lit une liste de personnes contenue dans un fichier
    """
    fic=open(nomFic)
    listePers=[]
    for ligne in fic:
        [nom,age,moyenTrans]=ligne[:len(ligne)-1].split(',')
        listePers.append(Personne(nom,int(age),moyenTrans))
    fic.close()
    return listePers

def afficheListePersonnes(listePers):
    """
    affiche une liste de personnes
    """
    for perso in listePers:
        print(affichePers(perso))

def ageMoyenUtilisateurTransport(listePers,nomMoyenTransport):
    """
    retourne l'age moyen des personnes qui utilise comme moyen de transport
    celui passé en paramètres. Si aucune personne n'utilise ce moyen de transport
    la fonction doit retourner -1
    """
    somme_age = 0
    nbr_perso = 0
    age_moyen = -1
    for perso in listePers:
        if getMoyenTransport(perso) == nomMoyenTransport:
            somme_age += getAge(perso)
            nbr_perso += 1
    if somme_age != 0:
        age_moyen = somme_age/nbr_perso
    return age_moyen

def listeMoyensTransport(listePers):
    """
    retourne sous la forme d'une liste de chaines de caractères la liste des 
    moyens de transport utilisés par les personne de listePers
    """
    transports = set()
    liste_transport = []
    for perso in listePers:
        transports.add(getMoyenTransport(perso))
    for vehicules in transports:
        liste_transport.append(vehicules)
    return liste_transport

### programme principal
if __name__=='__main__':
    lireFichierPersonnes('personnes.txt')
    #ajoutez vos appels aux fonctions sur les personnes
