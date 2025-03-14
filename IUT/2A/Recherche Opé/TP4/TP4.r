#!/usr/bin/Rscript

# Rscript <nom fichier>

# IUT d'Orléans | Département Informatique
# Module Aide à la décision
# Feuille de TP4 : Classification par k-Plus Proches Voisins

# Ecrire vos réponses dans le fichier après chaque question et testez vos programmes au fur et à mesure dans la console

# L'objectif de ce TP est d'implémenter en R un classifieur k-PPV (k-Plus Proches Voisins) puis de le tester sur le jeu de données 'zoo.data'. Il s'agit d'un tableau contenant la description de 100 animaux selon 17 descripteurs (binaires ou numériques).
# La première colonne du tableau contient les noms des espèces et la dernière colonne renferme une étiquette de classe correspondant à une catégorie dans la classification des espèces (ex. reptiles (3), oiseaux (2), etc.).
# Les 17 descripteurs portent sur des caractéristiques physiologiques, biologiques ou comportementales de chaque animal (poils, plumes, oeufs, lait, aérien, aquatique, prédateur, dents, épine dorsale, respire, venimeux, nageoires, nb. pattes, queue, domestique, taille)

# 1. Charger le fichier 'zoo.data' dans un data.frame puis transformez-le en une matrice *data* (plus efficace pour les calculs à venir) en ayant pris soin d’enlever l’attribut des noms d’animaux que vous aurez stocké dans un vecteur *animaux* au préalable.
data <- read.csv("zoo.data", header=FALSE, sep=",", dec=".")
#data[,1]

animaux <- as.vector(data[,1])

data <- as.matrix(data[,-1])


# 2. Observez la distribution des classes sous forme d’un vecteur (table) puis visualisez-la à l’aide d’un graphique 'camembert' (pie).
 
classes <- table(data[,ncol(data)])
pie(classes)

# 3. Créez une fonction distance(x,y) qui retourne la distance euclidienne entre deux vecteurs x et y.

distance <- function(x,y){
    return (sqrt(sum(x-y)^2))
}

# 4. Créez une fonction dist.voisins(vecteur,data) qui calcule le vecteur des distances entre *vecteur* et chacun des objets de *data*.

dist.voisins <- function(vecteur,data){
    apply(data, 1, distance, vecteur)
} 

# 5. Créez une fonction kppv(vecteur, k, data) qui retourne le vecteur des indices des k plus proches voisins de l’objet *vecteur* dans *data* (en cas d’égalité, on retourne arbitrairement l’un des indices des objets équidistants).

kppv <- function(vecteur, k, data){
    return (order(dist.voisins(vecteur, data))[1:k])
}

kppv(data[1,],3,data)


# 6. Créez une fonction classerKPPV(vecteur,k,data) qui retourne la classe majoritaire parmi les k plus proches voisins de *vecteur* dans *data* (en cas d’égalité, on retourne arbitrairement l’une des classes majoritaires)

classeKPPV <- function(vecteur,k,data){
    classes <- table(data[kppv(vecteur, k, data), ncol(data)])
    return (sample(names(classes[classes == max(classes)]), 1))

}

classeKPPV(data[1,],10,data)


# 7. Ecrire une fonction erreurkPPV(k, data) qui calcule l’erreur d'“apprentissage” pour le classifieur des k-PPV sur *data*.
 
erreurKPPV <- function(k, data){
    res<-sapply(1:nrow(data), function(i)classeKPPV(data[i, -ncol(data)], k, data[-i, -ncol(data)]))
    return (sum(res == data[, ncol(data)]))
}

# 8. Créez un graphique qui représente l’évolution du taux d’erreur en fonction de k (identifiez les bornes pertinentes pour k).
 


# 9. Refaites ce même graphique en calculant les taux d’erreurs après normalisation des attributs (scale).
 

