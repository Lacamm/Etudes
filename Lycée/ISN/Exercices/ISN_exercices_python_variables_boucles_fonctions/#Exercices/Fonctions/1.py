#On définit le calcul à effectuer
def volBoite(l,p,h):
    volume = 0
    volume = l*p*h
    return volume

######################################
# Programme principal
######################################

#On saisit les valeurs
l = float(input("Longueur de la boîte(en mètres): "))
l = round(l,2)
p = float(input("Largeur de la boîte(en mètres): "))
p = round(p,2)
h = float(input("Hauteur de la boîte(en mètres): "))
h = round(h,2)

volBoite(l,p,h) #on appelle la fonction qui fera le calcul

print("le volume de la boîte est de",volBoite(l,p,h),"mètres cubes")