            ########################################################
                  # Première Fonction: Génération d'un objet
            ########################################################


###############################################
#  Génération des objets: Fonction Secondaire
###############################################
  
def choix_objet():
  proba_classe = randint(1,100) # Générer une classe d'objet "aléatoirement"
  if proba_classe <= 50:        # On choisit un un objet dans la classe 1
    proba_objet = randint(1,2)
    if proba_objet == 1:
      objet_genere_aleatoire = 'BOM'
    else:
      objet_genere_aleatoire = 'REE'
  elif 50 < proba_classe <= 85: # On choisit un un objet dans la classe 2
    proba_objet = randint(1,2)
    if proba_objet == 1:
      objet_genere_aleatoire = 'DRL'
    else:
      objet_genere_aleatoire = 'ADC'
  else:                         # On choisit un un objet dans la classe 3
    objet_genere_aleatoire = 'CAS'
  return objet_genere_aleatoire


################################################
#   Génération des objets: Fonction Principale
################################################

def generation_objet(tour):

  # Déclaration des différentes variables
  nombre_objet_generes = 0
  droit = 0 # Désigne qui a le droit de recevoir un objet(drop, joueur ou bot)
  objet_generes_aleatoire = ""
  
  # On vérifie que les objets du drop apparaisent tout les 10 tours
  if tour[0]%10 == 0 and tour[0] != 0 and tour[1] != 2:
    nombre_objet_generes = 3
    droit = 1
  # On vérifie que les objets du joueur tout les 3 tours(SES tours)
  elif tour[0]%3 == 0 and tour[0] != 0 and tour[1] == 1:
    nombre_objet_generes = 1
    droit = 2
  # On vérifie que les objets du bot tout les 3 tours(SES tours)
  elif tour[0]%3 == 0 and tour[0] != 0 and tour[1] == 2:
    nombre_objet_generes = 1
    droit = 3

  for j in range(nombre_objet_generes): # On génère le nombre d'objets nécessaire    
    if droit == 1:                      # Les objets générés sont pour le drop
      if len(drop) == 3:                # On change le drop au bout de 10 tours, si il n'est pas pris
        for n in range(len(drop)):
          drop.remove(drop[0])
      drop.append(choix_objet())
    elif droit == 2:                    # Les objets générés sont pour le joueur
      if len(inventaire_joueur) < 5:    # L'inventaire du joueur ne peut contenir plus de 5 objets
        inventaire_joueur.append(choix_objet())
    elif droit == 3:                    # Les objets générés sont pour le bot
      if len(inventaire_bot) < 5:       # L'inventaire du joueur ne peut contenir plus de 5 objets
        inventaire_bot.append(choix_objet())

  return inventaire_bot, inventaire_joueur, drop

            ########################################################
                  # Deuxième Fonction: Utilisation d'un objet
            ########################################################


##################################################
#  Utilisation des objets: Fonctions Secondaires
##################################################

def bombes(coordonnees):                   # Objet qui détruit les cases adverses
  caracteristique_BOM =[1, 20]
  caracteristique_BOM = caracteristique_BOM + coordonnees
  return caracteristique_BOM

def regenerateur_energie():     # Objet qui remet l'énergie au maximum suivant le tour
  caracteristique_REE = [2, 20, 100]
  return caracteristique_REE
    
def drop_leurre(coordonnees):              # Objet qui trompe l'adversaire
  caracteristique_DRL = [3, 50]
  caracteristique_DRL = caracteristique_DRL + coordonnees
  return caracteristique_DRL

def accelerateur_de_case():     # Objet qui accélère l'avancement du jeu
  caracteristique_ADC = [4, 50, 2]
  return caracteristique_ADC

def case_supplementaire(coordonnees):      # Objet qui autiorise 2 coups dans le même tour
  caracteristique_CAS = [5, 70, 1]
  caracteristique_CAS = caracteristique_CAS + coordonnees
  return caracteristique_CAS


#################################################
#   Utilisation des objets: Fonction Principale
#################################################

