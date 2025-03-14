#On définit le calcul à effectuer
def volBoite(l,p,h):
    volume = 0
    volume = l*p*h
    return volume

######################################
# Programme principal
######################################

nbr_cotes = int(input("Combien de côtés différents y a t'il? "))
l = 0
p = 0
h = 0

#On vérifie le nombre de côtés à calculer

if nbr_cotes == 1:
  l = float(input("Longueur de la boîte(en mètres): "))
  l = round(l,2)
  p = h = l
elif nbr_cotes == 2:
  l = float(input("Longueur de la boîte(en mètres): "))
  l = round(l,2)
  p = float(input("Largeur de la boîte(en mètres): "))
  p = round(p,2)
  h = l
elif nbr_cotes == 3:
  l = float(input("Longueur de la boîte(en mètres): "))
  l = round(l,2)
  p = float(input("Largeur de la boîte(en mètres): "))
  p = round(p,2)
  h = float(input("Hauteur de la boîte(en mètres): "))
  h = round(h,2)
else:
  print("Vous n'avez pas le nombre requis de côtés")

print("le volume de la boîte est de",volBoite(l,p,h),"mètres cubes")
