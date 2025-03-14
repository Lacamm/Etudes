#!/usr/bin/python3
# ===========
# Les données
# ===========
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

# ================================
# Outils de traitement des données
# ================================

def cree_liste_tout_les_noms(liste_personnages):
    liste_noms = []
    for nom,genre,taille in liste_personnages:
        liste_noms.append(nom)
    return liste_noms

def noms_feminins(liste_personnages):
    liste_noms_feminins = []
    for nom,genre,taille in liste_personnages:
        if genre == 'female':
            liste_noms_feminins.append(nom)
    return liste_noms_feminins

def persosGrand(liste_personnages):
    liste_grand = []
    for nom,genre,taille in liste_personnages:
        if taille > 180:
            liste_grand.append(nom)
    return liste_grand

def noms_masculins(liste_personnages):
    liste_noms_masculins = []
    for nom,genre,taille in liste_personnages:
        if genre == 'male':
            liste_noms_masculins.append(nom)
    return liste_noms_masculins


def noms_droides(liste_personnages):
    liste_noms_droides = []
    for nom,genre,taille in liste_personnages:
        if genre == 'droide':
            liste_noms_droides.append(nom)
    return liste_noms_droides

def liste_tout_le_monde(liste_personnages):
    liste_perso = []
    for nom,genre,taille in liste_personnages:
        liste_perso.append([nom,genre,taille])
    return liste_perso

print(liste_tout_le_monde(liste_personnages))
