ALLAIN Lucas
REVALIER Quentin

2A31

Challenge R

Librairies utilisées:
NLP
tm

Approche utilisée:
Classifieur 1-plus-proche-voisin
    Descripteurs = mots apparaissant au moins 300 fois dans le corpus
    Pondération = fréquence du mot dans le document
    Distance euclidienne 

Erreur calculée sur les données d'entraînement:
    Erreur d'apprentissage pour le classifieur des 1-PPV sur les données d'entraînement =  0.2352381 soit 23.52381 %
    Taux de réusite pour le classifieur des 1-PPV sur les données d'entraînement = 0.7647619 soit 76.47619 %


Initialisation du projet:
Ouvrir un terminal dan le dossier du projet et enter la commande: r
Lancer ensuite le fichier main.R avec la commande: source("main.r")

Utilisation du projet:
Une fois initilialisé, vous pouvez lancer la commande "classer" avec le fichier (chemin relatif + nom) dont vous voulez connaître la classe: classer("./lien/du/fichier")

Calcul du taux d'erreur d'aprentisage:
Dans le terminal toujours, tapez la commande:  erreurkPPV(1,mat)

Calcul du taux de bonne clasification:
Dans le terminal toujours, tapez la commande: bonneClassifKPPV(1, mat)

Création du modéle et entrainement:
Les fichiers de sauvegarde sont "vocab.rds" et "Mstr.rds"
Pour les recréer, il faut lancer test.r avec: source("test.r"), pensez à extraire l'archive "training" pour que le scrpit ai accès aux données d'entrainement.
