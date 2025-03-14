taux_de_change = 0.88715401 #Valeur du taux de change entre le dollar et l'euro

operation = int(input('Voulez-vous convertir des dollars (pressez 1) ou des euros (pressez 2)? ')) # On entre 1 ou 2

while operation!=1 and operation!=2:
    operation = int(input('Voulez-vous convertir des dollars (pressez 1) ou des euros (pressez 2)?'))  #Tant que 1 ou 2 n'est pas rentré on recommence

if operation == 1: #Si 1 est entré
    valeur_en_dollar = float(input('Valeur en dollar: ')) #On entre la valeur en dollar
    valeur_en_euro = valeur_en_dollar/taux_de_change      #On calcule la vlaeur en euro
    print('Valeur en euro: ',round(valeur_en_euro,2),'€') #on affiche la valeur en euro à 2 décimales

if operation == 2: #Si 2 est entré
    valeur_en_euro = float(input('Valeur en euro: ')) #On entre la valeur en euro
    valeur_en_dollar = taux_de_change*valeur_en_euro  #On calcule la vlaeur en dollar
    print('Valeur en dollar: ',round(valeur_en_dollar,2),'$')#on affiche la valeur en dollar à 2 décimales
