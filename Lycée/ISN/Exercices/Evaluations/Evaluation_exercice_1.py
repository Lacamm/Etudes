Annee_naissance = int(input("Entrer votre année de naissance : "))
Réponse = input ("Votre anniversaire a-t-il déjà eu lieu cette année ?")
réponse2 = {'oui', 'non'}

if Réponse == 'oui':
    Age = 2016 - Annee_naissance
else:
    Age = 2016 - Annee_naissance - 1

print ("Votre âge est  : ", Age)