def objet_choisit(tour, numero_objet, coordonnees):
  if tour[1] == 1:      # Le joueur utilise un objet ou récupère le drop
    if inventaire_joueur[numero_objet] == 'BOM':
      return bombes(coordonnees)
    elif inventaire_joueur[numero_objet] == 'REE':
      return regenerateur_energie()
    elif inventaire_joueur[numero_objet] == 'DRL':
      return drop_leurre(coordonnees)
    elif inventaire_joueur[numero_objet] == 'ADC':
      return accelerateur_de_case()
    elif inventaire_joueur[numero_objet] == 'CAS':
      return case_supplementaire(coordonnees)


  elif tour[1] == 2:    # Le bot utilise un objet ou récupère le drop
    if inventaire_bot[numero_objet_bot] == 'BOM':
      return bombes(coordonnees)
    elif inventaire_bot[numero_objet_bot] == 'REE':
      return regenerateur_energie()
    elif inventaire_bot[numero_objet_bot] == 'DRL':
      return drop_leurre(coordonnees)
    elif inventaire_bot[numero_objet_bot] == 'ADC':
      return accelerateur_de_case()
    elif inventaire_bot[numero_objet_bot] == 'CAS':
      return case_supplementaire(coordonnees)    


############################            TEST            ############################

from random import randint #*#


x = randint(1, 16)
y = randint(1, 16)
tour = [0,1]
numero_objet_bot = 0 #*#
caracteristique_BOM = [] #*#
caracteristique_REE = [] #*#
caracteristique_DRL = [] #*#
caractéristique_ADC = [] #*#
caracteristique_CAS = [] #*#
objet_generes_aleatoire = ""

global objet_gene #*#
objet_gene = '' #*#

global numero_objet #*#
numero_objet = 0 #*#

global inventaire_joueur #*#
inventaire_joueur = [] #*#

global inventaire_bot #*#
inventaire_bot = [] #*#

global drop #*#
drop = [] #*#

global Jauge_Drain_joueur 
Jauge_Drain_joueur = 50

global Jauge_Drain_bot
Jauge_Drain_bot = 50

global objet_utilise #*#
objet_utilise = [] #*#

global coordonnees
coordonnees = [x, y]

  

for n in range(50):  # Génération sur 25 tours
  print(tour)
  print('')
  
  generation_objet(tour) #*#
  print("Objets du drop", drop)
  print("Objets du joueur", inventaire_joueur)
  if len(inventaire_joueur) == 5: #*#
    print("L'inventaire est plein") #*#
    print("")
  print("Objets du bot", inventaire_bot)
  print('')
  if tour[1] == 1:
    tour[1] = 2
  else:
    tour[1] = 1
    tour[0] += 1

    

# Utilisation des objets

for n in range(2):  #  A retirer pour l'integration

  # Le joueur choisit un objet
  if tour[1] == 1:  #*#
    print(tour)
    print('')
    numero_objet = int(input('numero_objet = ')) # On vérifie de quel objet il s'agit   #*#
    numero_objet = numero_objet - 1   #*#
    objet_utilise = objet_choisit(tour, numero_objet, coordonnees) # On trouve les caractéristiques de l'objet    #*#
    print(objet_utilise)

    if Jauge_Drain_joueur < objet_utilise[1]: #on vérifie qu'on a la capcité d'utiliser l'objet   #*#
      print("Impossible d'utiliser l'objet") #*#
      tour[1] = 2
      # Tour suivant
    else: #*#
      # Envoi de la liste objet-utilise au plateau pour les modifications
      del inventaire_joueur[numero_objet] #*#
      print(inventaire_joueur)
      tour[1] = 2
      # Tour suivant

 # Le bot utilise un objet
  elif tour[1] == 2:  #*#
    print(tour)
    print('')
    objet_gene = input('objet_gene = ') # On vérifie de quel objet il s'agit    #*#
    # Taper le nom de l'objet sans paranthèse, sinon le programe ne trouvera jamais   #*#
    
    while objet_gene != inventaire_bot[numero_objet_bot] or numero_objet_bot > 4:  #*#
      if objet_gene != inventaire_bot[numero_objet_bot]: #*#
        numero_objet_bot += 1 #*#
      else: #*#
        numero_objet_bot =+ 1 #*#
        print(numero_objet_bot)    
        
    objet_utilise = objet_choisit(tour, objet_gene, coordonnees) # On trouve les caractéristiques de l'objet    #*#
    print(objet_utilise)

    if Jauge_Drain_bot < objet_utilise[1]: #on vérifie qu'on a la capcité d'utiliser l'objet    #*#
      print("Impossible d'utiliser l'objet") #*#
      # Tour suivant
      tour[1] = 1
      tour[0] += 1
    else:   #*#
      # Envoi de la liste objet-utilise au plateau pour les modifications
      del inventaire_bot[numero_objet_bot]   #*#
      # Tour suivant
      print(inventaire_bot)
      tour[1] = 1
      tour[0] += 1


# Intégration

## A l'intégration certaines lignes du test seront à intégrées dans une fonction
## objet() qui sera celle appelée par le main, elles seront annotées de #*#.
## Les lignes que j'aurai signalées ne seront peut-être pas exhaustives
