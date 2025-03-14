Information sur le projet:
	Librairie utiliser:
		-NLP
		-tm

	Approche utiliser:
		Classifieur 1-plus-proche-voisin
			Descripteurs = mots apparaissant au moins 200 fois dans le corpus
			Pondération = fréquence du mot dans le document
			Distance = ditance euclidienne "au carré" (afin d'éviter un calcul inutile nous ne calculons pas la racine carée, à la fin de la formule de la distance euclidienne, nous donnons de ce fait le carré de la distance euclidienne)

	Erreur calculée sur les données d'entraînement:
		Erreur d'apprentissage pour le classifieur des 1-PPV sur les données d'entraînement = 25,52381 %
		Taux de réusite pour le classifieur des 1-PPV sur les données d'entraînement = 74,47619 %


Utilisation:
	Initialisation du projet:
	Lancer main.R, pour ce faire, lancer un terminal à l'intérieur du projet, démarer R (commande "R" dans le terminal) puis faire un source("main.R")

	Utilisation du projet:
	Dans R, taper utiliser la fonction classer qui prend en paramétre une chaine de caractére, correspondant au lien du fichier à classer

	Calcul du taux d'erreur d'aprentisage:
	Dans R, taper erreurkPPV(1,M)
	
	Calcul du taux de bonne clasification:
	Dans R, taper 1-erreurkPPV(1,M)

	Création du modéle et entrainement:
	Le modéle est sauvegardé dans "modele.RData"
	Il peut être recréer en executant le script "modele_et_apprentissage.r" pour ce faire, dans R faire source("modele_et_apprentissage.r"), attention pour recréer le modéle il faut au préalable décompresser la fichier "training.zip" qui contient les donnés d'entrainement


Auteurs:
	Longatte Léandre
	Viraud Florian
