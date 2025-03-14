from random import randint


###Fonctions###

def choix_mot(liste_Mot):
    
    index_Mot = randint(0,9)# choix du mot à trouver dans la liste
    mot_Mystere = liste_Mot[index_Mot]
    resultat = "-"*len(mot_Mystere)
    resultat_Liste = []
    
    for n in range(len(mot_Mystere)):
        resultat_Liste.append("-")
        
    return resultat, resultat_Liste, mot_Mystere # variables contenat les lettres testées bonnes et le mot à trouver

def presence_Lettre(index_Lettre,mot_Mystere):
    
    lettre = str(input("Une lettre: ")) # choix des lettre à vérifier
    for n in range(len(mot_Mystere)): # on regarde combien de fois la lettre
        if lettre == mot_Mystere[n]:     # apparait dans le mot
            index_Lettre.append(n)
    return index_Lettre

def ajout_Lettre(index_Lettre):                    
    for n in range(len(index_Lettre)): # on ajoute dans resultat les lettres
        resultat_Liste[index_Lettre[0]] = lettre #choisies si elles si trouvent
        resultat = "".join(resultat_Liste)
        index_Lettre.remove(index_Lettre[0])
        print(resultat)
             
    index_Lettre.clear()
    essais += 1
    issue(resultat, mot_Mystere) 
    
    return resultat_Liste, victoire, resultat

def issue(resultat, mot_Mystere):
    if resultat == mot_Mystere: # on vérifie si le mot est trouvé avant les 10 essais
        victoire = "Vous avez trouvé le mot Mystère !!!"
        essais= 10
    elif resultat != mot_Mystere: # on vérifie si le mot est trouvé après les 10 essais
        victoire = "Vous n'avez pas trouvé le mot Mystère ..."
    return essais, victoire
            
print(victoire)

                                 ###Programme###


###Variables###

liste_Mot = ["cheval","route","voiture","entrepot","cargaison","industrie",
             "jockey","ensemble","ordinateur","chaise"] # liste de mot à trouver
index_Lettre = []
global essais
essais = 1
global victoire
victoire = ""

###Début###

choix_mot(liste_Mot)

print(resultat)
print(mot_Mystere)

while essais < 10: # nombre de tentatives
    presence_Lettre(index_Lettre,mot_Mystere)