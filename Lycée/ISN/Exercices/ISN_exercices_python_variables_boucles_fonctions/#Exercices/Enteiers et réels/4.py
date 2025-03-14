from math import* # utilisation du module math

angle_degré = float(input("Veuillez entrer une mesusre d'un agle en degré= ")) #Saisie de la valeur de l'angle en degré
sinus_angle = round(sin(angle_degré/180*pi),3) #Calcul du sinus de l'angle à 3 décimales
print("Le sinus de l'angle est= ",sinus_angle) #Affichage de la valeur du sinus
