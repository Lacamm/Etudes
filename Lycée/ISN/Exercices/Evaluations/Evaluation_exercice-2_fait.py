prenom = input("Veuillez entrer votre prénom: ")
nom = input("Veuillez entrer votre nom: ")

if len(nom) > 6:
    nom = nom[0:6]
print(prenom[0],'.',nom)
