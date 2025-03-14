# IUT d'Orléans | Département Informatique
# Module Aide à la décision
# Feuille de TP3

# Ecrire vos réponses dans le fichier après chaque question et testez vos programmes au fur et à mesure dans la console

#------------------------------------------------------------------------------------
# PARTIE 1 - Implémentation du classifieur de Bayes
#------------------------------------------------------------------------------------
# Dans cette partie nous supposerons que *dat* est une matrice contenant la description de nos objets, la dernière colonne correspondant à la classe (comme dans le TD3). Nous supposerons que *vec* est un vecteur représentant un objet à classer.

# 1. Construisez *dat* et *vec* à partir du fichier de données *champi.csv* disponible dans le cours Célène :
#    - *dat* servira d'ensemble d'entraînement et doit correspondre au dataframe initial, transformé en matrice et privé : des noms de champignons et de la dernière ligne dont l’étiquette de classe est inconnue
#    - *vec* servira d'exemple de test et doit contenir la dernière ligne du dataframe, privée : du nom du champignon et de la classe (à prédire).

data<-read.csv('champi.csv',header=T,sep=' ')
data<-as.matrix(data)
dat<-data[-10,-1]
vec<-data[10,c(-1,-7)]

# 2. Donnez une expression en R pour obtenir le vecteur des classes présentes dans *dat*. Nommez ce vecteur *classes* et stockez dans une variable *colClasse* le numéro de la colonne associée à la classe dans *dat*. 
colClasse<-ncol(dat)
classes<-names(table(dat[,colClasse]))

# 3. Créez un vecteur *lesClasses* correspondant à la colonne des classes dans *dat* puis supprimez la colonne des classes dans dat.
lesClasses<-dat[,colClasse]
dat<-dat[,-colClasse]

# 4. Créez un vecteur contenant la fréquence de chaque classe dans *dat* (stockez-le dans une variable *tailleClasse*).
tailleClasse<-table(lesClasses)

# 5. Créez un vecteur *probaClasse* contenant la probabilité (a priori) de chaque classe. 
probaClasse<-tailleClasse/length(lesClasses)

# 6. Écrivez une fonction *prAttVal(attribut,valeur,classe,data)* qui retourne la probabilité p(attribut=valeur|classe) observée dans une matrice *data* dont la dernière colonne contient les étiquettes de classes.
prAttVal<-function(attribut,valeur,classe,data){
  lesClasses<-data[,ncol(data)]
  tailleClasse<-table(lesClasses)
  return(sum((data[,attribut]==valeur)&(lesClasses==classe))/tailleClasse[classe])}

# 7. Créez une fonction qui, pour un vecteur, une classe et une matrice *data* passés en paramètres,retourne p(vecteur|classe) observée dans la matrice *data*.
prVec<-function(vecteur,classe,data){
  return(prod(sapply(1:length(vecteur),function(i)prAttVal(i,vecteur[i],classe,data))))}

# 8. Donnez une expression qui retourne le résultat de la classification d’un vecteur (classe prédite).
names(sort(sapply(classes,prVec,vecteur=vec,data=dat),decreasing=TRUE))[1]

# 9. En cas d’égalité (plusieurs classes ont la probabilité maximum), faites en sorte que la classe prédite soit la classe la plus fréquente.
p=sapply(classes,prVec,vecteur=vec,data=dat)
n<-names(p[p==max(p)])
if(length(n)>1) res<-names(which.max(probaClasse[n]))
else res<-n

# 10. Écrire une fonction *classerBayes(vecteur,data)* retournant la classe attribuée au vecteur *vec* à partir des observations décrites dans *data* dont la dernière colonne contient les étiquettes de classes.
classerBayes<-function(vecteur,data){
  lesClasses<-data[,ncol(data)]
  classes<-names(table(lesClasses))
  p<-sapply(classes,prVec,vecteur=vecteur,data=data)
  n<-names(p[p==max(p)])
  if(length(n)>1){
    probaClasse<-table(lesClasses)/length(lesClasses)
    return(names(which.max(probaClasse[n])))
    }
  else return(n)} 


#------------------------------------------------------------------------------------
# PARTIE 2 - Utilisation du classifieur de Bayes sur un jeu de données
#------------------------------------------------------------------------------------
# Dans cette seconde partie, nous allons utiliser ce classifieur sur un jeu de données réelles ("agaricus-lepiota.data" sur Célène), contenant la description de plus de 8000 champignons. Ce fichier sera partagé en :
#    - d’une part un ensemble d'apprentissage sur lequel les calculs de probabilités conditionnelles seront effectués,
#    - d’autre part un ensemble test sur lequel le classifieur sera testé.

# 1. Chargez le fichier dans un data-frame, sachant qu’il existe des valeurs manquantes (notées “?”dans le fichier).  Stockez dans une matrice *mush* les lignes pour lesquelles aucune valeur ne manque.
mushdf<-read.csv("agaricus-lepiota.data",header=FALSE,na.strings="?")
mush<-as.matrix(na.omit(mushdf))

# 2. Déplacez la première colonne de la matrice en dernière position.  Cette colonne contient les étiquettes de classes (e=edible,p=poisonous).
mush<-mush[,c(2:ncol(mush),1)]

# Cette matrice comporte beaucoup de données.  Pour vous mettre dans un contexte plus proche de votre projet (futur proche), on pourrait supposer que nous connaissons la classe de seulement 250 champignons

# 3. Après avoir comparé la distribution des classes des 250 premiers champignons de la matrice, par rapport à la distribution des classes sur tous les champignons, construisez un vecteur d’indices *learn* composé des indices des 125 premiers champignons de la classe "e" et des 125 premiers dela classe "p" (ensemble d'apprentissage).

# distribution des 250 premiers champignons
table(mush[1:250,ncol(mush)])
#pasdu tout représentative de la distribution sur le jeu de données complet 
table(mush[,ncol(mush)])
learn<-c(which(mush[,ncol(mush)]=="e")[1:125],which(mush[,ncol(mush)]=="p")[1:125])

# 4. Créez un vecteur *target* (ensemble de test) contenant les indices des champignons qui ne sont pas contenus dans *learn*. Nous ferons "comme si" nous ne connaissions pas la classe des champignons de *target* pour classer ces champignons.
target<-(1:nrow(mush))[-learn] 

# 5. Observez les probabilités conditionnelles des deux classes pour le champignon d’indice 306 dans le jeu de données initial. D’où vient ce résultat? Comment tenir compte de ce cas de figure dans la classification?

#On retrouve ici le problème d’une proba p(att=val|classe) nulle qui annule de fait la p(vec|classe). On modifie la fonction *prAttVal* de sorte à lui faire retourner une valeur très petite (ex.10−6) plutôt que 0 

# 6. Calculez l’erreur d’apprentissage (ou erreur d’entraînement) sur les champignons de l’ensemble learn.
predit<-apply(mush[learn,-23],1,classerBayes,data=mush[learn,])
erreurApp<-100*sum(predit!=mush[learn,23])/length(learn) 

# 7. Calculez l’erreur de généralisation sur les champignons de l’ensemble target.
predit<-apply(mush[target,-23],1,classerBayes,data=mush[learn,])
erreurGen<-100*sum(predit!=mush[target,23])/length(target)
table(predit,mush[target,23]) 