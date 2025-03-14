from math import sqrt #On importe la fonction racine carrée

#On rentre les coefficiants de la fonction du second degré, et on les arrondies à 2 chiffres après la virgule
print("Veuillez rentrer les coefficiants a,b et c de l'équation du second degré")
a = float(input("a= "))
a = round(a,2)
b = float(input("b= "))
b = round(b,2)
c = float(input("c= "))
c = round(c,2)

#Calcul et affichage du discriminant
discriminant = (b**2)-(4*a*c)
print("Le discriminant vaut: ",discriminant)

#On cherche si il a des racines
if discriminant < 0: #Elle n'a pas de racine rélles
    print("Il n'y a pas de solutions réelles")
elif discriminant == 0: #Elle a une racine rélle
    print("Il n'y a qu'une racine réelle pour cette équation")
    print("x0=-b/2a= ",(-b)/(2*a)) #On la calcule
elif discriminant > 0: #Elle a deux racines rélles
    print("Il y a deux racines réelles pour cette équation")
    #On les calcule
    print("x1=(-b-sqrt(discriminant))/2a= ",round((-b-sqrt(discriminant))/(2*a),2))
    print("x2=(-b+sqrt(discriminant))/2a= ",round((-b+sqrt(discriminant))/(2*a),2))
