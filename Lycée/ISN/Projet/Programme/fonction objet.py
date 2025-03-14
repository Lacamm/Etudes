            ########################################################
             # Première Fonction secondaire: Génération des objets
            ########################################################


###############################################
#  Génération des objets: Sous-Fonction 2
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
#   Génération des objets: Sous-Fonction 1
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
  elif tour[0]%3 == 0 and tour[0] != 0 and tour[1] == 0:
    nombre_objet_generes = 1
    droit = 2
  # On vérifie que les objets du bot tout les 3 tours(SES tours)
  elif tour[0]%3 == 0 and tour[0] != 0 and tour[1] == 1:
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
             # Deuxième Fonction secondaire: Utilisation des objets
            ########################################################


##################################################
#  Utilisation des objets: Sous-Fonction 2
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


##########################################################
#   Utilisation des objets: Sous-Fonction 1
##########################################################

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


############################            Fonctions principales            ############################
def objet(tour, coordonnes):

  caracteristique_BOM = []
  caracteristique_REE = []
  caracteristique_DRL = []
  caractéristique_ADC = []
  caracteristique_CAS = []

  generation_objet(tour)
  print("Objets du drop", drop)
  print("Objets du joueur", inventaire_joueur)
  if len(inventaire_joueur) == 5:
      print("L'inventaire est plein")
      print("")
  print("Objets du bot", inventaire_bot)
  print('')
  return inventaire_joueur, inventaire_bot, drop



        
def utilisation():

  objet_gene = ''
  numero_objet = 0
  
  if tour[1] == 0: # Le joueur choisit un objet
      numero_objet = int(input('numero_objet = ')) # On vérifie de quel objet il s'agit   #*#
      numero_objet = numero_objet - 1
      while 0 >= numero_objet and numero_objet > 5:
        print("L'inventaire a une limite de 5 objets")
        numero_objet = int(input('numero_objet = ')) # On vérifie de quel objet il s'agit   #*#
        numero_objet = numero_objet - 1
      objet_choisit(tour, numero_objet, coordonnees)
      objet_utilise = objet_choisit(tour, numero_objet, coordonnees) # On trouve les caractéristiques de l'objet    #*#
      print(objet_choisit(tour, numero_objet, coordonnees))
      
      if Jauge_Drain_joueur < objet_utilise[1]: #on vérifie qu'on a la capcité d'utiliser l'objet   #*#
        print("Impossible d'utiliser l'objet")  # Tour suivant
      else: #Envoi de la liste objet-utilise au plateau pour les modifications
        del inventaire_joueur[numero_objet] # Tour suivant

  
  elif tour[1] == 1: # Le bot utilise un objet
    objet_gene = input('objet_gene = ') # On vérifie de quel objet il s'agit
    # !!! Taper le nom de l'objet SANS PARANTHESES, sinon le programe ne trouvera jamais   #*#

  while objet_gene != 'BOM' and objet_gene != 'REE' and objet_gene != 'DRL' and objet_gene != 'ADC' and objet_gene != 'CAS':
    print("Le nom saisit est invalide")
    objet_gene = input('objet_gene = ')
    
  while objet_gene != inventaire_bot[numero_objet_bot]:
    if objet_gene != inventaire_bot[numero_objet_bot]:
        numero_objet_bot += 1
    else: 
      numero_objet_bot =+ 1
      break
    if numero_objet_bot > 4:
      print("Vous ne possédez pas cet objet")
      objet_gene = input('objet_gene = ')
      while objet_gene != 'BOM' and objet_gene != 'REE' and objet_gene != 'DRL' and objet_gene != 'ADC' and objet_gene != 'CAS':
        print("Le nom saisit est invalide")
        objet_gene = input('objet_gene = ')
      numero_objet_bot = 0

  objet_utilise = objet_choisit(tour, objet_gene, coordonnees) # On trouve les caractéristiques de l'objet    #*#

  if Jauge_Drain_bot < objet_utilise[1]: #on vérifie qu'on a la capcité d'utiliser l'objet    #*#
    print("Impossible d'utiliser l'objet")# Tour suivant
  else:# Envoi de la liste objet-utilise au plateau pour les modifications 
    del inventaire_bot[numero_objet_bot]   #*#
    return objet_utilise 
  
# Intégration

## A l'intégration certaines lignes du test seront à intégrées dans une fonction
## objet() qui sera celle appelée par le main, elles seront annotées de #*#.
## Les lignes que j'aurai signalées ne seront peut-être pas exhaustives


###########################################       Main     #########################################
from random import randint

global action
action = ''


def utilisateur(tour):
    if tour[1] == 0:
        return 'Joueur'
    else:
        return 'Bot'


x = 0
y = 0

global tour
tour = [1,0]
global numero_objet
numero_objet = 0
global inventaire_joueur
inventaire_joueur = []
global inventaire_bot
inventaire_bot = []
global drop
drop = []
global Jauge_Drain_joueur 
Jauge_Drain_joueur = 50
global Jauge_Drain_bot
Jauge_Drain_bot = 50
global objet_utilise
objet_utilise = []
global coordonnees
coordonnees = [x, y]


###############  Initialisation
print("""Dans ce programme vous allez pouvoir générer et 'utiliser' les objets de "Dominion" """)
print('')
nombre_tour = int(input('Combien de tours voulez vous jouer? '))
while nombre_tour < 0:
  print("La valeur saisie est incorrecte")
  nombre_tour = int(input('Combien de tours voulez vous jouer? '))

for z in range (2*nombre_tour): #On peut effectuer des actions à chaques tours
  x = randint(1, 16)
  y = randint(1, 16)
  print('Tour: ', tour[0])
  print('Utilisateur: ', utilisateur(tour)) ###############
  
  objet(tour, coordonnees) # On génère les objets

# On utilise des objets
  action = input('Voulez-vous utiliser un objet? oui/non ') # On vérifie de quel objet il s'agit
  while action != 'oui' and action != 'non':
      print("Cette action n'est pas valide")
      action = input('Voulez-vous utiliser un objet? oui/non ')

  if tour[1] == 0 and (action == 'oui')and len(inventaire_joueur) == 0: #On vérifie qu'on possède des objets
    print("Vous ne possédez pas d'objets")
  elif tour[1] == 1 and (action == 'oui')and len(inventaire_bot) == 0: #On vérifie qu'on possède des objets
    print("Vous ne possédez pas d'objets")
  elif action == 'non':
    action  = ''
  else:
    utilisation()  # Renvoi des caractériqtiques de l'objet
    print(utilisation())

#Possibilité de prendre le drop
  action = input('Voulez-vous récupérer le drop? oui/non ') #On vérifie qu'on veut prendre le drop
  while action != 'oui' and action != 'non':
      print("Cette action n'est pas valide")
      action = input('Voulez-vous récupérer le drop? oui/non ')

  if tour[1] == 0 and (action == 'oui'):
    a = 1
    # On vérifie le nombre d'objets que le joueur peut récupérer
  elif tour[1] == 1 and (action == 'oui'):
    a = 1
    # On vérifie le nombre d'objets que le bot récupérer
  else:
    action  = ''
    
  print('Tour suivant') # Tour suivant
  print('')
  
  if tour[1] == 0:
    tour[1] = 1
  else:
    tour[1] = 0
    tour[0] += 1
