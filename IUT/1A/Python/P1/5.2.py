#!/usr/bin/python

def dialogueMotDePasse():

    ################ Fonctions ################
    def initialisation(MDP):
        motDePasse = str(input("Créez votre mot de passe: "))
        MDP = []
        for n in range(len(motDePasse)):
            MDP.append(motDePasse[n])
        return MDP

    def nombresCaracteres(MDP):
        while len(MDP) < 8:
            print("Votre mot de passe doit contenir au moins 8 caractères")
            initialisation(MDP)
        return MDP

    def nombreChiffres(MDP):
        chiffre  = False
        for caractere in  MDP:
            if caractere.isdigit():
                chiffre = True
        while not chiffre:
            print("Votre mot de passe doit contenir au moins 1 chiffre")
            initialisation(MDP)
        return MDP

    def nombreEspace(MDP):
        while ' ' in MDP:
            print("Votre mot de passe ne doit pas contenir d'espace")
            initialisation(MDP)
        return MDP

    def nombreMajuscules(MDP):
        majuscule  = False
        for caractere in  MDP:
            if caractere.isupper():
                majuscule = True
        while not majuscule:
            print("Votre mot de passe doit contenir au moins 1 majuscule")
            initialisation(MDP)
        return MDP

    def nombreMajusculesConsecutives(MDP):
        majusculesConsecutives = False
        for indice in range(len(MDP)):
            if MDP[indice].isupper() and MDP[indice-1].isupper():
                majusculesConsecutives = True
        while majusculesConsecutives == True:
            print("Votre mot de passe ne doit pas contenir 2 majuscules consécutives")
            initialisation(MDP)
        return MDP

    def ponctuation(MDP):
        ponctuation  = False
        for caractere in  MDP:
            if not caractere.isdigit() or not caractere.isalpha():
                ponctuation = True
        while ponctuation:
            print("Votre mot de passe ne doit pas contenir de ponctuation")
            initialisation(MDP)
        return MDP


    ################ Main  ################

    global MDP
    MDP = []

    initialisation(MDP)
    nombresCaracteres(MDP)
    nombreChiffres(MDP)
    nombreEspace(MDP)
    nombreMajuscules(MDP)
    nombreMajusculesConsecutives(MDP)
    ponctuation(MDP)

    motDePasse = "".join(MDP)
    print(motDePasse)
    print("Votre mot de passe est créé!")

    return motDePasse


dialogueMotDePasse()
