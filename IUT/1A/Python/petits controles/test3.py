#!/usr/bin/python3

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
