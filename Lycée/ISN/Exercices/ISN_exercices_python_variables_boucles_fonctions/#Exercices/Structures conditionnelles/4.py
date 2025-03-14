année = int (input("Veuillez entrer une année: ")) #saisir une année

if année%400==0 or année%4==0 and année%100!=0: #Vérifier si elle est bissetxile
#On affiche le résultat
    print(année,"est année bissextile")
else:
    print(année,"n'est pas une année bissetxile")
