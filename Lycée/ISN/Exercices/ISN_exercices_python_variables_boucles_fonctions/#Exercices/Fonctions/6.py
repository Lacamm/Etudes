def eleMax(liste,debut,fin): #On cherche la valeur la plus grande dans l'intervalle
  Max = 0
  for n in range(debut, fin):
    if Max < liste[n]:
      Max = liste[n]
  return Max

###################
#Porg
###################

liste = []
Max = 0
taille_liste = int(input("Comment de valeurs y'a t'il dans la liste? ")) #on définit la taille de la liste

for i in range(taille_liste):
  liste.append(int(input("Entrez les valeurs: "))) #On remplit la liste

print("Sur quel intervalle doit t'on chercher?") #on définit l'intervalle sulequel on va chercher la plus grande valeur

debut = int(input("Début: "))
fin = int(input("fin: "))

if debut > fin:  #On vérifie bien que l'intervalle du début est plus petit que celui de la fin
  debut, fin = fin, debut

print("la valeur la plus élevée dans l'intervalle est",eleMax(liste,debut,fin))
