Annee_naissance = int(input("Entrer votre année de naissance : "))
Réponse = input ("Votre anniversaire a-t-il déjà eu lieu cette année ?")

if Réponse == 'oui':
    Age = 2016 - Annee_naissance
else:
    Age = 2016 - Annee_naissance - 1

print ("Votre âge est  : ", Age)

if Age < 7:
    print('Vous étes un enfant')
elif Age > 7 and Age < 18:
    print('Vous avez l\'âge de raison')
elif Age > 18:
    print('Vous étes majeur')
