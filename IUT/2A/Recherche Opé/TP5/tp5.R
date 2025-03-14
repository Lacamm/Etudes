#installer les librairies utiles

#install.packages("tm")

#appel de la librairie tm
library(tm)

#chargement du corpus de textes
actu<-Corpus(DirSource("actu",recursive=TRUE))

#observer les types des objets actu, actu[1] et actu[[1]]
#class(actu)      #-->"SimpleCorpus" "Corpus"
#class(actu[1])   #-->"SimpleCorpus" "Corpus"
#class(actu[[1]]) #-->"PlainTextDocument" "TextDocument"
#class(actu[[1]]$content) #-->"character"
#que contiennent les variables : actu, actu[1] et actu[[1]]

#visualiser le contenu du 1er document (vecteur de chaînes de caractères)
#content(actu[[1]]) ou actu[[1]]$content


###############################################################
#2. on teste différentes fonctions spécifiques aux textes :
###############################################################

#tolower(actu[[1]])     # package de base R : renvoie un (vecteur de) chaînes de caractères en minuscules
#removePunctuation(actu[[1]])  # package tm : renvoie un PlainTextDocument sans ponctuation (utiliser content() pour observer le résultat)

#pour utiliser le stemmer il est nécessaire d'installer une librairie supplémentaire
#install.packages("SnowballC")
#stemDocument(actu[[1]],language='fr') # package tm : renvoie un PlainTextDocument avec racinisation (utiliser content() pour observer le résultat)
#removeNumbers(actu[[1]]) # package tm : renvoie un PlainTextDocument avec suppression des nombres (utiliser content() pour observer le résultat)
#stopwords("fr")     # package tm : 164 mots vides pour le français
#removeWords()   # package tm : suppression des mots passés en paramètre (vector)

nettoyage<-function(corpus){
    corpus<-tm_map(corpus,content_transformer(tolower))
    corpus<-tm_map(corpus,removeWords,words=stopwords('fr'))
    corpus<-tm_map(corpus,removePunctuation)
    corpus<-tm_map(corpus,removeNumbers)
    corpus<-tm_map(corpus,stemDocument,language='fr')
}

#nettoyage de notre corpus brut
actuN<-nettoyage(actu)


###############################################################
#3. vectorisation
###############################################################

mat<-DocumentTermMatrix(actuN)
#mat
#<<DocumentTermMatrix (documents: 15, terms: 2401)>>
#Non-/sparse entries: 4213/31802
#Sparsity           : 88%
#Maximal term length: 123
#Weighting          : term frequency (tf)

#liste des termes utilisés comme descripteurs
#mat$dimnames$Terms

#termes qui apparaissent au moins 20 fois dans le corpus
#findFreqTerms(mat,20)

#taille du vocabulaire vs. fréquence d'apparition
#vec<-sapply(1:50,function(x) length(findFreqTerms(mat,x)))
#plot(vec,type="l")

#nouvelle représentation avec seulement les mots qui apparaissent au moins 20 fois dans le corpus
vocab<-findFreqTerms(mat,20)
mat20<-DocumentTermMatrix(actuN,list(dictionary=vocab))
#mat20
#<<DocumentTermMatrix (documents: 15, terms: 33)>>
#Non-/sparse entries: 246/249
#Sparsity           : 50%
#Maximal term length: 8
#Weighting          : term frequency (tf)


###############################################################
#4. classification
###############################################################

#préparation de la matrice R pour la classification (on rajoute la colonne de classe en dernière position)
M<-cbind(as.matrix(mat20),c(rep(1,5),rep(2,5),rep(3,5)))

#test du classifieur 1-PPV
source("../TP4/TP4_correction.r")
erreurkPPV(k=1,data=M)
#[1] 0.1333333

#Visualiser la matrice des distances euclidiennes entre chaque paire de documents
#image(1:15,1:15,as.matrix(dist(M[,-ncol(M)])))

#test avec pondération binaire des vecteurs (présence/absence)
#mat20bin<-weightBin(mat20)
#Mbin<-cbind(as.matrix(mat20bin),c(rep(1,5),rep(2,5),rep(3,5)))
#erreurkPPV(k=1,data=Mbin)
#[1] 0.2

#test avec pondération tfIdf des vecteurs (présence/absence)
#mat20tfidf<-weightTfIdf(mat20)
#Mtfidf<-cbind(as.matrix(mat20tfidf),c(rep(1,5),rep(2,5),rep(3,5)))
#erreurkPPV(k=1,data=Mtfidf)
#[1] 0.3333333


###############################################################
#5. préparation et classification d'un nouveau texte
###############################################################

#new<-Corpus(URISource("newText.txt"))
#newN<-nettoyage(new)
#newMat<-DocumentTermMatrix(newN,list(dictionary=vocab))
#classerKPPV(k=1,vecteur=as.matrix(newMat)[,colnames(M)[-ncol(M)]],data=M)
#[1] "3"
