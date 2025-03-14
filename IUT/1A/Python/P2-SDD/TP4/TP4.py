#!/usr/bin/python3

######################################################################
# Feuille de TP 4
# NOM : ALLAIN Lucas
#######################################################################

#######################################################################

print("==========================================")
print("Exercice 0")

liste = ['A','C','a','A','A','a']

def dico_frequence(liste):
    frequence = {}
    for elem in liste:
        if elem in frequence:
            frequence[elem] += 1
        else:
            frequence[elem] = 1
    return frequence

assert dico_frequence(liste) == {'A':3, 'a':2, 'C':1}, 'Pb avec dico_frequence(liste)'


def lettre_frequence(liste):
    frequence = dico_frequence(liste)
    apparition_lettre = 0
    lettre_frequente = None
    for (lettre, apparition) in frequence.items():
        if apparition_lettre < apparition:
            apparition_lettre = apparition
            lettre_frequente = lettre
    return lettre_frequente

assert lettre_frequence(liste) == 'A', 'Pb avec lettre_frequence(liste)'

print("==========================================")
print("Exercice 1 - Echauffement - Fan-club")

groupePrefere={'Florent':'Chantal Goya','Celine':'SuperBus', 'Julien':'ACDC','Denys':'ACDC','Caroline':'Chantal Goya'}
  
def fansDe(groupePrefere,nomGroupe):
    ensemble_fans = set()
    for (fan, groupe) in groupePrefere.items():
        if nomGroupe == groupe:
            ensemble_fans.add(fan)
    return ensemble_fans

assert fansDe(groupePrefere,'Chantal Goya') == {'Florent','Caroline'}
assert fansDe(groupePrefere,'ACDC') == {'Julien','Denys'}

def dico_fans(groupePrefere):
    dicoFans = {}
    for (fan, groupe) in groupePrefere.items():
        if groupe not in dicoFans:
            dicoFans[groupe] =  set()
        dicoFans[groupe].add(fan)
    return dicoFans


assert dico_fans(groupePrefere) == {'Chantal Goya': {'Florent','Caroline'}, 'ACDC': {'Julien','Denys'}, 'SuperBus':{'Celine'}}


print("==========================================")
print("Exercice 2 - Naturalistes en herbe")


regimeAlimentaire={
  'Requin':{'Nageur','Sac Plastique','Poisson'},
  'Nageur':{'Poisson','Noisette'},
  'Lion':{'Gazelle'},
  'Ecureuil':{'Noisette'}}
nourritureDisponible={
  'Ocean':{'Poisson','Sac Plastique','Nageur'},
  'Savane':{'Gazelle'},
  'Jardin avec piscine':{'Nageur','Noisette'}
}

def inverse(dico):
    dico_inverse = {}
    for (predateur, nourriture) in dico.items():
        for proie in nourriture:
            if proie not in dico_inverse.keys():
                dico_inverse[proie] = set()
            dico_inverse[proie].add(predateur)
    return dico_inverse

assert inverse(regimeAlimentaire) == {'Poisson': {'Nageur', 'Requin'}, 'Sac Plastique': {'Requin'}, 'Nageur': {'Requin'}, 'Noisette': {'Nageur', 'Ecureuil'}, 'Gazelle': {'Lion'}}


print("   Avez-vous pensé à écrire des tests pour l'exercice 2 ?")


print("==========================================")
print("Exercice 3 - Rapide et furieux, une série qui se répète un peu")


#Version 1
def nombre_apparition(chaine, caractere):
    cpt=0
    for char in chaine: 
        # ICI
        if caractere == char:
            cpt=cpt+1
    return cpt

def caracteres_en_double(chaine):
    """
    resultat : l'ensemble des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    caracteresRepetees = set() 
    for caractere in chaine:
        if nombre_apparition(chaine, caractere) > 1:
            caracteresRepetees.add(caractere)
    return caracteresRepetees


print(caracteres_en_double("Yolo"))

print(caracteres_en_double("Tu lui brises le coeur, je te brise la tête !")) # 45 caractères

#Version 2
def caracteres_en_double(chaine):
    """
    resultat : la liste des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    dejaVu=[]
    caracteres_repetes=[]
    for caractere in chaine:
        if caractere not in dejaVu:
            dejaVu.append(caractere)
        else:
            caracteres_repetes.append(caractere)
    return caracteres_repetes


#Version 3
def caracteres_en_double(chaine):
    """
    resultat : l'ensemble des caractères qui apparaissent au
    moins 2 fois dans la chaine
    """
    dejaVu=set()
    caracteres_repetes=set()
    for caractere in chaine:
        if caractere not in dejaVu:
            dejaVu.add(caractere)
        else:
            caracteres_repetes.add(caractere)
    return caracteres_repetes

print("==========================================")
print("Exercice 4 - Oh les amoureux !")

ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida', 
     'Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri',
     'Gaston':'Beatrice','Henri':'Firmin'}

def reciproque(dicoAmoureux):
    """ 
    TODO
    """
    pass
    

# assert len(reciproque(ATM))==2, "Il y a très certainement des couples en double"
# assert ('Henri','Firmin') in reciproque(ATM) or ('Firmin','Henri') in reciproque(ATM)
# assert ('Dalida','Cesar')  in reciproque(ATM) or ('Cesar','Dalida') in les_couples(ATM)


print("==========================================")
print("Exercice 6 - Le retour des timides maladifs")

amoursATM={
  'Armand':{'Beatrice','Dalida'},
  'Beatrice':{'Cesar','Armand'},
  'Cesar':{'Dalida','Gaston'}, 
  'Dalida':{'Cesar','Armand'},
  'Etienne':{'Beatrice','Firmin'},
  'Firmin':{'Henri','Beatrice','Armand','Dalida'},
  'Gaston':{'Beatrice','Dalida','Cesar'},
  'Henri':{'Firmin','Armand','Cesar','Henri'}}
